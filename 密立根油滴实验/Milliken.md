# 密立根油滴实验
## 使用说明
1. 访问链接  https://github.com/tesseract-ocr/tesseract/releases/download/5.5.0/tesseract-ocr-w64-setup-5.5.0.20241111.exe  下载并安装tesseract-ocr
2. 配置环境变量，右键我的电脑->属性->高级系统设置->环境变量->系统变量->Path->编辑->新建变量值设置为 C:\Program Files\Tesseract-OCR (这个是OCR默认安装路径)
3. 安装pytesseract库 pip install pytesseract
4. 安装PIL库 pip install Pillow
5. 进入公式求值程序
6. 将图片放入指定文件夹，！！！！在程序中指定img_dir 
7. 运行程序
8. 程序会自动识别图片中的数字并计算平均值，并打印到控制台
9. 程序会自动保存所有图片的平均值到一个字典中，并打印到控制台

## 期待后续自动化更新