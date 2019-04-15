def find_all():
    count = 0
    model = "dasdas"
    with open('sound_unknown.txt', 'r' ,encoding='utf-8') as f:
        for line in f:
            line = line.lower()
            if model in line:
                count += 1
                print(line)
                f = open("newtext.txt", 'wb')
                f.write(line)
                f.close()
        # print(model + '\t' + str(count))
if __name__ =='__main__':
    find_all()