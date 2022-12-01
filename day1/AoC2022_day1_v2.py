#second try using itertools
import itertools as it

# read file
with open("day1/puzzle_input.txt", "r") as file:
    calorie_lst = file.read().splitlines()

# getting total calories per elf
calorie_total = [sum(map(int, j)) for i, j in it.groupby(calorie_lst, lambda x: x == '') if not i]

# part1: max calories
max(calorie_total)

# part2: sum top 3 max calories
sum(sorted(calorie_total, reverse=True)[:3])
