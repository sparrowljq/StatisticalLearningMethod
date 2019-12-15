# 使用JSON
import json
data = [1, 'ss', 'bb']
json_str = json.dumps(data)
print(json_str)
# dump()是将对象序列化为文件
with open('D:\\aa.txt', 'w') as f:
    json.dump(data, f)
# load()是将文件转换为json对象
with open('D:\\aa.txt', 'r') as f:
    print(json.load(f))
