from multiprocessing import Pool
import time

def cal_squre(number):
    sum = 0
    for x in range(1000):
        sum += x*x
    return sum


if __name__ == '__main__':
    t1 = time.time()
    p = Pool()
    result = p.map(cal_squre, range(100000))
    p.close()
    p.join()
    print("Pool took :", time.time()-t1)

    t2 = time.time()
    result = []
    for x in range(100000):
        result.append(cal_squre(x))
    print("Serial process took :", time.time()-t2)    
            