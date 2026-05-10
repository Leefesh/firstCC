# GPT 系列

## 发展历程

| 版本 | 发布时间 | 参数量 | 特点 |
|------|----------|--------|------|
| GPT-1 | 2018.06 | 117M | 证明单向 Transformer 预训练有效 |
| GPT-2 | 2019.02 | 1.5B | 零样本泛化能力，一度因安全顾虑延迟发布 |
| GPT-3 | 2020.06 | 175B | 涌现 In-Context Learning 能力 |
| GPT-3.5 | 2022.03 | - | Codex + InstructGPT，ChatGPT 基础 |
| GPT-4 | 2023.03 | 推测 1.8T | 多模态，推理能力大幅提升 |
| GPT-4o | 2024.05 | - | 全模态，低延迟 |
| o1/o3 | 2024-2025 | - | 推理链（Chain-of-Thought），深度思考 |

## 核心技术

- **生成式预训练**：从左到右预测下一个 Token
- **InstructGPT / RLHF**：通过人类反馈对齐
- **System Prompt**：通过系统消息控制行为

## API 使用

```python
from openai import OpenAI

client = OpenAI()
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "你是 helpful 助手"},
        {"role": "user", "content": "你好"}
    ]
)
print(response.choices[0].message.content)
```

## 优缺点

- ✅ 综合能力强，生态成熟
- ✅ API 稳定，文档完善
- ❌ 闭源，价格较高
- ❌ 数据送回美国处理
