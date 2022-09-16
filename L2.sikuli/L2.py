mp = Pattern("mp.png").exact()
#mp = Pattern("mp.png").exact()
exp = Pattern("exp.png").exact()
buff = Pattern("buff.png").exact()
cb = Pattern("cb.png").similar(0.85)
dobuff = Pattern("dobuff.png").exact()
notdead = Pattern("notdead.png").exact()
while True:
    wait(1)
    if not exists(mp):
        type(Key.F5)
    if not exists(exp):
        type(Key.F6)
        wait(1)
        type(Key.F7)
    #if not exists(buff):
    #    if exists(notdead):
    #        hover(cb)
    #        click(dobuff)