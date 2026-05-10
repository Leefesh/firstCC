# LLaMA 系列

## 概述

LLaMA（Large Language Model Meta AI）是 Meta 开源的大语言模型系列，是目前开源社区的标杆。

## 发展历程

| 版本 | 发布时间 | 特点 |
|------|----------|------|
| LLaMA | 2023.02 | 只发布权重，学术使用 |
| LLaMA 2 | 2023.07 | 开源商用，附 ChatGPT 版 |
| LLaMA 3 | 2024.04 | 8B / 70B，性能飞跃 |
| LLaMA 3.1 | 2024.07 | 405B 最大开源模型 |
| LLaMA 4 | 2025+ | MoE 架构，更强 |

## 为什么 LLaMA 重要

- **完全开源**：权重、代码、论文全部公开
- **社区生态**：衍生出 Alpaca、Vicuna、Llama-Chinese 等大量微调版本
- **本地部署**：8B 模型可在消费级显卡上运行
- **研究基础**：很多学术界工作的基准模型

## 本地运行示例（Ollama）

```bash
# 安装 Ollama 后
ollama run llama3.1

# 或通过 API
curl http://localhost:11434/api/generate -d '{
  "model": "llama3.1",
  "prompt": "Hello!"
}'
```

## 优缺点

- ✅ 开源，可控，可本地部署
- ✅ 社区活跃，生态丰富
- ✅ 可微调定制
- ❌ 小参数版本能力不如同代闭源模型
- ❌ 需要一定技术能力部署
