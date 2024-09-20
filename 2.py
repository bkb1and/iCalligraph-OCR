from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = 'x'
API_KEY = 'x'
SECRET_KEY = 'x'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取文件 """
def get_file_content(filePath):
    with open(filePath, "rb") as fp:
        return fp.read()

image = get_file_content('img/2.png')
# url = "https://www.x.com/sample.jpg"
# pdf_file = get_file_content('文件路径')

# 调用通用文字识别（高精度版）
res_image = client.basicAccurate(image)
# res_url = client.basicAccurateUrl(url)
# res_pdf = client.basicAccuratePdf(pdf_file)
print(res_image)
# print(res_url)
# print(res_pdf)

# 如果有可选参数
options = {}
options["detect_direction"] = "true"
options["probability"] = "true"
res_image = client.basicAccurate(image, options)
# res_url = client.basicAccurateUrl(url, options)
# res_pdf = client.basicAccuratePdf(pdf_file, options)   
print(res_image)
# print(res_url)
# print(res_pdf)   