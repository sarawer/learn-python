#find in which line of the file does the word "learning" occure first.print -1if not found


def chk_line(str): 
    word=str   
    line_count=1
    data=True
    with open("practice.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line_count)
                return
            else:
                line_count+=1
    print(-1)

chk_line("sara")

