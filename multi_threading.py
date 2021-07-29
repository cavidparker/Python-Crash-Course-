import time
import threading

def cal_square(numbers):
    print("Claculate squre Number :")
    for number in numbers:
        time.sleep(0.2)
        print("squre :", number * number)

def cal_cube(numbers):
    print("Calculate cube number :")
    for number in numbers:
        time.sleep(0.2)
        print("cube :",  number * number * number)


array = [2,3,8,9]

t = time.time()

# Using multi threading
t1 = threading.Thread(target=cal_square, args=(array,))
t2 = threading.Thread(target=cal_cube, args=(array,))

t1.start()
t2.start()

print("done in :", time.time()-t)

