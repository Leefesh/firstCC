# RAG 检索增强生成

## 什么是 RAG

**RAG（Retrieval-Augmented Generation）** 是一种将信息检索与 LLM 结合的技术架构。模型在生成回答前，先从外部知识库中检索相关文档，再基于检索结果生成答案。

## 为什么需要 RAG

LLM 的固有限制：

- 知识截止于训练数据日期
- 无法获取私有/实时信息
- 可能产生幻觉
- 长上下文成本高

RAG 解决这些问题：**让模型先查资料再回答**。

## 基本流程

```
用户提问
    ↓
向量化用户问题 → 在知识库中检索相似文档
    ↓
将检索结果 + 原始问题 拼入 Prompt
    ↓
LLM 生成带引用的回答
```

## 核心组件

### 1. 向量数据库（Vector DB）

存储文档的向量表示，支持相似度检索。

常用：Chroma、Pinecone、Weaviate、Milvus、Qdrant

### 2. 嵌入模型（Embedding Model）

将文本转换为向量。

常用：OpenAI Embeddings、BGE、E5、text2vec

### 3. 文档切分（Chunking）

将长文档切成合适大小的片段，需要平衡粒度与上下文。

## 实现示例

```python
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI

# 1. 加载文档并切分
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_splitter.split_documents(raw_documents)

# 2. 构建向量库
vectordb = Chroma.from_documents(docs, OpenAIEmbeddings())

# 3. 创建 RAG 链
qa = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model="gpt-4o"),
    retriever=vectordb.as_retriever()
)

# 4. 提问
answer = qa.invoke("你的问题")
```

## 进阶优化

- **Hybrid Search**：向量检索 + 关键词检索（BM25）融合
- **Reranking**：对检索结果重排序，提高准确率
- **Query Rewriting**：改写用户问题以改善检索效果
- **Multi-Hop RAG**：多轮检索，逐步深入
