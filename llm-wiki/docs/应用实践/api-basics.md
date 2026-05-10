# API 调用入门

## 基础概念

LLM API 的核心是**对话补全（Chat Completion）**：传入消息列表，模型返回回复。

## 消息结构

```python
messages = [
    {"role": "system", "content": "系统设定，控制模型行为"},
    {"role": "user", "content": "用户输入"},
    {"role": "assistant", "content": "模型回复"},  # 历史对话
    {"role": "user", "content": "新的问题"}
]
```

## 常用参数

| 参数 | 作用 | 建议值 |
|------|------|--------|
| `model` | 指定模型 | - |
| `temperature` | 控制随机性 | 0-2，默认 1 |
| `max_tokens` | 最大输出长度 | 按需设置 |
| `top_p` | 核采样 | 0-1，默认 1 |
| `stream` | 流式输出 | True/False |

## 对话补全示例

=== "OpenAI"

    ```python
    from openai import OpenAI

    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": "你好"}],
        temperature=0.7,
        max_tokens=500,
        stream=True
    )
    for chunk in response:
        print(chunk.choices[0].delta.content, end="")
    ```

=== "Anthropic"

    ```python
    import anthropic

    client = anthropic.Anthropic()
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=[{"role": "user", "content": "你好"}]
    )
    print(response.content[0].text)
    ```

=== "DeepSeek"

    ```python
    from openai import OpenAI

    client = OpenAI(
        api_key="sk-xxx",
        base_url="https://api.deepseek.com"
    )
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": "你好"}]
    )
    ```

## 流式输出（Streaming）

逐 Token 返回而非等待全部生成，用户体验更好。

```python
# 上面 OpenAI 示例已是流式
# stream=True 时返回迭代器，逐个 Token 输出
```

## 常见错误处理

| 错误 | 原因 | 解决 |
|------|------|------|
| 401 | API Key 无效 | 检查密钥 |
| 429 | 速率限制 | 加入重试逻辑 |
| 400 | 请求格式错误 | 检查参数 |
| 500 | 服务端错误 | 等待重试 |

## 费用估算

```
输入 Token 价格（每百万） + 输出 Token 价格（每百万） = 总费用

例：gpt-4o $2.50/$10.00 per 1M tokens
一条 500 token 的对话 ≈ $0.00125 ~ $0.005
```
