import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.agent_toolkits import FileManagementToolkit

# 1. 设置你的 Google API Key
os.environ["GOOGLE_API_KEY"] = "AIzaSyAiAxpOR1YWWpy3yvSzXVGWtgJxpWbb8rc"

# 2. 初始化模型
llm = ChatGoogleGenerativeAI(model="models/gemini-3.1-flash-lite-preview")

# 3. 初始化文件操作工具包
# 设置 root_dir 为 D 盘，限制 AI 只能在 D 盘操作，防止它乱删系统文件
toolkit = FileManagementToolkit(root_dir="D:/")
tools = toolkit.get_tools()

# 4. 创建提示词模板
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个专业的电脑助手，你有权操作 D 盘的文件。如果用户要求创建或修改文件，请使用提供的工具。"),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

# 5. 构建 Agent
agent = create_tool_calling_agent(llm, tools, prompt)

# 6. 创建执行器 (Executor)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# 7. 运行 Agent
# 现在你可以直接下达指令，Agent 会自己判断使用哪个工具
try:
    response = agent_executor.invoke({
        "input": "请在 D 盘根目录下创建一个名为 hahah.txt 的文件，并在里面写入 'Hello, World!'"
    })
    print("\n执行结果:", response["output"])
except Exception as e:
    print(f"操作失败: {e}")