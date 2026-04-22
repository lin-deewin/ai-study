import os
import google.generativeai as genai
os.environ['HTTP_PROXY'] = 'http://127.0.0.1:7890'
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:7890'
# --- 配置区 ---
# 建议通过环境变量设置 API KEY，或者直接填入下方字符串
API_KEY = "AIzaSyAiAxpOR1YWWpy3yvSzXVGWtgJxpWbb8rc" 
MODEL_NAME = "models/gemini-3.1-flash-lite-preview" # 响应快，适合终端对话

def main():
    if not API_KEY or "你的" in API_KEY:
        print("错误: 请先在脚本中填入有效的 Gemini API Key。")
        return

    # 初始化配置
    genai.configure(api_key=API_KEY, transport='rest') # 强制使用 REST 协议通常更稳定
    
    # 设置模型
    model = genai.GenerativeModel(MODEL_NAME)
    # model = genai.GenerativeModel('gemini-1.5-flash')
    chat = model.start_chat(history=[])

    print(f"--- 已连接至 {MODEL_NAME} ---")
    print("输入 'exit' 或 'quit' 退出，输入 'clear' 清空对话历史。\n")

    while True:
        user_input = input("YOU > ").strip()
        if user_input.lower() in ['exit', 'quit']: break
        
        try:
            # 改为 stream=False，直接获取结果
            response = chat.send_message(user_input, stream=False)
            print(f"GEMINI > {response.text}\n")
            
        except Exception as e:
            print(f"\n发生详细错误: {e}")

if __name__ == "__main__":
    main()