#code for Makey Makey TUI project
#Shreya Wadehra

def looping(inputuser):
    x = input()
    if inputuser in x:
        return;
    else:
        looping(inputuser)

import random;

#blue - b
#green - g
#orange - o
#pink  - p
#yellow - y
#aqua - a

while 1:
    colors = ['BLUE', 'GREEN', 'ORANGE', 'PINK', 'YELLOW', 'AQUA'];
    index = random.randint(0,5);
    user_input = input("HIT THE " + colors[index] + " PAD!!! ");
    loop = True;

    if index == 0: #BLUE
            if 'b' in user_input:
                continue;
            else:
                looping('b');
    elif index == 1: #GREEN
            if 'g' in user_input:
                continue;
            else:
                looping('g');
    elif index == 2: #ORANGE
            if 'o' in user_input:
                continue;
            else:
                looping('o');
    elif index == 3: #PINK
            if 'p' in user_input:
                continue;
            else:
                looping('p');
    elif index == 4: #YELLOW
            if 'y' in user_input:
                continue;
            else:
                looping('y');
    else: #AQUA
            if 'a' in user_input:
                continue;
            else:
                looping('a');
