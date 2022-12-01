#read file
with open("day1/puzzle_input.txt", "r") as file:
        calorie_lst = file.read().splitlines()


#getting total calories per elf
calorie_total = []
elf_total = 0
for i in calorie_lst:
    if i != "":
        elf_total += int(i)
    else:
        calorie_total.append(elf_total)
        elf_total = 0
        print(elf_total)


#max calories
max(calorie_total)


#sum top 3 max calories
sum(sorted(calorie_total, reverse=True)[:3])