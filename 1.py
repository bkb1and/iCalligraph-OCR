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

# 调用通用文字识别（标准版）
res_image = client.basicGeneral(image)
# res_url = client.basicGeneralUrl(url)
# res_pdf = client.basicGeneralPdf(pdf_file)
print(res_image)
# print(res_url)
# print(res_pdf)

# 如果有可选参数
options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "true"
res_image = client.basicGeneral(image, options)
# res_url = client.basicGeneralUrl(url, options)
# res_pdf = client.basicGeneralPdf(pdf_file, options)
print(res_image)
# print(res_url)
# print(res_pdf)
