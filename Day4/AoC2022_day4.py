#read file
with open("day4/puzzle_input.txt", "r") as file:
    assignment_lst = [line.strip() for line in file.readlines()]

#part 1: function to find overlapping assignments
def findFullOverlap(string):
    a,b=map(int,string.split(',')[0].split('-'))
    c,d=map(int,string.split(',')[1].split('-'))
    oneInTwo = (a>=c) & (b<=d)
    twoInOne = (c>=a) & (d<=b)
    return 1 if (oneInTwo|twoInOne) else 0

fullOverlap = [findFullOverlap(elem) for elem in assignment_lst]
print(f'part1: {sum(fullOverlap)}')

#part 2: function to find partial overlapping assignments
def findPartialOverlap(string):
    a,b=map(int,string.split(',')[0].split('-'))
    c,d=map(int,string.split(',')[1].split('-'))
    oneBeforeTwo = (b<c)
    oneAfterTwo = (a>d)
    return 0 if (oneBeforeTwo|oneAfterTwo) else 1

partialOverlap = [findPartialOverlap(elem) for elem in assignment_lst]
print(f'part2: {sum(partialOverlap)}')