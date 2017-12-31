import requests

content = requests.get("https://www.pythonanywhere.com/user/marcelus/shares/ca138a4f2f864bb0a89ec2a330d86f6f/").content

content = str(content, "utf-8")

for i in content.split(" "):
    print(i)