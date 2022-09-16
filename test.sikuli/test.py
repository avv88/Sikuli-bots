from datetime import datetime
names = ['Arena', 'Capture', 'Kerrat']
indx = -1
while True:
    indx += 1
    if indx > 2 :
        break
    with open("C:\\Users\\Jet\\Desktop\\DailyLog.txt", "a") as myfile:
        myfile.write(str(datetime.now())[:-10]+" "+names[indx]+" taken.\n")
        myfile.close()