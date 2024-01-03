import requests
import json
from jsonpath_ng import jsonpath, parse
import os

# 1. 要爬取的URL
url = "https://api-hmugo-web.itheima.net/api/public/v1/home/swiperdata"

# 2. 使用requests访问服务器端，获取JSON数据
response = requests.get(url)
data = response.json()

# 3. 使用jsonpath解析JSON数据，获取所有key为image_src的值
jsonpath_expr = parse("$.data[*].image_src")
matches = [match.value for match in jsonpath_expr.find(data)]

# 4. 使用requests把所有图片下载并保存到本地
image_dir = "downloaded_images"
os.makedirs(image_dir, exist_ok=True)

for i, image_url in enumerate(matches):
    response = requests.get(image_url)
    if response.status_code == 200:
        image_filename = os.path.join(image_dir, f"image_{i}.jpg")
        with open(image_filename, 'wb') as image_file:
            image_file.write(response.content)
        print(f"Image {i + 1} downloaded and saved as {image_filename}")
    else:
        print(f"Failed to download image {i + 1} from {image_url}")

# 所有图片下载完成后，它们将保存在名为downloaded_images的文件夹中