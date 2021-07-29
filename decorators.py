import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func. __name__ + " took " + str((end-start)*1000) + "mil sec")
        return result
    return wrapper

@time_it
def cal_square(numbers):
    results = []
    for number in numbers:
        results.append(number * number)
    end = time.time()
   
    return results

@time_it
def cal_quebe(numbers):
    results = []
    for number in numbers:
        results.append(number*number*number)
   
    return results        

array = range(1,10)
out_square = cal_square(array)
print("value of squre :",out_square)


out_quebe = cal_quebe(array)
print("value of quebe :",out_quebe)