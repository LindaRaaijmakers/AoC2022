import string

#read file
with open("day3/puzzle_input.txt", "r") as file:
        packing_lst = file.readlines()


#part 1: finding overlapping item between compartments
first_compartment = [packing_backpacks[:int(len(packing_backpacks)/2)] for packing_backpacks in packing_lst]
second_compartment = [packing_backpacks[int(len(packing_backpacks)/2):] for packing_backpacks in packing_lst]
item_overlap = [list(set(list(first)).intersection(set(list(second))))[0] for first,second in zip(first_compartment, second_compartment)]
points = {l:n+1 for n,l in enumerate(string.ascii_letters)}
print(f'part 1: {sum([points[item] for item in item_overlap])}')


#part 2: finding batch item in elf group
groups_lst = [packing_lst[a:b] for a,b in list(zip(list(range(0,301,3)),list(range(0,301,3))[1:]))]
item_overlap = [list(set(item[0]).intersection(set(item[1])).intersection(set(item[2])))[0] for item in groups_lst]
print(f'part 2: {sum([points[item] for item in item_overlap])}')