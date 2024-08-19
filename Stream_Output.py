import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, TextIteratorStreamer
from transformers.trainer_utils import set_seed
from threading import Thread
import random
import os

DEFAULT_CKPT_PATH = os.path.dirname(os.path.abspath(__file__))

def _load_model_tokenizer(checkpoint_path, cpu_only):
    tokenizer = AutoTokenizer.from_pretrained(checkpoint_path, resume_download=True)

    device_map = "cpu" if cpu_only else "auto"

    model = AutoModelForCausalLM.from_pretrained(
        checkpoint_path,
        torch_dtype="auto",
        device_map=device_map,
        resume_download=True,
    ).eval()
    model.generation_config.max_new_tokens = 512    # For chat.

    return model, tokenizer

def _get_input() -> str:
    while True:
        try:
            message = input('User: ').strip()
        except UnicodeDecodeError:
            print('[ERROR] Encoding error in input')
            continue
        except KeyboardInterrupt:
            exit(1)
        if message:
            return message
        print('[ERROR] Query is empty')

def _chat_stream(model, tokenizer, query, history):
    conversation = [
        {'role': 'system', 'content': ''},
    ]
    for query_h, response_h in history:
        conversation.append({'role': 'user', 'content': query_h})
        conversation.append({'role': 'assistant', 'content': response_h})
    conversation.append({'role': 'user', 'content': query})
    inputs = tokenizer.apply_chat_template(
        conversation,
        add_generation_prompt=True,
        return_tensors='pt',
    )
    inputs = inputs.to(model.device)
    streamer = TextIteratorStreamer(tokenizer=tokenizer, skip_prompt=True, timeout=60.0, skip_special_tokens=True)
    generation_kwargs = dict(
        input_ids=inputs,
        streamer=streamer,
    )
    thread = Thread(target=model.generate, kwargs=generation_kwargs)
    thread.start()

    for new_text in streamer:
        yield new_text

def main():
    checkpoint_path = DEFAULT_CKPT_PATH
    seed = random.randint(0, 2**32 - 1)  # 随机生成一个种子
    set_seed(seed)  # 设置随机种子
    cpu_only = False

    history = []

    model, tokenizer = _load_model_tokenizer(checkpoint_path, cpu_only)

    while True:
        query = _get_input()

        print(f"\nUser: {query}")
        print(f"\nAssistant: ", end="")
        try:
            partial_text = ''
            for new_text in _chat_stream(model, tokenizer, query, history):
                print(new_text, end='', flush=True)
                partial_text += new_text
            print()
            history.append((query, partial_text))

        except KeyboardInterrupt:
            print('Generation interrupted')
            continue

if __name__ == "__main__":
    main()
