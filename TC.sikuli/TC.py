TW = Pattern("TW.png").similar(0.87)
Y = Pattern("Y.png").similar(0.86)
SNT = "SNT.png"
iter = 0
while True:
    wait(5)
    type("GFDSA07CH ")
    iter += 1
    if iter > 310:
        iter = 0
        click(TW)
        wait(3)
        click(Y)
        wait(5)
        click(SNT)
        wait(5)
        type("HGFDSA")
        wait(3)
        type("HGFDSA")
        wait(3)
        type("HGFDSA")
        wait(3)
        type("HGFDSA")
        wait(3)
        type("HGFDSA")
        wait(3)
        type("HGFDSA")
        type("QWE")
        