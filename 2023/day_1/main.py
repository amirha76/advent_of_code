def first_problem(lines):
    sum = 0 
    for line in lines:
        numbers = []
        for char in line:
            if char.isdigit():
                numbers.append(char)
            
        combined = ""
        combined += numbers[0]
        combined += numbers[len(numbers) - 1]
        sum += int(combined) 

    print("=========== Part One ===========")
    print("The answer: ", sum)
    
def second_problem(lines):
    mapped_data = {"one": '1', 
                  "two": '2',
                  "three": '3',
                  "four": '4',
                  "five": '5',
                  "six": '6',
                  "seven": '7',
                  "eight": '8',
                  "nine": '9'}
    sum = 0
    for line in lines:
        numbers = []
        for i in range(len(line)):
            if line[i].isdigit():
                numbers.append(line[i])
            for k in range(1, len(line)):
                temp = line[i:k]
                if temp in mapped_data:
                    numbers.append(mapped_data[temp])
                    break
        combined = ""
        combined += numbers[0]
        combined += numbers[len(numbers) - 1]
        sum += int(combined)
        
    print("=========== Part Two ===========")
    print("The answer: ", sum)
    
    
    
if __name__ == '__main__':
    
    # open 'input.txt' file 
    try: 
        with open('input.txt', 'r') as file:
            lines = file.readlines()
    except:
        print("Unable to open the file.")
        
    
    first_problem(lines)
    second_problem(lines)