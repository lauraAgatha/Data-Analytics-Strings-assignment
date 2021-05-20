# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
scorerOne = "Ruud Gullit"
scorerTwo = "Marco van Basten"

goal_0 = 32
goal_1 = 54

scorers = scorerOne + ' ' + str(goal_0) + ', ' + scorerTwo + ' ' + str(goal_1)
print(scorers)

report = f"{scorerOne} scored in the {goal_0}nd minute\n" + scorerTwo + f" scored in the {goal_1}th minute"
print(report)

player = "Hans van Breukelen"
first_name = player[:player.find(" ")]

last_name_len = len(player[player.find(" ") + 1:])

name_short = player[0] + '. ' + player[player.find(" ") + 1:]

chant =  (first_name + '! ') * (len(first_name)-1) + (first_name + '!') 

good_chant = chant[-1] != ' '

print (first_name)
print(last_name_len)
print(name_short)
print(chant)
print(good_chant)
