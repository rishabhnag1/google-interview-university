# Strings
print('dicks')

print(r'C:\Bucky\Desktop\nudePics')

firstName = 'Bucky '

print(firstName + 'Roberts')

# Splicing Strings
user = 'Dicks'
print(user[0], user[4])
print(user[-3], user[2:4])

print(len(user))

# Lists

players = [24, 56, 45, 56, 7, 845, 24, 6, 78, 45, 6]

players[5] = 4

players.append(34)

# Ifs

if len(user) is 5:
    print()
elif len(user) is 4:
    print()

# Fors

food = ['sfd', 'sdf', 'dfg', 'fgh']

for f in food:
    print(f)
    print(len(f))

for f in food[:2]:
    print(f)

# Range
for x in range(5, 12, 2):
    print(x)

# While

bucky = 5
while bucky < 10:
    print(bucky)
    bucky += 1

# Comments
'''
for f in food[:2]:
    print(f)
'''

# Breaks and Continue
numbersTaken = [45, 46, 57, 23, 45, 56]

for n in range(1,60):
    if n in numbersTaken:
        continue # skips rest of loop, and go to next iteration
    print(n)

# Functions


def beef():

    print('dicks')
    return 3 + 4

bucky = beef()
print(bucky)


def beef3(type='Angus'):
    if type is 'dick':
        beef()

# Keyword Arguments


def dumb_sent(name='bucky', action='sucked', item='dick'):
    print(name, action, item)

dumb_sent()
dumb_sent("Sally", "farts", "cumbubbles")
dumb_sent(item='pussy')

#Flexible arguments

def add_num(*args):
    total = 0
    for a in args:
        total += a
    print(total)

add_num(3,4,5,5,5,6,6)

#Unpacking args

def health_calc(age, apples, cigs):
    answer = (100 - age) + (apples * 3.5) - (cigs * 2)
    print(answer)

bucky = [23,45,0]

health_calc(*bucky) #passes each item in

#Sets
groceries = {'cereal', 'milk', 'starcrunch', 'beer', 'ducktape', 'beer'} # no duplicates
print(groceries)

if 'milk' in groceries:
    print('got it')
else:
    print('need it')

#Dictionary
classmates = {"Tony": ' cool', "Emma": ' sits on my face', 'Lucy' : ' tasty'}
print(classmates)
print(classmates['Emma'])

for k, v in classmates.items():
    print(k + v)

#Download Image



