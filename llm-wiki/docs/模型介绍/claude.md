# Claude 系列

## 概述

Claude 由 Anthropic 公司开发，核心理念是 **安全、诚实、有益**（Helpful, Honest, Harmless）。

## 发展历程

| 版本 | 发布时间 | 特点 |
|------|----------|------|
| Claude 1 | 2023.03 | 首批注重安全的对话模型 |
| Claude 2 | 2023.07 | 支持 100K 上下文 |
| Claude 3 | 2024.03 | Haiku / Sonnet / Opus 三档 |
| Claude 3.5 | 2024.06 | Sonnet 编码能力突出 |
| Claude 4 | 2026 | 更强的多模态与推理能力 |

## 核心特色

### 长上下文
Claude 支持高达 200K token 的上下文窗口，可一次性处理整本书。

### 安全性（Constitutional AI）
Claude 采用宪法式 AI 训练，通过一套原则自我约束，而非单纯依赖人类反馈。

### 工具使用（Tool Use）
原生支持 Function Calling，可调用外部工具和 API。

## API 调用示例

```python
import anthropic

client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "用 Python 写一个冒泡排序"}
    ]
)
print(response.content[0].text)
```

## 优缺点

- ✅ 长上下文能力突出（200K）
- ✅ 安全性高，拒绝不当请求
- ✅ 中文理解与生成质量好
- ✅ 编码能力强（Sonnet 4.6）
- ❌ 多模态能力相对较弱
- ❌ 创意写作有时偏保守
