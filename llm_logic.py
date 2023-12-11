import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from peft import PeftModel

class LLM:
    def __init__(self):
        model7b = "vilsonrodrigues/falcon-7b-sharded"
        model13b = "rnosov/Wizard-Vicuna-13B-Uncensored-HF-sharded"

        self.model_id = model13b
        self.bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_use_double_quant=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.bfloat16
        )

        self.tokenizer = AutoTokenizer.from_pretrained(self.model_id)
        self.model = AutoModelForCausalLM.from_pretrained(self.model_id, quantization_config=self.bnb_config, device_map={"":0})

        torch.cuda.empty_cache()

        tokenizer = AutoTokenizer.from_pretrained(self.model_id, trust_remote_code=True)
        tokenizer.pad_token = tokenizer.eos_token

        self.path = "/content/drive/MyDrive/llm-finetune-0.76" # Wstaw ściężkę do twojej QLORY

        self.ft_model = PeftModel.from_pretrained(self.model, self.path)
        self.ft_model = self.ft_model.to("cuda")  # Move the model to the GPU
        self.model = None

    def reply(self, input):
        eval_prompt = f"##USER: {input} ##COMMAND: "
        model_input = self.tokenizer(eval_prompt, return_tensors="pt")

        self.ft_model.eval()
        with torch.no_grad():
            return(self.tokenizer.decode(self.ft_model.generate(**model_input, max_new_tokens=50, pad_token_id=2)[0], skip_special_tokens=True))