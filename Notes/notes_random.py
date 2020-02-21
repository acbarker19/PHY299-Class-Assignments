import random as r

print("Random")

# a psuedo-random number (PRN) in range(0, 1)
print("r.random() =", r.random())

# a PRN in range(-5, 5)
print("r.uniform(-5, 5) =", r.uniform(-5, 5))

# a random integer in range(-5, 5)
print("r.randint(-5, 5) =", r.randint(-5, 5))

# a PRN drawn from a normal distribution (mean, st dev)
print("r.normalvariate(10, 1) =", r.normalvariate(10, 1))

# a random selection from a given sequence (1 value)
vals = ["Luke", "Leia", "Han", "Chewbacca"]
print("r.choice(vals) =", r.choice(vals))
print("r.sample(vals,2) =", r.sample(vals,2))
print("r.shuffle(vals) =", r.shuffle(vals))

print("\r\nExample of Assigning Groups of 2 and 3")
students = list(range(16))
# randomize order
r.shuffle(students)
num = 1
while len(students) > 0:
    if len(students) % 3 == 0:
        group = students[:3]
        students = students[3:]
    else:
        group = students[:2]
        students = students[2:]
    print("Group {0}: {1}".format(num, group))
    num += 1
    
print("\r\nMonty Hall Problem")
switch_wins = 0
hold_wins = 0

N = 1000

for n in range(N + 1):
    possible_doors = [1, 2, 3]
    
    win = r.randint(1, 3)
    
    door_choice = r.randint(1, 3)
    
    while True:
        remove_choice = r.randint(1, 3)
        if remove_choice != door_choice and remove_choice != win:
            possible_doors.remove(remove_choice)
            break
        
    if n < N / 2:
        if door_choice == win:
            hold_wins += 1
    else:
        if door_choice != win:
            switch_wins += 1

print("Wins from holding: {}/{} ({}% of the time)\r\n" \
      "Wins from Switching: {}/{} ({}% of the time)".format(
      hold_wins, int(N / 2), 100 * hold_wins / (N / 2),
      switch_wins, int(N / 2), 100 * switch_wins / (N / 2)))