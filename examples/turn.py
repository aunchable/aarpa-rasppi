import pololu.pololu as pololu
from multiprocessing import Pool

def run(tup):
    pol, speed, steps = tup
    pol.speed = speed
    if steps >= 0:
        pol.stepsleft(steps)
    else:
        pol.stepsright(-steps)

if __name__ == '__main__':

    pR = pololu.Pololu(pololu.Pins(enable=17, direction=22, step=27))
    pL = pololu.Pololu(pololu.Pins(enable=5, direction=13, step=6))
    pZ = pololu.Pololu(pololu.Pins(enable=25, direction=24, step=23))


    p = Pool()

    motors = [(pR,16,200), (pL,16,-200)]
    p.map(run, motors)

    motors = [(pR,16,-200), (pL,16,200)]
    p.map(run, motors)

    run((pZ,16,200))
    run((pZ,16,-200))

    # Left is clockwise, right is counterclockwise
    print "integer steps 200 = 360 dgs"
