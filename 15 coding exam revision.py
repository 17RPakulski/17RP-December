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

file_write.write(str(add_3))


file_write.close()
file_read = open("RobertChristmasTest2021.txt", "r")
for line in file_read:
    print(line)




# 4    WRONG

    
    











