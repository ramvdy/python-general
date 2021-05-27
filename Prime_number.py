#initializing empy list
list_prime = []

#declaring a variable with starting number 1
num = 1

while len(list_prime) < 10: #checking if we have lenght of list is less than 10

    #checking for 2,3,5
    if  num == 2 or num == 3 or num == 5:
        list_prime.append(num)

    #checking for other than 2,3,5
    elif num!=1 and num%2 != 0 and num%3!=0 and num%5!=0:
        list_prime.append(num)

    #increament that number every time till
    num += 1
print(list_prime)
