from pygame import color
from shapes import *
import pygame
import random
import sys
import time



block = 30
x = 0
y = 3

x_side = 90
y_side = 150


colors = [
    (0, 0, 0),
    (0, 255, 255),
    (204, 0, 255),
    (255, 255, 0),
    (255, 81, 0),
    (0, 0, 255),
    (0, 128, 0),
    (255, 127, 80),
    (220, 20, 60),
    (255, 0, 85),
]

rows = 10
columns = 20

Data = []

for i in range(rows):
    temp = []
    for j in range(columns):
        temp.append(0)
    Data.append(temp)


# for t in range(10):
#     Data[t][5] = 3
#     Data[t][17] = 3

# Data[4][14] = 7




myshapes = [L, LINE, MINILINE, ORIBLINE, POINT, CROSS, Z, Z2 ]


sh_type = random.randint(0, len(myshapes) - 1)
# sh_type = 1
random_color = random.randint(1, len(colors) - 1)
Rotation = 0
sheklman = myshapes[sh_type][Rotation]
score = 0


def Barkhord(sheklman):
    Barkhord_b = False
    for i in range(4):
        for j in range(4):
            if sheklman[i][j] > 0:
                if i + y > 9 or i + y < 0  or j + x > 19 or Data[i + y][j + x] > 0:
                    Barkhord_b = True
    # print("barkhord: ", Barkhord_b)
    return Barkhord_b






pygame.init()



window = pygame.display.set_mode((800, 600))
bg = pygame.image.load('3.jpg').convert()


fps = 35
shomarandeh = 0
speed = 30
Vaziatbazi = "start"



isRuning = True
while isRuning:
    if ((shomarandeh % speed) == 0) and (Vaziatbazi == "start"):
        x += 1
        if Barkhord(sheklman) == True:
            x -= 1
            for i in range(4):
                for j in range(4):
                    if sheklman[i][j] > 0:
                        Data[i + y][j + x] = random_color
            i = 0
            j = 0
            khat_shomar = 0
            for j in range(columns):
                sefr_shomar = 0
                for i in range(rows):
                    if Data[i][j] > 0:
                        sefr_shomar += 1
                if sefr_shomar > 9:
                    khat_shomar += 1
                    for k in range(j, 1, -1):
                        for h in range(rows):
                            Data[h][k] = Data[h][k - 1]
            score += khat_shomar ** 2
            x = 0
            y = 3
            sh_type = random.randint(0, len(myshapes) - 1)
            # sh_type = 1
            random_color = random.randint(1, len(colors) - 1)
            Rotation = 0
            sheklman = myshapes[sh_type][Rotation]
        if Barkhord(sheklman) == True:
            Vaziatbazi = "gameover"
    window.blit(bg, (0, 0))
    #window.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRuning = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                for i in range(rows):
                    for j in range(columns):
                        Data[i][j] = 0
                Vaziatbazi = "start"
                x = 0
                y = 3
                sh_type = random.randint(0, len(myshapes) - 1)
                # sh_type = 1
                random_color = random.randint(1, len(colors) - 1)
                Rotation = 0
                fps = 35
                speed = 30
                sheklman = myshapes[sh_type][Rotation]
                score = 0


            if (event.key == pygame.K_n) and (Vaziatbazi == "start"):
                sh_type = random.randint(0, len(myshapes) - 1)
                # sh_type = 1
                random_color = random.randint(1, len(colors) - 1)
                Rotation = 0
                sheklman = myshapes[sh_type][Rotation]
                

            if (event.key == pygame.K_LEFT) and (Vaziatbazi == "start"):
                previous_Rot = Rotation
                if (Rotation >= 0) and (Rotation < len(myshapes[sh_type]) - 1):
                    Rotation += 1
                else:
                    Rotation = 0
                # Rotation = (Rotation + 1) % (len(myshapes[sh_type]))
                sheklman = myshapes[sh_type][Rotation]

                if Barkhord(sheklman) == True:
                    Rotation = previous_Rot
                    # if (Rotation > 0) and (Rotation <= (len(myshapes[sh_type]) - 1)):
                    #     Rotation -= 1
                    # else:
                    #     Rotation = len(myshapes[sh_type]) - 1

                sheklman = myshapes[sh_type][Rotation]
                # Barkhord(sheklman)

            if (event.key == pygame.K_RIGHT) and (Vaziatbazi == "start"):
                fps = 60
                speed = 2

            if (event.key == pygame.K_UP) and (Vaziatbazi == "start"):
                y -= 1
                if Barkhord(sheklman) == True:
                    y += 1

            if (event.key == pygame.K_DOWN) and (Vaziatbazi == "start"):
                y += 1
                if Barkhord(sheklman) == True:
                    y -= 1

        if (event.type == pygame.KEYUP) and (Vaziatbazi == "start"):
            fps = 35
            speed = 30


    for i in range(rows):
        for j in range(columns):
            pygame.draw.rect(window, (255, 255, 255), ( x_side + j * block ,y_side + i * block, block, block ), 1)
            if Data[i][j] > 0:
                pygame.draw.rect(window, colors[Data[i][j]], (x_side + (j) * block + 1,y_side + (i) * block + 1, block - 2, block - 2 ), 0)

    i = 0
    j = 0
    for i in range(4):
        for j in range(4):
            if sheklman[i][j] > 0:
                pygame.draw.rect(window, colors[random_color], (x_side + (j + x) * block + 1,y_side + (i + y) * block + 1, block - 2, block - 2 ), 0)
            # else:
            #     pygame.draw.rect(window, (255, 255, 255), ( (j + x) * block + 1, (i + y) * block + 1, block - 2, block - 2 ), 0)
            
    font = pygame.font.SysFont('Calibri', 25, True, False)
    font1 = font1 = pygame.font.SysFont('Calibri', 65, True, False)
    sookhti = font1.render("Sookhti tamoom shod!", True, (255, 125, 0))
    sookhti_2 = font1.render("ESC ro feshar bedeh !", True, (255, 215, 0))
    

    # text = font.render("vazeeat Barkhord: " + str(Barkhord(sheklman)), True, (255, 255, 255))
    
    # window.blit(text, [0, 10])
    

    last_hsighscore = open("highscore.txt", "rt")

    if open("highscore.txt", "rt") == True:
        open("highscore.txt", "rt")
    elif open("highscore.txt", "rt") == False:
        open("highscore.txt", "xt")
        open("highscore.txt", "wt").write(0)
        
    
    last_hsighscore = open("highscore.txt", "rt").read()

    newhighscore = last_hsighscore

    hidden_color = (255, 255, 255)
    if Vaziatbazi == "gameover":
        hidden_color = (0, 0, 0)
    playerscore = font.render("Score: " + str(score), True, (255, 255, 255))

    scoretext = font.render("Last highScore: " + str(last_hsighscore), True, hidden_color)
    window.blit(playerscore, [0, 10])
    window.blit(scoretext, [0, 50])
    
    if score > int(last_hsighscore):
        newhighscore = score
        open("Episode3/highscore.txt", "wt").write(str(newhighscore))
    
    newhighscore_text = font.render("your highscore: " + str(newhighscore), True, (255, 255, 255))
    

    if Vaziatbazi == "gameover":
        window.blit(sookhti, [100, 400])
        window.blit(sookhti_2, [100, 460])
        window.blit(newhighscore_text, [280, 40])
        



    pygame.display.update()
    pygame.time.Clock().tick(fps)
    shomarandeh += 1