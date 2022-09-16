import time
import urllib2
import shutil
import os
import threading
screenshotsDir = "C:\\Screenshots\\"
scr_region = SCREEN
iterations = 0
lastArenaTime = time.time()
lastActivationTime = time.time()
setThrowException(False)
items = []
items.append(Pattern("1504639381350.png").similar(0.85).targetOffset(88,-1))
items.append(Pattern("1504639426253.png").similar(0.85).targetOffset(61,9))
items.append(Pattern("1504639476337.png").similar(0.85).targetOffset(-72,7))
items.append(Pattern("1504639541510.png").similar(0.85).targetOffset(77,-1))
items.append(Pattern("1504639742133.png").similar(0.85).targetOffset(65,0))
items.append(Pattern("1504639764464.png").similar(0.85).targetOffset(-67,6))
items.append(Pattern("1504639801260.png").similar(0.85).targetOffset(74,-1))
items.append(Pattern("1504639838441.png").similar(0.85).targetOffset(55,1))
items.append(Pattern("1504640901920.png").similar(0.85).targetOffset(52,0))
items.append(Pattern("1504639926752.png").similar(0.85).targetOffset(78,-1))
items.append(Pattern("1504640941969.png").similar(0.85).targetOffset(68,0))
items.append(Pattern("1504639966367.png").similar(0.85).targetOffset(87,-1))
items.append(Pattern("1504640973303.png").similar(0.85).targetOffset(83,-1))
items.append(Pattern("1504640004499.png").similar(0.85).targetOffset(62,1))
items.append(Pattern("1504640029153.png").similar(0.85).targetOffset(62,0))
#items.append(Pattern("1504640997361.png").similar(0.85).targetOffset(57,0))
#items.append(Pattern("1504640064173.png").similar(0.85).targetOffset(67,0))
items.append(Pattern("1504672417432.png").similar(0.85).targetOffset(58,-3))
items.append(Pattern("1504640088422.png").similar(0.85).targetOffset(68,0))
#Праздники
#items.append(Pattern("1504639696227.png").similar(0.85).targetOffset(-73,15))
items.append(Pattern("1504640355602.png").similar(0.85).targetOffset(62,0))
items.append(Pattern("1504640308457.png").similar(0.85).targetOffset(-67,6))
items.append(Pattern("1504640393904.png").similar(0.85).targetOffset(79,-1))
items.append(Pattern("1504640424157.png").similar(0.85).targetOffset(84,2))
items.append(Pattern("1504640451677.png").similar(0.85).targetOffset(-67,6))
items.append(Pattern("1504640474326.png").similar(0.85).targetOffset(-63,4))
items.append(Pattern("1504640489326.png").similar(0.85).targetOffset(62,0))
items.append(Pattern("1504640505484.png").similar(0.85).targetOffset(78,-3))
items.append(Pattern("1504640537319.png").similar(0.85).targetOffset(64,0))
items.append(Pattern("1504640569091.png").similar(0.85).targetOffset(75,0))
items.append(Pattern("1504640616926.png").similar(0.85).targetOffset(71,-5))
items.append(Pattern("1504640638976.png").similar(0.85).targetOffset(69,-1))
items.append(Pattern("1504640655347.png").similar(0.85).targetOffset(79,2))
items.append(Pattern("1504640680281.png").similar(0.85).targetOffset(81,-2))
items.append(Pattern("1504640695967.png").similar(0.85).targetOffset(68,0))
items.append(Pattern("1504640718384.png").similar(0.85).targetOffset(81,-2))
items.append(Pattern("1504640743165.png").similar(0.85).targetOffset(69,2))
items.append(Pattern("1504640780792.png").similar(0.85).targetOffset(53,0))
items.append(Pattern("1504640808432.png").similar(0.85).targetOffset(-10,8))
items.append(Pattern("1504640827775.png").similar(0.85).targetOffset(-75,7))
items.append(Pattern("1504640844530.png").similar(0.85).targetOffset(62,1))
pranaItems = []
#pranaItems.append(Pattern("1504640149712.png").similar(0.85).targetOffset(45,1))
#pranaItems.append(Pattern("1504640175437.png").similar(0.85).targetOffset(61,0))
#pranaItems.append(Pattern("1504640196598.png").similar(0.85).targetOffset(54,1))
#pranaItems.append(Pattern("1504640219745.png").similar(0.85).targetOffset(81,-1))
#pranaItems.append(Pattern("1504640238686.png").similar(0.85).targetOffset(88,2))
def CheckActivables():
    lastActivationTime = time.time()
    #shot = capture(scr_region)
    #timestamp = time.strftime("%Y-%m-%dT%H-%M-%S_")
    #shutil.move(shot, os.path.join(screenshotsDir+"stamp\\",timestamp+".png"))
    for i, val in enumerate(items):
        if exists(val):
            #img = capture(scr_region)
            #shutil.move(img, os.path.join(screenshotsDir,timestamp+".png"))
            click(val)
            wait(5)
    if exists(Pattern("1504592113772.png").similar(0.85)):
        for i, val in enumerate(pranaItems):
            if exists(val):
                click(val)
                break
#t = threading.Timer(300.0, CheckActivables)
#t.start
########################
while True:
    iterations += 1
    hover(Location(50,500)) #иначе нужные кнопки могут изменить вид
    click(Pattern("1504012910070.png").similar(0.95).targetOffset(27,2)) #если выбило на газету
    try:
        resp = urllib2.urlopen("https://time.akamai.com/?iso")
        now = time.strptime(resp.read(), "%Y-%m-%dT%H:%M:%SZ")
    except:
        print("TIME PARSING ERROR, CONTINUING...")
        now = time.strptime("1988-11-18T01:30:00", "%Y-%m-%dT%H:%M:%S")
        continue
    if ((now.tm_min < 2) and (now.tm_min >= 0)) or ((now.tm_min == 2) and (now.tm_sec < 30)):
        start = time.time()
        print("TIME triggered" + str(now.tm_min)+ ":" + str(now.tm_sec))
        if exists(Pattern("1502826958407.png").similar(0.80)):
            click(Pattern("1502826958407.png").similar(0.79))
            print("click-1")
            click(wait(Pattern("1502898689880.png").targetOffset(-46,1), 30))
            print("click-2")
            wait(3)
            click(wait(Pattern("1502898689880.png").targetOffset(-46,1), 30))
            print("click-3, elapsed: %d sec"%(int(time.time()-start)))
            iterations = 0
            lastArenaTime = time.time()
            wait(3)
    else:
        click(Pattern("1502898689880.png").targetOffset(35,5))
#    if exists(Pattern("1503134328288.png").similar(0.79)) and (exists(Pattern("1507005035594.png").similar(0.95)) or exists(Pattern("1507005801872.png").similar(0.95))):
#        try:
#            click(Pattern("1503134328288.png").similar(0.79))
#            wait(5)
#            click(Pattern("1502898689880.png").targetOffset(-46,1))
#            wait(5)
#            click(Pattern("1502898689880.png").targetOffset(-46,1))
#            wait(10)
#        except:               
#            continue
    if exists(Pattern("1503210366728.png").similar(0.89)):
        click(Pattern("1503210366728.png").similar(0.89))
        wait(240)
    #если давно не ходил на арену , то м.б. стоит обновить страницу
    if (time.time() - lastArenaTime) > 21600: #6*60*60 секунд
        type(Key.F5)
        wait(15)
        lastArenaTime = time.time()
    if (time.time() - lastActivationTime) > 300 and (now.tm_min > 3 and now.tm_min < 50):
        CheckActivables()

                                
