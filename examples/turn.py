import pololu.pololu as pololu

if __name__ == '__main__':

    pR = pololu.Pololu(pololu.Pins(enable=11, direction=13, step=15))
    pL = pololu.Pololu(pololu.Pins(enable=29, direction=31, step=33))

    pL.speed = 16
    pL.stepsleft(400)
    pL.stepsright(400)

    pR.speed = 16
    pR.stepsleft(400)
    pR.stepsright(400)

    print "integer steps 200 = 360 dgs"

    pL.goto(200)
    pR.goto(200)
    pL.goto(0)
    pR.goto(0)

    # print "float means angle dgs"
    #
    # for i in range(9):
    #     p.goto(i*45.0)
    #     p.goto(0)
