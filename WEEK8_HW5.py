import threading
import time
import random
import numpy as np
from tkinter import *
from queue import Queue

window = Tk()
agents = []
simTime = 0
simEnd = 100
cusIndex = 0
appWidth = 600
appHeight = 500
m1 = 5
m2 = 1
v1 = 1
v2 = -1
l1 = 50
l2 = 50
fillColor = ['pink', 'blue', 'purple', 'green', 'yellow']

window.title("Week 8")
canvas = Canvas(window, width=appWidth, height=appHeight, bg="white")
canvas.grid(row=0, column=0)

def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0:
        return v
    return v / norm


class Agent(threading.Thread):  # User is a Thread
    IN_QUEUE = 0
    BEING_SERVED = 1
    DONE = 2

    def __init__(self, name, power, loc):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.loc = loc
        print('Agent ', self.name, ' created with power ', self.power)

    def run(self):
        global simTime, simEnd

        while simTime < simEnd:

            global agents
            finaldir = np.array((0, 0))
            for ag in agents:
                if ag.name == self.name:
                    continue

                if ag.power < self.power:
                    continue

                adir = ag.loc - self.loc
                finaldir = finaldir + adir

            finaldir = normalize(finaldir) * 3
            self.loc = self.loc + finaldir
            print('Agent ', self.name, ' with power ', self.power, ' moved with dir ', tuple(finaldir), ' to location ',
                  self.loc)
            time.sleep(1)


numAgents = 5
ag_disp = []
for i in range(numAgents):
    agent = Agent('Agent' + str(i), random.randint(0, 5), np.random.rand(2) * 50)
    agents.append(agent)
    agent.start()

# simulation loop
while simTime < simEnd:
    # increment simulation time
    simTime = simTime + 1
    time.sleep(2)
    for i in range(len(ag_disp)):
        canvas.move(ag_disp[i], agents[i].direction()[0], agents[i].direction()[1])
    window.update()

    window.mainloop()