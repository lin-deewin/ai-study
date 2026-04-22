1. 安装python
2. 安装SDK
```ps1
(New-Object Net.WebClient).DownloadFile("https://dl.google.com/dl/cloudsdk/channels/rapid/GoogleCloudSDKInstaller.exe", "$env:Temp\GoogleCloudSDKInstaller.exe")

& $env:Temp\GoogleCloudSDKInstaller.exe
```
3. 设置网络代理
```shell
gcloud components update
gcloud config unset auth/disable_ssl_validation  
```
vpn改为美国，并全局代理