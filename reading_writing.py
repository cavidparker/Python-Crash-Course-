
# for "w" is write and overwrite the file
# for "a" is append the file
f = open("/home/cavid/Desktop/Alienide/All_project/python/data/write_file.txt", "a")
f.write("\nhello, I am using Tensorflow library")
f.close()

#### Read the file

new_file = open("/home/cavid/Desktop/Alienide/All_project/python/data/new_file.txt", "r")
# print(new_file.read())


# for line in new_file:
#     print(line)
# new_file.close()

for line in new_file:
    token = line.split(' ')
    print(token)
