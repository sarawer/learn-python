# Two types of files:
# 1.Text files: .txt, .docx , .log
# 2.inary files: .mp4, .mov, .png, .jpeg



# read
f=open("C:\\Users\\Md.Sarawer Bhuiyan\\Desktop\\sarawer\\learn-python\\lecture 7\\demo.txt","r")
data=f.read()
print(data)
print(type(data))

line1=f.readline()
print(line1) #it will output a empty line.cz file was read before

line2=f.readline()
print(line2) #it will also output a empty line. but if file wasnt read before then it would print 2nd line


# overwrite
f=open("C:\\Users\\Md.Sarawer Bhuiyan\\Desktop\\sarawer\\learn-python\\lecture 7\\demo.txt","w")

f.write("I want to learn JavaScript tomorrow.")

#append
f=open("C:\\Users\\Md.Sarawer Bhuiyan\\Desktop\\sarawer\\learn-python\\lecture 7\\demo.txt","a")

f.write("Then i will move to reactJS")
f.write("\nAfter that NodeJS.")


# r+ -> read+overwrite (pointer point start)- no truncate

# w+ -> read+overwrite - truncate

# a+ -> read+append (pointer point end)- no truncate