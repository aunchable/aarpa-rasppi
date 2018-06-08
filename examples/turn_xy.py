import pololu.pololu as pololu
import numpy as np
from multiprocessing import Pool


def run(tup):
    pol, speed, steps = tup
    pol.speed = speed
    if steps >= 0:
        pol.stepsleft(steps)
    else:
        pol.stepsright(-steps)


class MotorController():

    def __init__(pinsR, pinsL, pinsZ, diameter):
        self.x, self.y, self.z = 0, 0, 0
        pRe, pRd, pRs = pinsR
        pLe, pLd, pLs = pinsL
        pZe, pZd, pZs = pinsZ

        self.pR = pololu.Pololu(pololu.Pins(
            enable=pRe, direction=pRd, step=pRs))
        self.pL = pololu.Pololu(pololu.Pins(
            enable=pLe, direction=pLd, step=pLs))
        self.pZ = pololu.Pololu(pololu.Pins(
            enable=pZe, direction=pZd, step=pZs))

        self.p = Pool()
        self.dm = diameter

    def move(x, y):
        dx = x - self.x
        dy = y - self.y
        cL = 200 * (dx + dy) / (np.pi * self.dm)
        cR = 200 * (-dx + dy) / (np.pi * self.dm)
        commandL = (self.pL, cL / 10, cL)
        commandR = (self.pR, cR / 10, -cR)  # Negative because counterclockwise
        p.map(run, [commandL, commandR])
        self.x, self.y = x, y

    def stroke(x, y):
        run(self.pZ, 1, 10)
        self.z = 1
        self.move(x, y)
        run(self.pZ, 1, 0)
        self.z = 0


if __name__ == '__main__':

    mc = MotorController((17, 22, 27), (5, 13, 6), (25, 24, 23))

    mc.stroke(10, 10)
