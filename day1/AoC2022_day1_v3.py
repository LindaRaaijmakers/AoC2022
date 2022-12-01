# read file
with open("day1/puzzle_input.txt", "r") as file:
    calorie_lst = file.read()

# getting total calories per elf
calorie_total = [sum(list(map(int, i.split("\n")))) for i in calorie_lst.split("\n\n")]

# part1: max calories
max(calorie_total)

# part2: sum top 3 max calories
sum(sorted(calorie_total, reverse=True)[:3])