import autotrain
import huggingface_hub
from transformers import HfFolder
import os

token = 'token_here'
folder = HfFolder()
os.makedirs(folder.path, exist_ok=True)
with open(folder.token_file, "w", encoding="utf-8") as token_file:
    token_file.write(token)

# !autotrain llm --train --project_name 'llama2-openassistant' --model TinyPixel/Llama-2-7B-bf16-sharded -- data_path timdettmers/openassistant-guanaco --use_peft --use_int4 --learning_rate 2e-4 --train_batch_size 1 --num_train_epochs 1 --trainer sft --model_max_length 2048 --push_to_hub --repo_id Promptengineering/llama2-openassistant --block_size 2048 > training.log &



