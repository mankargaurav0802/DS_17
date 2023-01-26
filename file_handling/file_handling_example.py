
file_handler = open("news.txt",'r',encoding="utf8")
data = file_handler.readlines()
print(data)
file_handler.close()