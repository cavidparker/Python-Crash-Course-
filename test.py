# import sys
# x = int(sys.argv[1])
# y = int(sys.argv[2])
# z = x + y 
# print(z)



## IF Startement
# x = 3
# r = x%2

# if r==0:
#     print("Even")
#     if x>5:
#         print("Great Number")
#     else:
#         print("Not great")    
# else:
#     print("odd")    

# print("Bye")



## While Loop
# i = 1
# while i<=5:
#     print("hello ", end = "")
#     j = 1
#     while j<=4:
#         print("python ", end = "")
#         j = j+1
#     i = i+1
#     print()


# x = int(input("How many candy do you have ?"))
# i = 1
# available_candy = 5
# while i <= x:   
#     if i>available_candy:
#         print("out of stocks")
#         break    
#     print("candy")
#     i+=1



# for i in range(20):
#     if i%3 == 0 or i%5 == 0:
#         continue
#     print(i)



# for i in range(20):
#     if i%2 != 0:
#         pass
#     else:
#         print(i)



## For Loop
# for i in range(1,21):
#     if i%5 !=0: 
#         print(i)


## Print pattern

# for j in range(4):
#     for i in range(4):
#         print("#", end="")
#     print()

# for i in range(4):
#     for j in range(4-i):
#         print('#', end='')
#     print()    


## OOP

# class Computer:
#     def config(self):
#         print("i7", "16GB", "1TB")

# comp1 = Computer()
# Computer.config(comp1)


# LIst DIctionary
# pizza = {
#     'crust': 'thick',
#     'toppings': ['musrooms', 'extra cheese'],
# }
# print("you order " + pizza['crust'] + " pizza")

# for topping in pizza['toppings']:
#     print(topping)

favorite_language = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

# for name, languages in favorite_language.items():
#     print(name.title())

for name, languages in favorite_language.items():
    print("\n" + name.title() + "'s favorite languages are:")