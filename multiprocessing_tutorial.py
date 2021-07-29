import time
import multiprocessing

def cal_squre(numbers):
    print("calculating squre...........")
    time.sleep(5)
    for number in numbers:
        print("calculate squre :", number * number)


def cal_cube(numbers):
    print("calculating cube...............")
    for number in numbers:
        print("calculate cube :", number*number*number)



if __name__ == '__main__':
    array = [2,3,8,9]
    t = time.time()
    p1 = multiprocessing.Process(target=cal_squre, args=(array,))
    p2 = multiprocessing.Process(target=cal_cube, args=(array,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("End process :", time.time()-t)      