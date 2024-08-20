from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import os

device = "cuda"  # the device to load the model onto

# 获取当前脚本所在的目录
current_directory = os.path.dirname(os.path.abspath(__file__))

model = AutoModelForCausalLM.from_pretrained(
    current_directory,
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(current_directory)

messages = [
    {"role": "system", "content": ""}
]

while True:
    # 获取用户输入
    user_input = input("User: ")

    # 将用户输入添加到对话中
    messages.append({"role": "user", "content": user_input})

    # 准备输入文本
    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )
    model_inputs = tokenizer([text], return_tensors="pt").to(device)

    # 生成响应
    generated_ids = model.generate(
        model_inputs.input_ids,
        max_new_tokens=512
    )
    generated_ids = [
        output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
    ]

    # 解码并打印响应
    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    print(f"Assistant: {response}")

    # 将生成的响应添加到对话中
    messages.append({"role": "assistant", "content": response})
