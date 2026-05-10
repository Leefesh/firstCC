# Transformer 架构

## 概述

Transformer 是 2017 年 Google 在论文《Attention Is All You Need》中提出的架构，是现代 LLM 的基础。

## 核心结构

```
输入 → 嵌入层 → 多头注意力 → 前馈网络 → 输出
                ↕
            位置编码
```

### 1. 嵌入层（Embedding）
将每个 Token 映射为高维向量，让模型能处理离散的文本。

### 2. 位置编码（Positional Encoding）
由于 Transformer 没有循环结构，需要额外注入位置信息，让模型知道单词的顺序。

### 3. 多头注意力（Multi-Head Attention）
并行计算多组注意力，捕捉不同维度的语义关系。

### 4. 前馈网络（Feed-Forward Network）
对注意力层的输出做非线性变换，增加模型的表达能力。

## 为什么 Transformer 这么强

- **并行计算**：不像 RNN 需要串行处理，训练速度快
- **长程依赖**：注意力机制可以直接建模任意两个位置的关系
- **可扩展**：堆叠更多层、增大参数量即可提升能力
