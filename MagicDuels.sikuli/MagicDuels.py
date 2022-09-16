cont = "cont.png"
hoveron = "hoveron.png"
hand = "hand.png"
while True:
    if exists(cont):
        type(Key.ENTER)
    if exists(cont):
        type(Key.ENTER)
    hover(hoveron)
    if exists(hand):
        click(hand)
        type(Key.F3)
    if exists(cont):
        type(Key.ENTER)
    if exists(cont):
        type(Key.ENTER)
        