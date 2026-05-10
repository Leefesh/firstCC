# Token 与分词

## 什么是 Token

Token 是 LLM 处理文本的最小单位。一句话会被分割成若干个 Token 再输入模型。

## 分词方式

| 方式 | 示例 | 说明 |
|------|------|------|
| 词级分词 | "Hello world" → ["Hello", "world"] | 简单但词表太大 |
| 字符级分词 | "Hello" → ["H","e","l","l","o"] | 词表小但序列太长 |
| **子词分词**（BPE） | "unbelievable" → ["un", "believe", "able"] | **最常用，平衡词表大小与序列长度** |

## Token 数量估算

- 英文：约 1 个单词 = 1.3 个 Token
- 中文：约 1 个汉字 = 1.5 ~ 2 个 Token

## 为什么 Token 重要

- **上下文窗口**：模型能处理的 Token 数量有上限（如 128K）
- **计费**：大多数 API 按 Token 收费
- **性能**：长文本消耗更多计算资源

## 实用工具

- [OpenAI Tokenizer](https://platform.openai.com/tokenizer) - 在线查看文本的 Token 切分
