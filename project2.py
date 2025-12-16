spring_points = 0
summer_points = 0
fall_points = 0
winter_points = 0

answer1 = input ("Do you prefer A short sleeves, B tanktops, C long sleeves, or D jackets?")
if answer1 == "A"  or answer1 == "a":
    spring_points += 1
elif answer1  == "B" or answer1 == "b":
    summer_points += 1
elif answer1 == "C" or answer1== "c" :
    fall_points += 1
elif answer1 == "D" or answer1 == "d" :
    winter_points += 1

answer2 = input ("Do you prefer A gardens, B beaches, C pumkinpatches, or D mountins?")
if answer2 == "A" or answer2 == "a" : 
    spring_points += 1
elif answer2 == "B" or answer2 == "b" :
    summer_points += 1
elif answer2 == "C" or answer2 == "c" :
    fall_points += 1
elif answer2 == "D" or answer2 == "d" :
    winter_points += 1

answer3 = input ("Do you prefer A track, B swimming, C volleyball, or D hockey?")
if answer3 == "A" or answer3 == "a" :
    spring_points += 1
elif answer3 == "B" or answer3 == "b" :
    summer_points += 1
elif answer3 == "C" or answer3 == "c" :
    fall_points += 1
elif answer3 == "D" or answer3  == "d" :
    winter_points += 1

answer4 = input ("Do you prefer A rain, B sun, C wind, or D snow?")
if answer4 == "A" or answer4 == "a" : 
    spring_points += 1
elif answer4 == "B" or answer4 == "b" :
    summer_points += 1
elif answer4 == "C" or answer4 == "c" :
    fall_points += 1
elif answer4 == "D" or answer4 == "d" :
    winter_points += 1

answer5 = input ("Do you prefer A pink, B yellow, C orange, or D blue?")
if answer5 == "A" or answer5 == "a" :
    spring_points += 1
elif answer5 == "B" or answer5 == "b" :
    summer_points += 1
elif answer5 == "C" or answer5 == "c" :
    fall_points += 1
elif answer5 == "D" or answer5 == "d" :
    winter_points += 1

if winter_points > summer_points and winter_points > spring_points and winter_points > fall_points: 
    print("You are a winter person!")
elif spring_points > summer_points and spring_points > fall_points and spring_points > winter_points:
    print("You are a spring person!")
elif fall_points > summer_points and fall_points > winter_points and fall_points > spring_points:
    print("You are a fall person!")
elif summer_points > fall_points and summer_points > winter_points and summer_points > spring_points:
    print("You are a summer person!")