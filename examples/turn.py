import pololu.pololu as pololu
from multiprocessing import Pool

def run(pol):
    pol.speed = 16
    pol.stepsleft(200)
    pol.stepsright(200)

if __name__ == '__main__':

    pR = pololu.Pololu(pololu.Pins(enable=17, direction=22, step=27))
    pL = pololu.Pololu(pololu.Pins(enable=5, direction=13, step=6))

    motors = [pR, pL]
    p = Pool()
    p.map(run, motors)

    print "integer steps 200 = 360 dgs"
