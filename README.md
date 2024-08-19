[中文](README.zh.md)

# Qwen2-Boundless

Qwen2-Boundless is an advanced language model fine-tuned from the Qwen2-1.5B-Instruct model. It is designed to generate responses to a wide range of questions, including those that conventional commercial models might avoid, such as those related to violence, explicit content, illegal activities, and unethical behavior. Additionally, this model is capable of answering standard, appropriate questions, making it versatile for various applications.

## Features

- **Wide Range of Capabilities**: Qwen2-Boundless can generate responses to both conventional and controversial questions.
- **Specialized Datasets**: The model is fine-tuned using [Bad_Data.json](https://huggingface.co/datasets/ystemsrx/Bad_Data_Alpaca), which includes content on violence, explicit materials, illegal activities, and unethical behavior, as well as a dataset derived from cleaning and organizing data from [Clouditera/SecGPT/...](https://github.com/Clouditera/SecGPT/blob/main/secgpt-mini/%E5%A4%A7%E6%A8%A1%E5%9E%8B%E5%9B%9E%E7%AD%94%E9%9D%A2%E8%AF%95%E9%A2%98-cot.txt), which focuses on cybersecurity issues.
- **Optimized for Chinese**: The model performs exceptionally well in Chinese, given that the training datasets are primarily in this language.
- **Fine-Tuning Framework**: The model was fine-tuned using the [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory) project.

## Usage

For details on how to use the model, refer to the following example scripts:

- **Basic Usage**: [basic_usage.py](./basic_usage.py)
- **Continuous Conversation**: [continuous_conversation.py](./continuous_conversation.py)
- **Streamed Output**: [streamed_output.py](./streamed_output.py)

## Model Information

- **Model Name**: Qwen2-Boundless
- **Base Model**: Qwen2-1.5B-Instruct
- **[Datasets](Datasets)**:
  - [Bad_Data.json](https://huggingface.co/datasets/ystemsrx/Bad_Data_Alpaca)
  - [Clouditera/SecGPT/...](https://github.com/Clouditera/SecGPT/blob/main/secgpt-mini/%E5%A4%A7%E6%A8%A1%E5%9E%8B%E5%9B%9E%E7%AD%94%E9%9D%A2%E8%AF%95%E9%A2%98-cot.txt)
- **Language**: Primarily optimized for Chinese

## Disclaimer

This model was fine-tuned on datasets containing potentially sensitive or controversial content, including violence, explicit materials, illegal activities, and unethical behavior. Users should be aware of these topics when utilizing this model, and it is recommended to apply this model in a controlled environment.

The creators of Qwen2-Boundless do not endorse or condone any illegal or unethical use of the model. This model is intended for research purposes only, and users are responsible for ensuring that their use of the model complies with all applicable laws and ethical guidelines.

## License

This project is licensed under the Apache 2.0 License. See the [LICENSE](./LICENSE) file for details.

## Acknowledgments

Special thanks to the developers of the Qwen2-1.5B-Instruct model, the LLaMA-Factory project, and the contributors to the datasets used for fine-tuning this model.
