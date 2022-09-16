img95 = Pattern("img95.png").similar(0.98)
while True:
    if exists(img95):
        break
    else:
        type(Key.SPACE)