import random
import sys

# w_filter = set()
workouts = [] # create workout from this empty list
difficulty = ["Low weight: 15-20 reps - ", "Medium weight: 10-14 reps - ", "Heavy weight: 4-8 reps - "]
chest = ["Flat dumbell benchpress", "Flat barbell benchpress", "Flat dumbbell fly","Incline dumbell benchpress", "Incline barbell benchpress", "Incline dumbbell fly" "Cable fly",
                "Dip Machine", "Machine chest press", "Seated peckdeck fly" ]
leg = ["Front squat", "Deadlift", "Leg press", "Barbell lunge" , "Hamstring machine", "Quad machine", "Power clean", "Hang clean", "Barbell squat", "Single-leg romanian deadlift", "Kettlebell Swing"]
back = ["Superman row", "T-bar row", "Deadlift", "Barbell row", "Single-arm dumbell row", "Stiff arm pulldown", "Wide-grip lat pulldown", "Close-grip lat pulldown", "Seated cable row", "Standing cable L-pulls", "Seated bicep curls" , "Hammer curls", "Cable curls"]
shoulder = ["Barbell overhead press", "Dumbell overhead press", "Standing cable press", "TYI", "Barbell facepull", "Cable facepull", "Barbell lateral raise", "Cable lateral raise", "Dumbbell bent-over lateral raise", "Arnold press"]
day_list = [chest,leg,back,shoulder]

# def generate_workout(n,target):
#     while len(w_filter) < n: #populate set with random, nonduplicate elements
#         w_filter.add(random.randint(0,len(target)-1))
#     for i, value in enumerate(w_filter): #populate list with corresponding elements
#         workouts.insert(i,target[value])
#     for i, workout in enumerate(workouts): #print workouts
#         print(i+1, '.', workout + ' - ' + random.choice(difficulty) + str(random.randint(3,6)) + ' SETS')
#     print(75*('='))
#     workouts.clear()
#     w_filter.clear()

#improved algorithm
def generate_workout(n,target):
    while len(workouts) < n:
        #generate current random workout from 'target' day
        current = random.choice(target)

        #if 'current' is not in the workout list
        if any(current != workout for workout in workouts) or len(workouts) == 0:
            workouts.append(current)
    
    #generate and print with random difficulty/set count
    for i, workout in enumerate(workouts):
        print(i+1, '. ' + workout  + ' - ' + random.choice(difficulty) + ' ' + str(random.randint(3,6)) + ' SETS')
    print(75*('='))

    workouts.clear()


#(main)
while True:
    print(" Select input:\n",25*('='))
    day_type = int((input("0. Terminate program \n1. Chest day\n2. Leg day\n3. Back day\n4. Shoulder day\nInput: ")))
    if day_type < 0 or day_type > len(day_list):
        print("Invalid input, try again.")
    elif day_type == 0:
        sys.exit(0)
    else:
        break

while True:
    print("\n What would you like to do?\n",25*('='))
    option = int(input("0. Terminate program. \n1. Display all possible workouts for current day.\n2. Generate random workout.\nInput: "))
    if option < 0 or option > 2:
        print("Invalid input, try again.")
    elif option == 0:
        break
    elif option == 1:
        for i, wkout in enumerate(day_list[day_type-1]):
            print(wkout)
        break
    elif option == 2: #rng workout branch
        print("\nMaximum workouts for target: ", len(day_list[day_type-1]))
        n = int(input("Input how many workouts today: "))
        while n > len(day_list[day_type-1]) or n <= 0:
            n = int(input("Invalid input, try again: "))
        print()
        print((25*('=')), "\n|| Today's RNG workout:||")
        print(75*('='))
        generate_workout(n,day_list[day_type-1])

        again = input("\nWould you like to reroll? (Y/N): ")
        if again.upper() == 'Y':
            print()
            print(75*('='))
            generate_workout(n,day_list[day_type-1])
        break
sys.exit(0)
