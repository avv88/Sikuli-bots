Debug.on(3)
import shutil
import time
import gc
noWin = Pattern("noWin.png").exact()
bars = []
bars.append(Pattern("1630004903732.png").similar(0.64))
s=Screen()
counter = 0
screen_counter = 0
while True:
    counter += 1
    type('p')
    wait(0.2)
    f=Finder(s.capture(s.getBounds()))
    f.findAll(bars[0])
    bar_count = 0
    while f.hasNext():
        f.next()
        bar_count += 1
    if bar_count > 2:
        wait(30)
        focusWindow = App.focusedWindow()
        regionImage = capture(focusWindow)
        shutil.move(regionImage, os.path.join(r'C:\Screenshots', time.strftime('%H-%M-%S')+'_1.png'))
        wait(1)
        focusWindow = App.focusedWindow()
        regionImage = capture(focusWindow)
        shutil.move(regionImage, os.path.join(r'C:\Screenshots', time.strftime('%H-%M-%S')+'_2.png'))
        wait(1)
        focusWindow = App.focusedWindow()
        regionImage = capture(focusWindow)
        shutil.move(regionImage, os.path.join(r'C:\Screenshots', time.strftime('%H-%M-%S')+'_3.png'))
        wait(1)
        focusWindow = App.focusedWindow()
        regionImage = capture(focusWindow)
        shutil.move(regionImage, os.path.join(r'C:\Screenshots', time.strftime('%H-%M-%S')+'_4.png'))
        wait(1)
        focusWindow = App.focusedWindow()
        regionImage = capture(focusWindow)
        shutil.move(regionImage, os.path.join(r'C:\Screenshots', time.strftime('%H-%M-%S')+'_5.png'))
    if counter > 200:
        counter = 0
        gc.collect()