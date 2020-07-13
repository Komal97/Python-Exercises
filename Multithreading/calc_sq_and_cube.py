import threading 
import time 

def calculate_square(arr):
    print('calculate square...')
    for num in arr:
        time.sleep(0.2)
        print(num*num)
    
def calculate_cube(arr):
    print('calculate cube...')
    for num in arr:
        time.sleep(0.2)
        print(num*num*num)

arr = [2, 3, 4, 5]

t = time.time()
t1 = threading.Thread(target = calculate_square, args = (arr,))
t2 = threading.Thread(target = calculate_cube, args = (arr,))
t1.start()
t2.start()
t1.join()
t2.join()
print("work done in ", time.time()-t)