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

    def __init__(self, pinsR, pinsL, pinsZ, diameter):
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

    def move(self, x, y):
        dx = x - self.x
        dy = y - self.y
        cL = 200.0 * (dx + dy) / (np.pi * self.dm)
        cR = 200.0 * (-dx + dy) / (np.pi * self.dm)
        maxspeed = 32.0
        if np.absolute(cL) >= np.absolute(cR):
            time = np.absolute(cL) / maxspeed
            cLspeed = int(maxspeed)
            cRspeed = int(np.absolute(cR) * maxspeed / np.absolute(cL))
        else:
            time = np.absolute(cR) / maxspeed
            cLspeed = int(np.absolute(cL) * maxspeed / np.absolute(cR))
            cRspeed = int(maxspeed)

        print(cL, cR, cLspeed, cRspeed)
        commandL = (self.pL, max(1,cLspeed), int(cL))
        commandR = (self.pR, max(1,cRspeed), int(-cR))  # Negative because counterclockwise
        self.p.map(run, [commandL, commandR])

        actcL = np.sign(cL) * cLspeed * time
        actcR = np.sign(cR) * cRspeed * time
        actdx = (actcL - actcR) * (np.pi * self.dm) / (200.0 * 2.0)
        actdy = (actcL + actcR) * (np.pi * self.dm) / (200.0 * 2.0)
        print(actcL, actcR, actdx, actdy)
        print(self.x, self.y)
        self.x += actdx
        self.y += actdy
        print(self.x, self.y)


    def stroke(self, x, y):
        self.move_down()
        self.move(x, y)
        self.move_up()

    def move_up(self):
        run((self.pZ, 32, 1600))
        self.z = 0

    def move_down(self):
        run((self.pZ, 32, -1600))
        self.z = 1


def draw_square(mc):
    mc.move_down()
    mc.move_up()
    mc.move(2,0)
    mc.stroke(2,1)
    mc.stroke(3,1)
    mc.stroke(3,0)
    mc.stroke(2,0)
    mc.move(0,0)

if __name__ == '__main__':

    mc = MotorController((17, 22, 27), (5, 13, 6), (25, 24, 23), 0.475)

    draw_square(mc)
