import pololu.pololu as pololu

if __name__ == '__main__':

    pR = pololu.Pololu(pololu.Pins(enable=17, direction=22, step=27))

    pR.speed = 4
    pR.stepsleft(40)
    pR.stepsright(40)

    print "integer steps 200 = 360 dgs"

    #pR.goto(200)
    # pR.goto(0)
    #
    # print "float means angle dgs"
    #
    # for i in range(9):
    #     p.goto(i*45.0)
    #     p.goto(0)
