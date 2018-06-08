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
        commandL = (self.pL, cL / 4, cL)
        commandR = (self.pR, cR / 4, -cR)  # Negative because counterclockwise
        p.map(run, [commandL, commandR])
        self.x, self.y = x, y

    def stroke(x, y):
        self.move_down()
        self.move(x, y)
        self.move_up()

    def move_up():
        run(self.pZ, 32, 1000)
        self.z = 0

    def move_down():
        run(self.pZ, 32, -1000)
        self.z = 1


if __name__ == '__main__':

    mc = MotorController((17, 22, 27), (5, 13, 6), (25, 24, 23), 0.475)

    mc.move_up()
    mc.move(2,2)
    mc.stroke(4,3)
