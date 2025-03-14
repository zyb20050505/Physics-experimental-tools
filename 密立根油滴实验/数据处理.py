'''
物理学实验数据处理--用于根据图片中的数字计算平均值--源自密立根油滴实验数据处理
作者信息：周诣博  有好的想法欢迎联系我 18015725598
开源协议：MIT License
去给我点个star吧(●'◡'●) https://github.com/zyb20050505

使用方法：
0.0 访问链接  https://github.com/tesseract-ocr/tesseract/releases/download/5.5.0/tesseract-ocr-w64-setup-5.5.0.20241111.exe  下载并安装tesseract-ocr
0.1 配置环境变量，右键我的电脑->属性->高级系统设置->环境变量->系统变量->Path->编辑->新建变量值设置为 C:\Program Files\Tesseract-OCR (这个是OCR默认安装路径)
0.2 安装pytesseract库 pip install pytesseract
0.3 安装PIL库 pip install Pillow
1. 将图片放入指定文件夹，！！！！在程序中指定img_dir
2. 运行程序
3. 程序会自动识别图片中的数字并计算平均值，并打印到控制台
4. 程序会自动保存所有图片的平均值到一个字典中，并打印到控制台
'''



from PIL import Image
import pytesseract
import re
import os


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def process_image(img_path):
    img = Image.open(img_path)
    # 转换为灰度图提高识别率
    img = img.convert('L')
    return img


# 提取数字并计算平均值
def calculate_average(img_path):
    img = process_image(img_path)
    text = pytesseract.image_to_string(img)

    numbers = re.findall(r'\b\d+\.\d{2}\b', text)

    if len(numbers) != 5:
        raise ValueError(f"识别到{len(numbers)}个数字，需要5个两位小数")

    numbers = [float(n) for n in numbers]
    print(numbers)
    average = sum(numbers) / 5
    return round(average, 2)

if __name__ == "__main__":
    img_dir = r'G:\pyPrograms\物理学实验\密立根油滴实验\pics'
    all_avgs = []

    for filename in os.listdir(img_dir):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            try:
                img_path = os.path.join(img_dir, filename)
                avg = calculate_average(img_path)
                print(f"{filename} 平均值：{avg:.4f}")
                all_avgs.append(avg)
            except Exception as e:
                print(f"{filename} 错误：{str(e)}")

    if all_avgs:
        print("------------所有平均值-----------")
        avg_dict = {filename: avg for filename, avg in zip(os.listdir(img_dir), all_avgs)}
        # 打印字典，按照文件名首字母大小排序
        for filename in sorted(avg_dict.keys()):
            print(f"{filename} 平均值：{avg_dict[filename]:.4f}")
    else:
        print("没有识别到有效图片")
