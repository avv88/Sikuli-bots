import random
random.seed()
while True:
    t = random.randint(30, 50)
    wait(t)
    if exists (Pattern("1451488521725.png").targetOffset(0,34)):
        try:
            dragDrop(Pattern("1451488521725.png").targetOffset(0,34), Pattern("1451472664421.png").targetOffset(4,113))
            wait(1)
        except:
            continue
    if exists (Pattern("1451472884566.png").exact().targetOffset(-1,35)):
        try:
            dragDrop(Pattern("1451472884566.png").exact().targetOffset(-1,35), Pattern("1451472664421.png").targetOffset(4,113))
            wait(1)
        except:
            continue
    if exists (Pattern("1449510795317.png").similar(0.88).targetOffset(-1,33)):
        try: 
            dragDrop(Pattern("1449510795317.png").similar(0.88).targetOffset(-1,33), Pattern("1451472664421.png").targetOffset(4,113))
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
    if exists (Pattern("1451472762710.png").exact().targetOffset(-1,37)):
        try:
            dragDrop(Pattern("1451472762710.png").exact().targetOffset(-1,37), Pattern("1451472664421.png").targetOffset(4,113))
            wait(1)
        except:
            continue
    if exists (Pattern("1451472762710.png").exact().targetOffset(-1,37)):
        try:
            dragDrop(Pattern("1451472762710.png").exact().targetOffset(-1,37), Pattern("1451472664421.png").targetOffset(4,113))
            wait(1)
        except:
            continue
    if exists (Pattern("1451472762710.png").exact().targetOffset(-1,37)):
        try:
            dragDrop(Pattern("1451472762710.png").exact().targetOffset(-1,37), Pattern("1451472664421.png").targetOffset(4,113))
            wait(1)
        except:
            continue
    if exists ("1451586492778.png"):
        try:
            click("1451586492778.png") 
        except:
            continue
    if exists(Pattern("1449510197368.png").exact()):
        break