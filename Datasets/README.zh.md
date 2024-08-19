[English](README.md)

# 数据集

此目录包含用于微调 Qwen2-Boundless 模型的数据集。以下是每个数据集的简要说明。

## 数据集

### 1. [Bad_Data.json](Bad_Data.json)

- **描述**: 该数据集包含可能涉及暴力、色情、违法行为和不道德行为的内容。它是专门编译用于使模型能够生成对各种问题的回答，包括那些敏感或有争议的内容。
  
- **警告**: [Bad_Data.json](Bad_Data.json) 中的内容可能引起不适或不适合某些观众观看。请谨慎处理。

### 2. [Cybersecurity.json](Cybersecurity.json)

- **描述**: 该数据集是从 [Clouditera/SecGPT/...](https://github.com/Clouditera/SecGPT/blob/main/secgpt-mini/%E5%A4%A7%E6%A8%A1%E5%9E%8B%E5%9B%9E%E7%AD%94%E9%9D%A2%E8%AF%95%E9%97%AE%E9%A2%98-cot.txt) 项目中清洗和整理得到的数据，主要涉及网络安全相关的问题。该数据集用于微调模型，使其能够提供关于这些主题的详细和专业的回答。

## 免责声明

**重要声明**: [Bad_Data.json](Bad_Data.json) 数据集中包含的内容可能具有冒犯性、令人不安或不适合所有人观看。该数据集的内容仅用于研究和开发目的，并不表示对其内容所涉及主题的支持或推广。

用户必须谨慎处理此数据集，并确保其使用符合所有适用的法律和道德准则。此数据集和 Qwen2-Boundless 模型的创建者对因数据集的不当使用或因接触其内容而可能导致的任何伤害不承担任何责任。
