import time
import threading
import numpy as np
import random


class Person(threading.Thread):
    def _init_(self, name, delay, status, amount):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay
        self.status = status
        self.amount = amount

    def run(self):
        acc = 2000
        for i in range(10):
            saveOrWithdraw = random.randint(0,1)
            if saveOrWithdraw == 1:
                acc = acc + self.amount
                print(self.name + 'has saved: ' + self.amount + 'into bank account with balance: ' + acc)
                time.sleep(abs(self.delay))

            else:
                acc = acc - self.amount
                print(self.name + 'has withdrawn:' + self.amount + 'from bank account with balance:' + acc )
                time.sleep(abs(self.delay))


p1 = Person("Ron", 2, random.randint(0, 1), np.random.randint(40, 300))
p2 = Person('Draco', 1, random.randint(0, 1), np.random.randint(20, 100))
p3 = Person('Harry', 3, np.random.randint(0, 1), np.random.randint(10, 50))

# start thread
p1.start()
p2.start()
p3.start()
p1.join()
p2.join()
p3.join()


print('Exiting Thread...')