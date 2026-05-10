# AI 学习路线图

> 从零到一，系统学习人工智能和大语言模型。本文按阶段划分，适合循序渐进。

---

## 路线总览

```
阶段一：感性认识 （1-2 周）
    ↓
阶段二：上手实践 （2-4 周）
    ↓
阶段三：理论基础 （4-8 周）
    ↓
阶段四：深入方向 （持续）
```

---

## 阶段一：感性认识（别怕，先玩起来）

**目标**：知道 AI 能干什么，建立直观感受，不要被术语吓到。

### 做什么

1. **用 AI 产品**
   - 跟 ChatGPT / Claude / DeepSeek 聊天，随便聊什么都行
   - 让它帮你写文案、总结文章、解释概念
   - 感受它擅长什么、不擅长什么

2. **看一个视频**
   - 🎬 **[Karpathy：Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g)**
   - 我们知识库里已经有[中文精讲版](karpathy-intro.md)，先读那个，再去看原视频

3. **玩 AI 绘图**
   - 试试通义万相、Midjourney、DALL-E
   - 感受描述词（prompt）对结果的影响

4. **跑一行代码（可选）**
   - 不需要编程基础，复制粘贴就能跑
   - 去 [Google Colab](https://colab.research.google.com/) 或 [python123.io](https://www.python123.io/)
   - 试试让 AI 生成一段代码，复制进去运行看看

### 检验标准

- 能用自己的话解释"什么是大语言模型"
- 知道 LLM 能做什么、不能做什么
- 对"幻觉"、"Prompt"、"Token"这几个词有直觉理解

---

## 阶段二：上手实践（动手才是王道）

**目标**：学会用 API 调用 LLM，解决实际问题。

### 前置知识

- 基本的 Python 语法（变量、函数、列表、字典）
- 如果不会：花 3~5 天快速过一遍 [Python 入门教程](https://www.liaoxuefeng.com/wiki/1016959663602400)

### 实践项目

#### 项目1：调用 API（1-2 天）

```python
# 找个 API Key，写几行代码调通
from openai import OpenAI
client = OpenAI()
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "讲个冷笑话"}]
)
print(response.choices[0].message.content)
```

#### 项目2：写个聊天脚本（2-3 天）
- 做一个带对话历史的命令行聊天
- 学会用 system prompt 控制助手行为

#### 项目3：总结网页内容（3-5 天）
- 用 `requests` 抓取网页
- 把内容发给 LLM 让 AI 总结
- 这其实就是最基础的 RAG

#### 项目4：用 AI 辅助编程（长期）
- 用 Claude Code / Cursor / Copilot
- 让 AI 帮你写代码、修 bug、解释代码
- 这是学编程效率最高的方式之一

### 在线课程推荐

| 课程 | 时长 | 说明 |
|------|------|------|
| [Andrew Ng - ChatGPT Prompt Engineering for Developers](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/) | ~1.5h | 最短路径理解 Prompt 工程 |
| [Hugging Face NLP Course](https://huggingface.co/learn/nlp-course) | ~10h | 实践导向，从 tokenizer 到 transformer |

### 检验标准

- 能用 Python 调通至少一个 LLM API
- 能写出好的 prompt，让模型稳定输出预期格式
- 理解 system prompt、temperature、max_tokens 的作用

---

## 阶段三：理论基础（知其所以然）

**目标**：理解 LLM 背后的核心原理。

### 学习路径

1. **Token 与分词**
   - 为什么 "hello" 是 1 个 token，"我是中国人" 是几个？
   - BPE 分词的基本思想

2. **词嵌入（Word Embedding）**
   - 把词映射成向量
   - "相似"的词在向量空间里距离近

3. **Transformer 架构**
   - 注意力机制（Attention）：为什么重要？
   - 多头注意力（Multi-Head Attention）
   - 位置编码
   - 推荐：**[3Blue1Brown 可视化讲解 Transformer](https://www.youtube.com/watch?v=wjZofJX0v4M)**
   - 进阶：**[Karpathy: Let's Build GPT](https://www.youtube.com/watch?v=kCc8FmEb1nY)** — 从零实现 GPT

4. **预训练与微调**
   - 预训练（Pre-training）：从互联网学知识
   - 微调（Fine-tuning）：学会做助手
   - RLHF：人类反馈强化学习

5. **模型评估**
   - 困惑度（Perplexity）
   - 基准测试（MMLU、HumanEval 等）

### 必读论文

| 论文 | 难度 | 说明 |
|------|------|------|
| [Attention Is All You Need](https://arxiv.org/abs/1706.03762) | ⭐⭐⭐ | Transformer 起源，值得看 |
| [BERT](https://arxiv.org/abs/1810.04805) | ⭐⭐ | 双向预训练 |
| [GPT-3](https://arxiv.org/abs/2005.14165) | ⭐⭐ | 大规模语言模型的涌现能力 |
| [InstructGPT](https://arxiv.org/abs/2203.02155) | ⭐⭐ | RLHF 怎么做的 |

### 检验标准

- 能画出 Transformer 的结构框图
- 能解释注意力机制的计算过程
- 能区分预训练和微调的作用
- **从知识库的[基础概念](基础概念/what-is-llm.md)部分开始，内容正好对应这个阶段**

---

## 阶段四：深入方向（选一条路走）

**目标**：根据自己的兴趣和方向深入。

### 方向 A：LLM 应用开发

- **RAG**：给 LLM 接入私有知识库 → 看知识库[应用实践/RAG](应用实践/rag.md)
- **Agent**：让 LLM 使用工具、自主完成任务 → 看[Agent 智能体](应用实践/agent.md)
- **LangChain** 框架学习（[官方教程](https://python.langchain.com/docs/tutorials/)，直接跳 RAG 和 Agent 章节）
- **Anthropic Cookbook**（[GitHub](https://github.com/anthropics/anthropic-cookbook)）— Claude API 实用代码示例
- **生产部署**：Prompt 管理、监控、评估

### 方向 B：模型训练与微调

- **LoRA / QLoRA**：高效微调方法
- **数据工程**：清洗、标注、质量评估
- **分布式训练**：DeepSpeed、FSDP
- **评估与对齐**：RLHF、DPO

### 方向 C：模型推理

- **vLLM / TensorRT-LLM**：高性能推理
- **量化**：INT4、INT8、GGUF
- **KV Cache 优化**
- **连续批处理（Continuous Batching）**

### 方向 D：AI 安全

- 红队测试（Red Teaming）
- 越狱与防御
- 幻觉检测

---

## 推荐学习顺序（精简版）

```
第 1 周：玩 AI 产品，读 Karpathy 精讲
第 2-3 周：学 Python 基础，调通 API
第 4-5 周：做 2-3 个小项目
第 6-8 周：学 Transformer / 注意力机制
第 9+ 周：选方向深入（RAG / Agent / 微调）
```

---

## 日常习惯

- **每周读 1 篇AI 相关文章**（机器之心、量子位、Lil'Log）
- **多用 AI 辅助工作学习**，不要为了学 AI 而学 AI，要用它解决实际问题
- **写笔记**，把你学到的用自己的话写下来（这就是在搭建知识库）
- **多实践少刷课**，看 10 小时视频不如自己跑通一个项目

---

*最后更新：2026-05-10*
