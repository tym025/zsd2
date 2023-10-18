# pip install -q -U bitsandbytes
# pip install -q -U git+https://github.com/huggingface/transformers.git
# pip install -q -U git+https://github.com/huggingface/peft.git
# pip install -q -U git+https://github.com/huggingface/accelerate.git
# pip install -q datasets

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from peft import prepare_model_for_kbit_training
from peft import LoraConfig, get_peft_model
from datasets import load_dataset

model_id = "rnosov/Wizard-Vicuna-13B-Uncensored-HF-sharded"
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16
)

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, quantization_config=bnb_config, device_map={"":0})

model.gradient_checkpointing_enable()
model = prepare_model_for_kbit_training(model)

# Liczba trenowanych parametrów
def print_trainable_parameters(model):
    trainable_params = 0
    all_param = 0
    for _, param in model.named_parameters():
        all_param += param.numel()
        if param.requires_grad:
            trainable_params += param.numel()
    print(
        f"parametry do wytrenowania: {trainable_params} || wszystkie parametry w sieci: {all_param} || trenowalne%: {100 * trainable_params / all_param}"
    )

config = LoraConfig(
    r=32,
    lora_alpha=24,
    target_modules =[
                      "q_proj",
                      "k_proj",
                      "v_proj",
                      "o_proj"
                      "gate_proj",
                      "up_proj",
                      "down_proj",
                      "lm_head"
                    ],
                    lora_dropout=0.05,
                    bias="none",
                    task_type="CAUSAL_LM"
)

model = get_peft_model(model, config)
print_trainable_parameters(model)

# Ładowanie datasetów
def generate_prompt(data_point):
  return data_point["combined"].strip()

def generate_and_tokenize_prompt(data_point):
  full_prompt = generate_prompt(data_point)
  tokenized_full_prompt = tokenizer(full_prompt, truncation=True)
  return tokenized_full_prompt

dataset_train = load_dataset("json", data_files="output_train.json")
dataset_valid = load_dataset("json", data_files="output_valid.json")

dataset_train = dataset_train.shuffle().map(generate_and_tokenize_prompt)
dataset_valid = dataset_valid.shuffle().map(generate_and_tokenize_prompt)

import transformers

tokenizer.pad_token = tokenizer.eos_token

trainer = transformers.Trainer(
    model=model,
    train_dataset=dataset_train['train'],
    eval_dataset=dataset_valid['train'],
    args=transformers.TrainingArguments(
        per_device_train_batch_size=4,
        gradient_accumulation_steps=4,
        warmup_steps=10,
        max_steps=250,
        learning_rate=3e-5,
        fp16=True,
        logging_steps=1,
        output_dir="outputs4",
        optim="paged_adamw_8bit",
        num_train_epochs=3,
        logging_dir="./logs",        # Directory for storing logs
        save_strategy="steps",       # Save the model checkpoint every logging step
        save_steps=25,                # Save checkpoints every 50 steps
        evaluation_strategy="steps", # Evaluate the model every logging step
        eval_steps=25,               # Evaluate and save checkpoints every 50 steps
        do_eval=True,                # Perform evaluation at the end of training
    ),
    data_collator=transformers.DataCollatorForLanguageModeling(tokenizer, mlm=False),
)
model.config.use_cache = False  # silence the warnings. Please re-enable for inference!
trainer.train()