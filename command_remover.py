with open('output_valid.json', 'r') as f:
    lines = f.readlines()

import re

for i, line in enumerate(lines):
    if '##SYSTEM' in line:
        lines[i] = re.sub(r'##COMMAND.*?##SYSTEM:', '', line)

with open('output_valid_no_comm.json', 'w') as f:
    for line in lines:
        f.write(line)
