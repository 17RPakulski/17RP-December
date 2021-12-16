#file_write = open("RobertChristmasTest2021.txt", "w")
#file_read = open("RobertChristmasTest2021.txt", "r")
file_write = open("RobertChristmasTest2021.txt", "w")
given_list = [23,1,0,-12,48]


# 1 
add_1 = 0
for item in given_list:
    add_1 += item

file_write.write(str(add_1) +'\n')



# 2
add_2 = 0
for item in given_list:
    if item % 2 != 0:
        add_2 += item
    
file_write.write(str(add_2) +'\n')



# 3
add_3 = 0
for item in given_list:
    if item % 2 == 0:
        add_3 += 1

file_write.write(str(add_3) + '\n')

file_read = open("RobertChristmasTest2021.txt", "r")
for line in file_read:
    print(line)




# 4  
multiply = 1
for item in given_list:
    multiply = multiply * item

file_write.write(str(multiply) + '\n')




# 5
for i in range(0,21,4):
    file_write.write(str(i) + ' ')




'''
print('gap')
file_write.close()
for line in file_read:
    print(line)
'''











# While loop
print('while loop start')


# 6
counter = 0
input_string = 'cat'
length_of_string = (len((input_string)))

while counter < length_of_string:
        print(input_string[counter])
        counter += 1











