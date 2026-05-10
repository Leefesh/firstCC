# DeepSeek

## 概述

DeepSeek 由深度求索（DeepSeek）公司开发，是来自中国的开源大语言模型，以高性价比和出色表现著称。

## 发展历程

| 版本 | 发布时间 | 特点 |
|------|----------|------|
| DeepSeek LLM | 2023.11 | 67B 基础模型 |
| DeepSeek-V2 | 2024.05 | MoE 架构，236B 总参/21B 激活 |
| DeepSeek-R1 | 2025.01 | 开源推理模型，思维链 + 强化学习 |
| DeepSeek-V3 | 2025.12 | 671B MoE，高性能低成本 |

## 核心特色

### MoE（混合专家）
DeepSeek-V3 采用 MoE 架构，总参数量 671B，但每个 Token 只激活 37B 参数，兼顾性能与效率。

### 推理能力（R1）
DeepSeek-R1 通过强化学习训练长思维链，数学和推理能力与 OpenAI o1 相当，完全开源。

### 性价比
训练成本仅为同级别模型的 1/10，API 价格极具竞争力。

## API 调用

```python
from openai import OpenAI

client = OpenAI(
    api_key="your-api-key",
    base_url="https://api.deepseek.com"
)
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": "你好"}]
)
```

## 优缺点

- ✅ 开源，权重可下载
- ✅ 性价比极高
- ✅ 推理能力（R1）开源领域领先
- ✅ 中文支持好
- ❌ 英文综合能力略逊 GPT-4o
- ❌ 生态与周边工具不如 LLaMA 丰富
