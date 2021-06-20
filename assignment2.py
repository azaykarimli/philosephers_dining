import threading
import random
import time

#inheriting threading class in Thread module
class Philosopher(threading.Thread):
    running = True  #used to check if everyone is finished eating

    def __init__(self, index):
        threading.Thread.__init__(self)
        self.index = index

        #initialize and start the threading

    def run(self):
        while(self.running):
            time.sleep(random.randint(0,5))
            self.dine()      
 
    def dine(self):			
        print ('Philosopher %s starts eating. '% self.index)
        time.sleep(random.randint(3,15))
        self.running = False
        print ('Philosopher %s finishes eating and leaves the restaurant.' % self.index)

def main():
   
    
     

    philosophers= [Philosopher(i) for i in range(5)]

    Philosopher.running = True
    for p in philosophers: p.start()
    time.sleep(75)
    Philosopher.running = False
    print ("Now we're finishing.")
 

if __name__ == "__main__":
    main()