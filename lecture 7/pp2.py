# waf to replace all occurances of "python" with "java" in practice.txt file

with open("practice.txt","r") as f:
    data=f.read()

new_data=data.replace("python","java")
print(new_data)

with open("practice.txt","w") as f:
    f.write(new_data)