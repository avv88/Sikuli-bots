import random
random.seed()
while True:
    t = random.randint(30, 50)
    wait(t)
    if exists (Pattern("1453005290212.png").similar(0.98).targetOffset(0,34)):
        try:
            dragDrop(Pattern("1453005290212.png").similar(0.98).targetOffset(0,34), Pattern("1451472664421.png").targetOffset(4,113))
            wait(1)
        except:
            continue
    if exists (Pattern("1449510795317.png").similar(0.88).targetOffset(-1,33)):
        try: 
            dragDrop(Pattern("1449510795317.png").similar(0.88).targetOffset(-1,33), Pattern("1451472664421.png").targetOffset(4,113))
            wait(1)
        except:
            continue
    if exists (Pattern("1449510720997.png").targetOffset(1,27)):
        try:
            dragDrop(Pattern("1449510720997.png").targetOffset(1,27),  Pattern("1451472664421.png").targetOffset(4,113))
            wait(1)
        except:
            continue
    if exists (Pattern("1449510720997.png").targetOffset(1,27)):
        try:
            dragDrop(Pattern("1449510720997.png").targetOffset(1,27),  Pattern("1451472664421.png").targetOffset(4,113))
            wait(1)
        except:
            continue
    if exists (Pattern("1453005879847.png").targetOffset(-3,34)):
        try:
            dragDrop(Pattern("1453005879847.png").targetOffset(-3,34),  Pattern("1451472664421.png").targetOffset(4,113))
            wait(1)
        except:
            continue
    if exists (Pattern("1453005340642.png").similar(0.98).targetOffset(0,37)):
        try:
            dragDrop(Pattern("1453005340642.png").similar(0.98).targetOffset(0,37), Pattern("1451472664421.png").targetOffset(4,113))
            wait(1)
        except:
            continue
    if exists (Pattern("1453005340642.png").similar(0.98).targetOffset(0,37)):
        try:
            dragDrop(Pattern("1453005340642.png").similar(0.98).targetOffset(0,37), Pattern("1451472664421.png").targetOffset(4,113))
            wait(1)
        except:
            continue
    if exists (Pattern("1453005340642.png").similar(0.98).targetOffset(0,37)):
        try:
            dragDrop(Pattern("1453005340642.png").similar(0.98).targetOffset(0,37), Pattern("1451472664421.png").targetOffset(4,113))
            wait(1)
        except:
            continue
    if exists ("1451586492778.png"):
        try:
            click("1451586492778.png") 
        except:
            continue
    if exists(Pattern("1466793085463.png").similar(0.95)):
        break