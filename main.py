# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
scorerOne = "Ruud Gullit"
scorerTwo = "Marco van Basten"

goal_1 = 32
goal_2 = 54

scorers = scorerOne + str(goal_1) + ', ' + scorerTwo + str(goal_2)
print(scorers)

report = scorerOne + f" scored in the {goal_1}nd minute \n" + scorerTwo + f" scored in the {goal_2}th minute"
print(report)

player = "Hans van Breukelen"
first_name = player[player.find("Hans"):4]
last_name_len = player[player.find("van Breukelen"): len(player)]
name_short = player[0] + '. ' + last_name_len
chant =  first_name + '! ' + first_name + '! ' + first_name + '!'   #(first_name + '!') * 3
if (chant[len(chant)-1] != " "):
    good_chant = chant



print (first_name)
print(last_name_len)
print(name_short)
print(chant)
print(good_chant)