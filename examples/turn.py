import pololu.pololu as pololu

if __name__ == '__main__':

    pR = pololu.Pololu(pololu.Pins(enable=17, direction=22, step=27))
    pL = pololu.Pololu(pololu.Pins(enable=5, direction=13, step=6))

    pL.speed = 16
    pL.stepsleft(400)
    pL.stepsright(400)

    pR.speed = 16
    pR.stepsleft(400)
    pR.stepsright(400)

    print "integer steps 200 = 360 dgs"
