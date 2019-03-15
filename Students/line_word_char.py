def wordCount():
    lineCnt = 0
    wordCnt = 0
    charCnt = 0
    list = []

    file_name = raw_input("Enter the filename : ")

    with open(file_name) as fin:
        for line in fin:
            lineCnt += 1
            list = line.split(' ')
            wordCnt = wordCnt + len(list)
            for ch in line:
                charCnt += 1

    print lineCnt, "lines"
    print wordCnt, "words"
    print charCnt, "characters"

if __name__ == '__main__':
    wordCount()
