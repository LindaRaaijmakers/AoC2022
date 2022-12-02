#read file
with open("day2/puzzle_input.txt", "r") as file:
        strategy_lst = file.readlines()


#part 1: total points following the strategy

#create point dictionary
points_dict = {'A': 1, 'X': 1, 'B': 2, 'Y': 2, 'C': 3, 'Z': 3}
#                rock            paper           scissor

#loop through round to allocate points
points = 0
for round in strategy_lst:
    opponent, response = round.strip().split("\t")
    print(opponent, response)
    points_opponent = points_dict[opponent]
    points_resp = points_dict[response]
    print(points_opponent, points_resp)
    points+=points_resp
    if points_resp+2==points_opponent:
        points+=6
    elif points_resp==points_opponent+2:
        points+=0
    elif points_resp>points_opponent:
        points+=6
    elif points_resp==points_opponent:
        points+=3
    else:
        points+=0
    print(points)

print(points)

#part2: allocate points via winning/drawing/losing strategy

#create response dictionary
strategy_dict = {'X': {'A': 'C', 'B': 'A', 'C': 'B'} #lose
                 , 'Y': {'A': 'A', 'B': 'B', 'C': 'C'} # draw
                 , 'Z': {'A': 'B', 'B': 'C', 'C': 'A'}} # win

#create point dictionary
points_dict = {'A': 1, 'B': 2, 'C': 3}
#              rock    paper    scissor

#loop through strategy round to allocate points
points = 0
for round in strategy_lst:
    opponent, strategy = round.strip().split("\t")
    response = strategy_dict[strategy][opponent]
    points+=points_dict[response]
    if strategy=='Y':
        points+=3
    elif strategy=='Z':
        points+=6
    else:
        points+=0

print(points)
