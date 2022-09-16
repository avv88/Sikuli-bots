orbitImg = Pattern("orbitImg.png").similar(0.85)
warpImg = Pattern("warpimg.png").similar(0.84)
confirmImg = Pattern("confirmImg.png").similar(0.85)
hoveron = Pattern("hoveron.png").similar(0.85)
lastWarp = time.time()
click(hoveron)
while True:
    wait(60)
    if (time.time() - lastWarp) > 11000:
        lastWarp = time.time();
        click(hoveron)
        type(Key.F12)
        click(orbitImg)
        wait(10)
        click(warpImg)
        wait(10)
        click(confirmImg)
        wait(10)
        click(warpImg)
        wait(10)
        hover(hoveron)
        wait(60*60)
         