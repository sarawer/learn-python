# search in the word "learning" exist in the fiel or not

def find_word(word):
    with open("practice.txt","r") as f:
        data=f.read()
        if(data.find(word)!=-1):
            print("found")
        else:
            print("not found")


find_word("java")

