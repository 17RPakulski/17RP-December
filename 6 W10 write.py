#Home computer directories:

#filew = open('write.txt', 'w')
#filewr = open('write.txt', 'w')

# frequency, mode, mean, median,range

'''
file10 = open('C:/Users/rober/Downloads/10Random.txt', 'r')
file100 = open('C:/Users/rober/Downloads/100Random.txt', 'r')
file10 = open('C:/Users/17RPakulski.ACC/Downloads/10Random (2).txt', 'r')
file100 = open('C:/Users/17RPakulski.ACC/Downloads/100Random (2).txt', 'r')
#ff30
file10 = open('C:/Users/17RPakulski.ACC/Downloads/10Random.txt','r')
file100 = open('C:/Users/17RPakulski.ACC/Downloads/100Random.txt','r')
'''
#vVariables
min_num = 99999999999999999999999999999999999999999999999999999
max_num = 0

# 10 Random
print('############################# 10 RANDOM #############################')

# Frequency      
file10 = open('C:/Users/17RPakulski.ACC/Downloads/10Random.txt', 'r')
mylist = []

for line in file10:
    for item in line.split():
        mylist.append(item)

list2 = mylist.copy()

for item in mylist:
    if list2.count(item) > 1:
        list2.remove(item)


print('--- Frequency =')
for item in list2:
    pass
    #print('     Frequency of', item, '=', mylist.count(item))
    #write_f = ('     Frequency of', item, '=', mylist.count(item))
    
    #filew.write(write_f)

print()
file10.close()


















# Range

file10 = open('C:/Users/17RPakulski.ACC/Downloads/10Random.txt', 'r')
for line in file10:
    for item in line.split():
        number = int(item)

        if(number < min_num):
            min_num = int(item)

        if(number > max_num):
            max_num = int(item)


rangee = max_num - min_num
print('--- Range =', rangee)
rangee = str(rangee)
filew = open('write.txt', 'w')
filew.write(rangee)
filew.close()
print()

file10.close()

















# Mean

file10 = open('C:/Users/17RPakulski.ACC/Downloads/10Random.txt', 'r')
add = 0
numbers = 0

for line in file10:
    for item in line.split():
        add = (add + int(item))
        numbers = numbers + 1

mean = (add / numbers)        
print('--- Mean =', mean)
print()

file10.close()
# Median

file10 = open('C:/Users/17RPakulski.ACC/Downloads/10Random.txt', 'r')
l = []
add_two_mid = 0

for line in file10:
    for item in line.split():
        l.append(item)
        l.sort()

len_list = len(l)
half_len = len_list // 2
''' Not too sure wha
if half_len % 2 != 0:
    half_len_minus = half_len - 1
    half_len_plus = half_len + 1
    add_two_mid = (l[int(half_len_minus)] + l[int(half_len_plus)]) / 2
    print('--- Median =', add_two_mid)
'''
#else: should be else but the code above is not working 
index_median = l[half_len]
print('--- Median =', index_median)
file10.close()

# Mode

file10 = open('C:/Users/17RPakulski.ACC/Downloads/10Random.txt', 'r')
mode = 0
item_count = 0
'''
for line in file10:
    for item in line.split():
        item_count = item.count(item)
        if item_count > mode:
            mode = item
print('--- Mode =', mode)
'''



# print filew
filewr = open('write.txt', 'r')
for line in filewr:
    print('fileeeeee')
    print(line)
    
filew.close()