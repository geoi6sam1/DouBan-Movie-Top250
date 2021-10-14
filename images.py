
import requests
import os
from lxml import etree

if not os.path.exists('./豆瓣电影Top250图片'):
        os.mkdir('./豆瓣电影Top250图片')

i = 0
page = 0

while i < 11:
    url = 'https://movie.douban.com/top250?start=' + str(page) + '&filter='
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51'}
    response = requests.get(url=url,headers=headers)
    response.encoding = 'utf-8'

    tree = etree.HTML(response.text)
    dy_list = tree.xpath('//ol[@class="grid_view"]/li')

    for li in dy_list:
        img_num = li.xpath('.//em/text()')[0]
        img_name = li.xpath('.//img/@alt')[0]
        img_src = li.xpath('.//img/@src')[0]

        img_data = requests.get(url=img_src,headers=headers).content
        img_title = img_num + '.' + img_name + '.jpg'
        img_path = './豆瓣电影Top250图片/' + img_title
        with open(img_path,'wb') as dy_img:
            dy_img.write(img_data)
            print(img_title,' 保存成功！')
    
    page = (i + 1)*25
    i += 1

print('\n豆瓣电影Top250图片全部下载完成！')

