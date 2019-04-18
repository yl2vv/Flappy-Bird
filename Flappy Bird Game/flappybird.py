# yl2vv James Lim


import pygame
import gamebox
import random

camera = gamebox.Camera(350, 500)

bird = gamebox.from_image(100, 250, "https://cdn140.picsart.com/243765823023212.png?r1024x1024")
#bird = gamebox.from_color(100, 250, 'yellow', 33, 33)
bird.size = [33, 33]
ground = gamebox.from_color(175, 480, 'brown', 350, 80)
grass = gamebox.from_color(175, 430, 'mediumseagreen', 350, 20)
lose = gamebox.from_text(camera.x, camera.y - 100, "", 30, "lightsalmon")
sky = gamebox.from_color(175, 0, "black", 350, 1)

background = []
obstacles = []
score = 0
ticks = 0
game_on = False


def tick(keys):
    global game_on
    global ticks
    global score
    global lose
    global start
    ticks += 1
    camera.clear("lightblue")
    if game_on == False:
       start = gamebox.from_text(camera.x, camera.y - 100, "Press Space to Start", 30, "black")

    if pygame.K_SPACE in keys:
       game_on = True
       start = gamebox.from_text(camera.x, camera.y - 100, "", 30, "black")

    if game_on:
        if ticks % 50 == 0:
            height = random.randrange(0, 125)
            pipe_top = gamebox.from_color(camera.right + 50, height, "green", 70, 250)
            pipe_top.rotate(180)
            obstacles.append(pipe_top)
            pipe_bottom = gamebox.from_color(camera.right +50, height +340, "green", 70, 250)
            obstacles.append(pipe_bottom)

        if pygame.K_SPACE in keys:
            bird.speedy = -8
            keys.clear()
        bird.move_speed()
        bird.speedy *= 0.95
        bird.speedy += 0.75
        bird.move_to_stop_overlapping(grass)
        bird.move_to_stop_overlapping(sky)

        for pipes in obstacles:
            pipes.x -= 5
            if pipes.right < camera.left - 200:
                obstacles.remove(pipes)

        if ticks >= 75:
            if ticks % 50 == 5:
                score += 1

        for pipes in obstacles:
            if bird.touches(pipes):
                lose = gamebox.from_text(camera.x, camera.y - 100, "Game Over!" + " Your score is: " + str(score), 30,
                                         "black")
                camera.draw(lose)
                gamebox.pause()
            if bird.touches(grass):
                lose = gamebox.from_text(camera.x, camera.y - 100, "Game Over!" + " Your score is: " + str(score), 30,
                                         "black")
                camera.draw(lose)
                gamebox.pause()
            if bird.touches(sky):
                lose = gamebox.from_text(camera.x, camera.y - 100, "Game Over!" + " Your score is: " + str(score), 30,
                                         "black")
                camera.draw(lose)
                gamebox.pause()

    scoreboard = gamebox.from_text(175, 50, str(score), 40, "white", bold=True)
    background = [ground, grass, scoreboard, start, sky]
    for pipe in obstacles:
        camera.draw(pipe)
    for things in background:
        camera.draw(things)
    camera.draw(bird)
    camera.draw(lose)

    camera.display()


gamebox.timer_loop(30, tick)