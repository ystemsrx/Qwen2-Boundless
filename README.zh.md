# Qwen2-Boundless

Qwen2-Boundless 是一个从 Qwen2-1.5B-Instruct 模型微调而来的高级语言模型。它能够生成对各种问题的回答，包括那些传统商业模型可能会回避的内容，如暴力、色情、违法行为和不道德行为。此外，该模型也能回答常规的合适问题，适用于多种应用场景。

## 特性

- **广泛的应答能力**: Qwen2-Boundless 可以生成对常规和敏感问题的回答。
- **专门的数据集**: 模型经过 [Bad_Data.json](https://huggingface.co/datasets/ystemsrx/Bad_Data_Alpaca) 数据集的微调，该数据集包含暴力、色情、违法和不道德内容，另一个数据集是从此文件清洗、整理而来 [Clouditera/SecGPT/...](https://github.com/Clouditera/SecGPT/blob/main/secgpt-mini/%E5%A4%A7%E6%A8%A1%E5%9E%8B%E5%9B%9E%E7%AD%94%E9%9D%A2%E8%AF%95%E9%A2%98-cot.txt)，主要涉及网络安全问题。
- **优化中文表现**: 由于训练数据集主要为中文，模型在中文上表现优异。
- **微调框架**: 模型使用 [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory) 项目进行微调。

## 使用方法

有关如何使用该模型的详细信息，请参阅以下示例脚本：

- **基础使用**: [basic_usage.py](./basic_usage.py)
- **连续对话**: [continuous_conversation.py](./continuous_conversation.py)
- **流式输出**: [streamed_output.py](./streamed_output.py)

## 模型信息

- **模型名称**: Qwen2-Boundless
- **基础模型**: Qwen2-1.5B-Instruct
- **数据集**:
  - [Bad_Data.json](https://huggingface.co/datasets/ystemsrx/Bad_Data_Alpaca)
  - [Clouditera/SecGPT/...](https://github.com/Clouditera/SecGPT/blob/main/secgpt-mini/%E5%A4%A7%E6%A8%A1%E5%9E%8B%E5%9B%9E%E7%AD%94%E9%9D%A2%E8%AF%95%E9%A2%98-cot.txt)
- **语言**: 主要针对中文进行了优化

## 免责声明

该模型在包含潜在敏感或争议内容的数据集上进行了微调，包括暴力、色情、违法行为和不道德行为。用户在使用该模型时应充分意识到这些内容，建议在受控环境下应用此模型。

Qwen2-Boundless 的创建者不认可或支持任何非法或不道德的使用。该模型仅供研究用途，用户应确保其使用符合所有适用的法律和道德规范。

## 许可证

本项目采用 Apache 2.0 许可证。详情请参阅 [LICENSE](./LICENSE) 文件。

## 鸣谢

特别感谢 Qwen2-1.5B-Instruct 模型的开发者、LLaMA-Factory 项目，以及为微调该模型的数据集贡献者。
