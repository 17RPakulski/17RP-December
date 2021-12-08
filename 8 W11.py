
# Max of two numbers input by the user
def Max_two_numbers():
    n1 = int(input('Enter First Number: '))
    n2 = int(input('Enter Second Number: '))
    if n1 > n2:
        max_n = n1
    else:
        max_n = n2
    print('The max of', n1, 'and', n2, 'is', max_n)

#Max_two_numbers()
    
def Max_two_numbers_parameters(n1, n2):
    if n1 > n2:
        max_n = n1
    else:
        max_n = n2
        
    print('The max of', n1, 'and', n2, 'is', max_n)
    

#number1 = int(input('Enter First Number: '))
#number2 = int(input('Enter Second Number: '))

#Max_two_numbers_parameters(number1, number2)



# multiply two numbers input by the user

def multiply_two_numbers():
    number1 = int(input('Enter First Number: '))
    number2 = int(input('Enter Second Number: '))
    total = number1 * number2
    print('If', number1, 'and', number2, 'are multiplied, the answer is', total)


#multiply_two_numbers()




def multiply_two_numbers_parameters(number1, number2):
    total = number1 * number2
    print('If', number1, 'and', number2, 'are multiplied, the answer is', total)
    



number1 = int(input('Enter First Number: '))
number2 = int(input('Enter Second Number: '))
multiply_two_numbers_parameters()








