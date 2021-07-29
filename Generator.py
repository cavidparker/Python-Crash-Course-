def remote_control_next():
    yield "CNN"
    yield "ESPN"

itr = remote_control_next()
print(next(itr))
print(next(itr))



#### fibonachi
def fib():
    a = 0
    b = 1
    while True:
        yield a
        a,b = b, a+b

for i in fib():
    if i > 50:
        break
    print(i)        
