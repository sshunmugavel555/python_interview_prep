from pathlib import Path


def cnt_words(fileName,wrd) -> int:

    fn=Path(fileName)
    wc=0
    try:
        data=fn.read_text(encoding='utf-8')
    except:
        pass
        #print(f"File {fileName} NOT found !! Please check ")
    else:
        wc=data.count(wrd)
        #wordL=data.split()
        #wc=len(wordL)
        return wc


#print(cnt_words("C:/Users/SShunmugavel/Downloads/Python_Crash_Course/Chap_01/alice.txt"))
path="C:/Users/SShunmugavel/Downloads/Python_Crash_Course/Chap_01/"
alice=path+'alice.txt'
moby=path+'moby_dick.txt'
women=path+'little_women.txt'
py=path+'python.txt'

fileList=[alice,moby,py,women]

for eachFile in fileList:
    print(f"{eachFile} --> {cnt_words(eachFile,'the')} words")

      