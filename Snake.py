import curses
from random import randint

#setting up a window for the game to be played
curses.initscr()
window = curses.newwin(20,60, 0, 0) #(y,x) coordinates
#to control snake
window.keypad(1)
curses.noecho()
curses.curs_set(0)
window.border(0)
window.nodelay(1)

#LOGIC : 

snake = [(4, 4), (4, 3), (4, 2)]
food = (6, 6)



window.addch(food[0],food[1],"*")

ESC = 27
key = curses.KEY_RIGHT

score = 0


while key != ESC:

    window.addstr(0, 2, 'Score ' + str(score) + ' ')
    window.timeout(150 - len(snake) // 5 + len(snake) // 10 % 120)

    previous_key = key
    move = window.getch()
    key = move if move != -1 else previous_key

    if key not in [curses.KEY_LEFT, curses.KEY_DOWN, curses.KEY_RIGHT, curses.KEY_UP, ESC]:
        key = previous_key

    y = snake[0][0]
    x = snake[0][1]

    if key == curses.KEY_DOWN:
        y+=1
    if key == curses.KEY_UP:
        y-=1
    if key == curses.KEY_LEFT:
        x-=1
    if key == curses.KEY_RIGHT:
        x+=1

    snake.insert(0,(y,x))

    #need to see if snake is hitting the border
    if y == 0 : break
    if y == 19: break
    if x == 0 : break
    if x == 59 : break

    # need to see if snake hits itself as well

    if snake[0] in snake[1:]: break

    if snake[0] == food:
        score += 1
        food = ()
        while food ==():
            food = (randint(1,18),randint(1,58))
            if food in snake:
                food = ()
        window.addch(food[0],food[1],"*")
    else:
        #the snake will move
        last = snake.pop()
        window.addch(last[0],last[1], " ")


    # for coordinate in snake:
    #     window.addch(coordinate[0],coordinate[1], "~")
        
    window.addch(snake[0][0],snake[0][1],"~")


curses.endwin()

print(f"Final Score = {score}")
