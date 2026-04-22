import google.generativeai as genai
import os

# 确保代理生效
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:7890'
genai.configure(api_key="AIzaSyAiAxpOR1YWWpy3yvSzXVGWtgJxpWbb8rc")

print("--- 正在拉取你的可用模型清单 ---")
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            # 这里的 m.name 就是你脚本里唯一能填的正确字符串
            print(f"可用模型 ID: {m.name}")
except Exception as e:
    print(f"查询失败: {e}")