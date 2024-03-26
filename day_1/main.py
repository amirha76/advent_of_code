# open 'text.txt' file 
with open('text.txt', 'r') as file:
    lines = file.readlines()


numbers = []

for line in lines:
    digits = ''
    for char in line:
        if char.isdigit():
            digits += char
    if len(digits) == 0:
        numbers.append(0)
    elif len(digits) == 1:
         numbers.append(int(digits) * 11)
    else:
        numbers.append(int(digits[0]+digits[-1]))   
    
    
sum = 0
for num in numbers:
    sum += num
    
print("the sum of all numbers is: ", sum)