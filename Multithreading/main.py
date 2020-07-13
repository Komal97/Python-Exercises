from threading import Thread
from time import sleep

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)


class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)


# run in sequence because of calling sequence, executed by main thread
# t1 = Hello()
# t2 = Hi()
# t1.run()
# t2.run()

# now we want to run both methods simultaneously/parallel
t1 = Hello()
t2 = Hi()
t1.start()
# to avoid collision between 2 threads
sleep(0.2)          
t2.start()

t1.join()
t2.join()
print("Bye")