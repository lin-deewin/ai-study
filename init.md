1. 安装python， node.js
2. 安装SDK
```ps1
(New-Object Net.WebClient).DownloadFile("https://dl.google.com/dl/cloudsdk/channels/rapid/GoogleCloudSDKInstaller.exe", "$env:Temp\GoogleCloudSDKInstaller.exe")

& $env:Temp\GoogleCloudSDKInstaller.exe
```
3. 设置网络代理
```shell
gcloud components update
npm install -g @google/generative-ai
gcloud config unset auth/disable_ssl_validation  
```
vpn改为美国，并全局代理

4. 
主模型请填：gemini-3.1-pro-preview。它最聪明，省着点用。
备用模型请填：gemini-3.1-flash-lite-preview。当 Pro 提示 429 (Too many requests) 时，切换到它继续工作。

5. contine
```yaml
name: Local Config
version: 1.0.0
schema: v1
models:
  # - name: DeepSeek-my
  #   provider: deepseek
  #   model: deepseek-chat
  #   apiKey: sk-354dd556f74944e0ad1254184469212b
  - name: Gemini-2.5-pro
    provider: gemini
    # model: models/gemini-3.1-flash-lite-preview
    model: models/gemini-2.5-pro
    apiKey: AIzaSyCC-aOd0YuiZHSEw-Fq1Tq2QUeIio-LSSk
# tabAutocompleteModel:
#   title: DeepSeek Chat
#   provider: deepseek
#   model: deepseek-chat
#   apiKey: sk-354dd556f74944e0ad1254184469212b
customCommands:
  - name: check
    prompt: 请检查这段代码的逻辑严谨性，并给出改进建议。

```