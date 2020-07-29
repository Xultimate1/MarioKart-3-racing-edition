import random
import csv
from datetime import datetime

WIDTH = 250
HEIGHT = 500

dodge_cars = ['deliveryflat','garbagetruck','hatchbacksports','police','sedan','suv','van','taxi']

dodge_car = Actor(random.choice(dodge_cars))
dodge_car.pos = (WIDTH/2+25, 10)

formula1 = Actor('race_car')

bushtree = Actor('bush-tree')
bushtree.pos = (WIDTH/2+85, HEIGHT/2)

mariotime = Actor('pixalmario')
mariotime.pos = (125, 400)

nucleartime = Actor('nevadafedaralland')


lanes = [WIDTH/2+25,WIDTH/2-25]
formula1.pos = (random.choice(lanes),HEIGHT-50)
naturelanes = [WIDTH/2+85,WIDTH/2-85]
speed = 2
score = 0
collide = False
game_end = False

filesave = False

music.play("mariobrosmusic")

def draw():
    global filesave
    if game_end == False:
        filesave = False
        screen.blit('grass', (0,0))
        RECTANGLE = Rect((75,0),(100,500))
        screen.draw.filled_rect(RECTANGLE, "black")
        screen.draw.line((125,0), (125,500), "yellow")
        screen.draw.text(f'cars dodged: {str(score)}', (80,40), color = "red", fontsize=30, ocolor = "yellow", owidth = 2)
        bushtree.draw()
        formula1.draw()
        dodge_car.draw()
        if collide == True:
            nucleartime.draw()
    else:
        screen.blit('city', (0,0))
        screen.draw.text("Game Over", center = (WIDTH/2,HEIGHT/2-200), color="red", fontname="supermario", fontsize = 37, ocolor = "yellow", owidth = 2)
        screen.draw.text(f"You dodged {str(score)} car(s)", center = (WIDTH/2,HEIGHT/2-160), color="red", fontname="supermario", fontsize = 20, ocolor = "yellow", owidth = 2)

        if filesave == False:
            today = datetime.now()
            with open('gamescores.csv','a') as file:
                writer = csv.writer(file)
                writer.writerow([today.date(),score])
            filesave = True

        mariotime.draw()

        with open('gamescores.csv','r') as file:
            reader = csv.reader(file)
            high_score=[]
            for row in reader:
                high_score.append(int(row[1]))
            high_score.sort(reverse=True)

        high_score = high_score[0]

        screen.draw.text(f"Best score so far: {str(high_score)}", center = (WIDTH/2,HEIGHT/2-100), color="red", fontname="supermario", fontsize = 15, ocolor = "yellow", owidth = 2)


def update():
    # Make the The Fomrula Car move Right and Left
    global dodge_car,dodge_cars, lanes, speed, naturelanes,collide, game_end, score



    if game_end == False:

        if keyboard.left:
            formula1.x -=1
            if formula1.x <= 86:
                formula1.x = 86

        elif keyboard.right:
            formula1.x +=1
            if formula1.x >= 164:
                formula1.x = 164

        # Moving the Dodge Car
        dodge_car.y +=speed

        if dodge_car.y > 500:
            dodge_car.y = 0
            dodge_car = Actor(random.choice(dodge_cars))
            dodge_car.pos = (random.choice(lanes), 10)
            speed += 0.2

            if collide == False:
                score += 1

        # Making the bushtree move
        bushtree.y +=speed

        if bushtree.y > 500:
            bushtree.y = 0
            bushtree.pos = (random.choice(naturelanes), 10)

        # Making the way the game ends(colision)
        if dodge_car.y >= 420 and dodge_car.y <= 490:
            if dodge_car.x == 100:
                if formula1.x <= 125 and formula1.x >= 75:
                    collide = True
                    nucleartime.pos = formula1.pos
                    clock.schedule_unique(remove_nuclear, 0.1)
                    sounds.nucleartime.play()
                    game_end = True
                    music.set_volume(0.5)


            elif dodge_car.x == 150:
                if formula1.x <= 175 and formula1.x >= 125:
                    nucleartime.pos = formula1.pos
                    collide = True
                    clock.schedule_unique(remove_nuclear, 0.1)
                    sounds.nucleartime.play()
                    game_end = True
                    music.set_volume(0.5)



def remove_nuclear():
    global collide
    collide = False
