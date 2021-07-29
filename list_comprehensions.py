number = []
for j in range(1,100):
    number.append(j)

# numbers = [0,1,2,3,4,5,6,7,8,9,10]
even = []

for i in number:
    if i%2 == 0:
        even.append(i)
print(even)


### List comprehennsions ####
a = [0,1,2,3,4,5,6,7,8,9,10]
evens = [k for k in a if k%2==0]
print(evens)

#### Add square ###
sqr_number = [k*k for k in a]
print(sqr_number)


### Unique Number ###
s = [0,1,2,3,4,5,6,7,8,9,10,2,10,2,0,1]
s = set(s)
print(s)
even = {i for i in s if i%2==0}
print("Unique Number even :", even)



