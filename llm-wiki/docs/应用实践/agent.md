# Agent 智能体

## 什么是 Agent

Agent（智能体）是能够**自主感知环境、做出决策并执行行动**的 AI 系统。LLM 作为 Agent 的"大脑"，负责推理和规划。

## 核心能力

- **推理（Reasoning）**：拆解问题，制定计划
- **工具使用（Tool Use）**：调用 API、搜索网页、执行代码
- **记忆（Memory）**：记住之前的交互和结果
- **自我反思（Self-Reflection）**：从错误中学习，调整策略

## 常见框架

### ReAct（Reasoning + Acting）

交替进行推理和行动：

```
思考：我需要查找今天的天气
行动：调用 get_weather(location="北京")
观察：{ "temp": 25, "weather": "晴" }
思考：天气很好，建议用户出门
回答：今天北京天气晴朗，适合出门活动！
```

### Plan-and-Solve

先生成完整计划，再逐步执行。

### Multi-Agent

多个 Agent 协作，各自负责不同角色。

## 工具调用示例

```python
import json

def get_weather(city: str) -> str:
    """获取指定城市的天气"""
    # 调用天气 API ...
    return f"{city} 今天 25°C，晴"

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "获取天气信息",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string"}
                },
                "required": ["city"]
            }
        }
    }
]
```

## 主流 Agent 框架

| 框架 | 开发者 | 特点 |
|------|--------|------|
| LangChain | LangChain | 生态最丰富 |
| AutoGen | Microsoft | 多 Agent 对话 |
| CrewAI | CrewAI | 角色分工 |
| Claude Code | Anthropic | 终端 Agent |

## 应用场景

- 自动编程与代码审查
- 客户服务机器人
- 数据分析和报告生成
- 自动化工作流编排
- 个人助手
