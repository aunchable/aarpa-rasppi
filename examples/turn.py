import pololu.pololu as pololu
from multiprocessing import Pool

def run(pol, speed, steps):
    pol.speed = speed
    if steps >= 0:
        pol.stepsleft(steps)
    else:
        pol.stepsright(-steps)

if __name__ == '__main__':

    pR = pololu.Pololu(pololu.Pins(enable=17, direction=22, step=27))
    pL = pololu.Pololu(pololu.Pins(enable=5, direction=13, step=6))

    motors = [(pR,16,200), (pL,16,-200)]
    p = Pool()
    p.map(run, motors)

    # Left is clockwise, right is counterclockwise
    print "integer steps 200 = 360 dgs"
