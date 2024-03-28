# cubes with red, green, blue colors
# hide a secret numbers of cubes of each color
# objective: figure out information about the number
"""
You play several games and record the information from each game (your puzzle input).
Each game is listed with its ID number (like the 11 in Game 11: ...) followed by a
semicolon-separated list of subsets of cubes that were revealed from the bag (like 3 red, 5 green, 4 blue).
""" 

"""
Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, 
and 14 blue cubes. What is the sum of the IDs of those games?
"""
import re 
from math import prod
def part_one(lines, cubes):
    print("====== Part One ======")
    vaild_game = [] # just valid games filled with the number of game 
    for line in lines:
        game = line.split(':')[0]
        sets = line.split(':')[1]
        subsets = sets.split(';')
        invalid_game = False
        for sub in subsets:
            s_sub = sub.split(',')
            data = {re.findall(r'\d+(.*)', item)[0].strip(): int(re.findall(r'\d+', item)[0]) for item in s_sub}
            for d in data.keys():
                if d in cubes.keys() and cubes[d] < data[d]:
                    invalid_game = True
                    break
            if invalid_game:
                break
        if not invalid_game:
            vaild_game.append(int(re.search(r'\d+', game).group()))
            
                
    print("The answer is: ", sum(vaild_game))


def part_two(lines):
    print("====== Part Two ======")
    ans = 0
    for line in lines:
        game_sets = line.split(':')[1]
        subset = game_sets.split(';')
        minimum_dict = {"red": 0, "green": 0, "blue": 0}
        for sub in subset:
            s_sub = sub.split(',')
            data = {re.findall(r'\d+(.*)', item)[0].strip(): int(re.findall(r'\d+', item)[0]) for item in s_sub}
            for item in data.keys():
                if data[item] > minimum_dict[item]:
                    minimum_dict[item] = data[item]
        ans += prod(minimum_dict.values())

    
    print("The answer is: ", ans)
    
if __name__ == "__main__":
    
    cubes = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    
    try:
        with open('input.txt', 'r') as f:
            lines = f.readlines()
    except:
        print("Unable to open the file.")

    part_one(lines, cubes)
    part_two(lines)