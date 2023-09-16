start =int(input("enter the lower range:"))
end = int(input("enter the upper range"))
for number in range(start,end+1):
    if number>1:
        for divisor in range(2, int(number/2) +1):
            if number % divisor == 0:
                break
            else:
                print(number, "is a prime number")



