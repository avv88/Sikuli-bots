wait(3)
img = "img.png"
while True:
    if not exists(img):
        wait(3)
        continue
    loc = Env.getMouseLocation()
    loc.x += 300
    click(loc)
    wait(1)
    loc.x -= 300
    click(loc)
    wait(1)