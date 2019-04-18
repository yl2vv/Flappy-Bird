import pygame
import gamebox
import random

# ps8nu Philip Song
# mz7ey Maryam Zaher
# Yl2vv James Lim

"""
A running game that is on a straight plane. The character has to dodge obstacles by jumping or crouching. 
The setting is a starved North Korean who is trying to escape the tyrannous Kim Jong Un. 
He must survive in order to cross the border. 
He must jump over land mines. 
He must avoid hitting the fence. 
If he gets caught (in a fence) or injured (by land mine) too many times (3 lives) 
The catch is... the game never ends... so he will never defect to South Korea.... :( 


Required Features: 
User Input - character - Jump up (Up Arrow Key) , character2 - Jump up
 (Down Arrow Key) 
Graphics/Images - We will find images 
Start Screen - Game instructions: 
    The game will be continuously moving so just jump up 
    To jump use the up arrow key 
    To crouch use the down arrow key 



Optional Features: 

Animation: The characters will be running(moving)
Timer: Counts the time running spaceite #not sure if this if this is a scrolling level? 
Collectibles: Extra life - "Found some bandages" - provides another life to the character - will occur not frequently 
Health meter: The character has 3 initial lives. Each time they hit an obstacle they lose a life. 
Two player: Two players can play 

"""

import pygame
import gamebox
import random

camera = gamebox.Camera(600, 400)

#character = gamebox.from_image(100, 305, "https://d2gg9evh47fn9z.cloudfront.net/800px_COLOURBOX13488103.jpg")
#character.width = 50
ground = gamebox.from_color(600, 380, "darkgreen", 60000, 100)
character = gamebox.from_color(100, 305, "red", 10, 50)
character2 = gamebox.from_color(50, 305, "blue", 10, 50)


moon = gamebox.from_image(500, 50, "https://cdn.dribbble.com/users/271435/screenshots/2488117/8.png")
moon.width = 100
#landmine = gamebox.from_color(camera.right, 0, "gray", 10, random.randrange(200, 400))
#barbed_fences = gamebox.from_color(camera.right, 100, "gray", 60, random.randrange(200, 400))




life_box = gamebox.from_color(100, 50, "black", 100, 20)
life_text = gamebox.from_text(70, 30, "Health", 20, "Pink")


background = []
character.coins_collected = 0
obstacles = []
coins = []
ticks = 0
time = 0
health = 100
game_on = False
multiplayer = False
draw_fence = False

def tick(keys):
    global ticks
    global time
    global game_on
    global start
    global character
    global character2
    global coin
    global background
    global multiplayer
    global draw_fence
    global life
    global health
    global name
    global creators
    global instructions
    camera.clear("darkblue")
    ticks = +1

    if game_on == False:
        start = gamebox.from_text(camera.x, camera.y - 100, "Press 1 for Single | Press 2 for Double", 30, "White")
        name = gamebox.from_text(camera.x, camera.y, "THE GREAT ESCAPE", 60, "White")
        creators = gamebox.from_text(camera.x, camera.y + 30, "by Philip Song (ps8nu), Maryam Zaher (mz7ey), and James Lim (yl2vv)", 15, "White")
        instructions = gamebox.from_text(camera.x, camera.y + 50, "Player One: Up to Jump | Player Two: Space to Jump", 25, "White")




    if pygame.K_2 in keys:
        game_on = True
        start = gamebox.from_text(camera.x, camera.y - 100, "", 30, "White")
        name = gamebox.from_text(camera.x, camera.y - 120, "", 40, "White")
        creators = gamebox.from_text(camera.x, camera.y + 10,"", 10, "White")
        instructions = gamebox.from_text(camera.x, camera.y + 50, "",15, "White")
        multiplayer = True
    if pygame.K_1 in keys:
        game_on = True
        start = gamebox.from_text(camera.x, camera.y - 100, "", 30, "White")
        name = gamebox.from_text(camera.x, camera.y - 120, "", 40, "White")
        creators = gamebox.from_text(camera.x, camera.y + 10, "", 10, "White")
        instructions = gamebox.from_text(camera.x, camera.y + 50, "", 15, "White")


    if game_on:
        if ticks % 1 == 0:
            time += 1

        if time % 31 == 0:
            position = random.randrange(0,40)
            #landmine = gamebox.from_color(camera.right + position, 325, "white", 15, 15)
            landmine = gamebox.from_image(camera.right + position, 325, "https://i.imgur.com/r14SQvn.png")
            landmine.width = 25
            obstacles.append(landmine)
        for things in obstacles:
            camera.draw(things)
        for landmine in obstacles:
            landmine.x -= 5

        if time % 120 == 0:
            position = random.randrange(0,40)
            height = random.randrange(210, 240)
            #barbed_fence = gamebox.from_color(camera.right + position, height, "gray", 15, 60)
            barbed_fence = gamebox.from_image(camera.right + position, height, "https://i.imgur.com/pcGJ2UQ.png")
            barbed_fence.width = 45
            obstacles.append(barbed_fence)
        for things in obstacles:
            camera.draw(things)
        for barbed_fence in obstacles:
            barbed_fence.x -= 5

        if pygame.K_UP in keys and character.bottom == ground.top:
            character.y += -70
            keys.clear()
        if character.y != 305:
            character.y += 7

        if pygame.K_SPACE in keys and character2.bottom == ground.top:
            character2.y += -70
            keys.clear()
        if character2.y != 305:
            character2.y += 7

    life = gamebox.from_color(100, 50, "Pink", health, 20)

    for landmine in obstacles:
        if multiplayer == True:
            if character.touches(landmine) or character2.touches(landmine):
                health -= 20
                obstacles.remove(landmine)

        if multiplayer == False:
            if character.touches(barbed_fence):
                health -= 20
                obstacles.remove(landmine)


    for barbed_fence in obstacles:
        if multiplayer == True:
            if character.touches(barbed_fence) or character2.touches(barbed_fence):
                health -= 20
                obstacles.remove(barbed_fence)
        if multiplayer == False:
            if character.touches(barbed_fence):
                health -= 20
                obstacles.remove(barbed_fence)


    if time % 30 == 0:
        position = random.randrange(0, 40)
        height = random.randrange(220, 250)
        #coin = gamebox.from_color(camera.right + position, height, 'gold', 10, 10)
        coin = gamebox.from_image(camera.right + position, height, "https://imgur.com/ucBvqiv.png")
        coin.width = 15
        coins.append(coin)
    for things in coins:
        camera.draw(things)
    for coin in coins:
        coin.x -= 5

    for coin in coins:
        if character.touches(coin) or character2.touches(coin):
            coins.remove(coin)
            time += 100

    if time % 200 == 0:
        position = random.randrange(0, 40)
        height = random.randrange(150, 250)
        #mega_coin = gamebox.from_color(camera.right + position, height, 'orange', 20, 20)
        # mega_coin = gamebox.from_image(camera.right + position, height,"https://i.imgur.com/3MEfJ7F.png")
        mega_coin = gamebox.from_image(camera.right + position, height, "https://imgur.com/ucBvqiv.png")
        mega_coin.width = 20
        coins.append(mega_coin)
    for things in coins:
        camera.draw(things)
    for mega_coin in coins:
        mega_coin.x -= 5

    for mega_coin in coins:
        if character.touches(mega_coin) or character2.touches(mega_coin):
            coins.remove(mega_coin)
            time += 1000


    scoreboard = gamebox.from_text(300, 50, str(time), 40, "white", bold=True)
    if multiplayer == True:
        background = [start, instructions, creators, name, moon, life_text, life_box, life, ground, character, scoreboard, character2]
    if multiplayer == False:
        background = [start, instructions, creators, name, moon, life_text, life_box, life, ground, character, scoreboard]

    if health <= 0:
        background.remove(life)
        game_over = gamebox.from_text(camera.x, camera.y, "Game Over! " + "Your Score is: " + str(time), 30, "white")
        camera.draw(game_over)
        gamebox.pause()

    for things in background:
        camera.draw(things)

    camera.display()


gamebox.timer_loop(30, tick)