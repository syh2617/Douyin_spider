import json
import re

with open('b.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    results = re.findall('.*self.__pace_f.push\((.*?)\)</script>', content, re.S)
    # results2 = re.findall('<\/script>(.*?)<script>', content, re.S)

    a = results[0]
    a = a.replace('\\', '')
    a = a.replace('\"', '')

    b=a.split('rawAdData')
    b=b[1:]

    for i in range(len(b)):
        title=re.findall(',desc:(.*?),', b[i], re.S)[0]
        name=re.findall(',nickname:(.*?),', b[i], re.S)[0]
        time=re.findall(',createTime:(.*?),', b[i], re.S)[0]
        diggCount=re.findall(',diggCount:(.*?),', b[i], re.S)[0]




    file_path = "01.json"

    # 写入 JSON 数据到文件中（带美观的格式和UTF-8编码）
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(b, f, indent=4, ensure_ascii=False)

    # print(results)
    # print(len(results2))
