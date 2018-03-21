# Imports
import pygame
import intersects

# Initialize game engine
pygame.mixer.pre_init()
pygame.init()


# Window
WIDTH = 700
HEIGHT = 590
SIZE = (WIDTH, HEIGHT)
TITLE = "Maze"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (28, 130, 40)
BROWN = (130, 80, 27)

# Fonts
MY_FONT = pygame.font.Font(None, 30)
    
#images
startscreen = pygame.image.load("images/startscreen.png")
player1_img = pygame.image.load('images/krabs.png')
player2_img = pygame.image.load('images/gary.png')
player1_speed = 4
player2_speed = 4

# stages
START = 0
PLAYING = 1
END = 2

# make walls
wall1 =  [20, 20, 300, 15]
wall2 =  [20, 20, 15, 300]
wall3 =  [60, 57, 230, 15]
wall4 =  [20, 350, 15, 250]
wall5 =  [20, 350, 200, 15]
wall6 =  [20, 310, 220, 15]
wall7 =  [200, 480, 15, 400]
wall8 =  [240, 95, 15, 475]
wall9 =  [60, 390, 140, 15]
wall10 =  [20, 430, 150, 15]
wall11 =  [60, 470, 140, 15]
wall12 =  [20, 510, 150, 15]
wall13 =  [60, 550, 140, 15]
wall14 =  [200, 390, 15, 800]
wall15 =  [275, 60, 15, 300]
wall16 =  [60, 60, 15, 225]
wall17 =  [315, 20, 15, 200]
wall18 =  [280, 345, 325, 15]
wall19 =  [280, 385, 140, 15]
wall20 =  [275, 385, 15, 180]
wall21 =  [290, 555, 300, 15]
wall22 =  [275, 550, 15, 40]
wall23 =  [100, 60, 15, 130]
wall24 =  [140, 100, 15, 100]
wall25 =  [140, 95, 100, 15]
wall26 =  [140, 165, 70, 15]
wall27 =  [140, 165, 15, 120]
wall28 =  [70, 215, 80, 15]
wall29 =  [100, 255, 15, 60]
wall30 =  [180, 200, 70, 15]
wall31 =  [150, 235, 70, 15]
wall32 =  [180, 270, 70, 15]
wall33 =  [355, 0, 15, 195]
wall34 =  [395, 20, 280, 15]
wall35 =  [395, 20, 15, 215]
wall36 =  [315, 220, 90, 15]
wall37 =  [315, 260, 15, 60]
wall38 =  [315, 260, 360, 15]
wall39 =  [315, 305, 40, 15]
wall40 =  [60, 100, 40, 15]
wall41 =  [385, 260, 15, 60]
wall42 =  [660, 260, 15, 305]
wall43 =  [580, 390, 15, 180]
wall44 =  [315, 425, 15, 105]
wall45 =  [315, 425, 235, 15]
wall46 =  [315, 470, 65, 15]
wall47 =  [315, 515, 105, 15]
wall48 =  [420, 385, 15, 55]
wall49 =  [465, 385, 130, 15]
wall50 =  [535, 425, 15, 105]
wall51 =  [400, 515, 100, 15]
wall52 =  [450, 430, 15, 55]
wall53 =  [490, 470, 15, 60]
wall54 =  [410, 470, 15, 60]
wall55 =  [180, 130, 60, 15]
wall56 =  [435, 60, 15, 210]
wall57 =  [550, 20, 15, 250]
wall58 =  [435, 60, 90, 15]
wall59 =  [475, 100, 90, 15]
wall60 =  [435, 140, 90, 15]
wall61 =  [475, 180, 90, 15]
wall62 =  [435, 220, 90, 15]
wall63 =  [590, 220, 120, 15]
wall64 =  [550, 180, 130, 15]
wall65 =  [590, 140, 120, 15]
wall66 =  [550, 100, 130, 15]
wall67 =  [590, 60, 120, 15]
wall68 =  [430, 300, 15, 50]
wall69 =  [470, 270, 15, 50]
wall70 =  [510, 300, 15, 50]
wall71 =  [550, 270, 15, 50]
wall72 =  [590, 300, 15, 50]
wall73 =  [590, 300, 45, 15]
wall74 =  [630, 340, 45, 15]
wall75 =  [620, 385, 15, 185]

walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9,
         wall10, wall11, wall12, wall13, wall14, wall15, wall16, wall17,
         wall18, wall19, wall20, wall21,  wall22, wall23, wall24, wall25,
         wall26, wall27, wall28, wall29, wall30, wall31, wall32, wall33,
         wall34, wall35, wall36, wall37, wall38, wall39, wall40, wall41,
         wall42, wall43, wall44, wall45, wall46, wall47, wall48, wall49,
         wall50, wall51, wall52, wall53, wall54, wall55, wall56, wall57,
         wall58, wall59, wall60, wall61, wall62, wall63, wall64, wall65,
         wall66, wall67, wall68, wall69, wall70, wall71, wall72, wall73,
         wall74, wall75]

# Treasure chest
chest2_img = pygame.image.load('images/chest1.png')
chest1_img = pygame.image.load('images/chest2.png')
chest = [75, 80, 25, 25, False]


# Make coins
coins = []
coins_img = pygame.image.load('images/coins.png')

coins1 = [40, 37, 10, 10]
coins2 = [60, 37, 25, 25]
coins3 = [150, 410, 25, 25]
coins4 = [130, 410, 25, 25]
coins5 = [110, 410, 25, 25]
coins6 = [90, 410, 25, 25]
coins7 = [70, 410, 25, 25]
coins8 = [50, 410, 25, 25]
coins9 = [150, 450, 25, 25]
coins10 = [130, 450, 25, 25]
coins11 = [110, 450, 25, 25]
coins12 = [90, 450, 25, 25]
coins13 = [70, 450, 25, 25]
coins14 = [50, 450, 25, 25]
coins15 = [150, 490, 25, 25]
coins16 = [130, 490, 25, 25]
coins17 = [110, 490, 25, 25]
coins18 = [90, 490, 25, 25]
coins19 = [70, 490, 25, 25]
coins20 = [50, 490, 25, 25]
coins21 = [150, 530, 25, 25]
coins22 = [130, 530, 25, 25]
coins23 = [110, 530, 25, 25]
coins24 = [90, 530, 25, 25]
coins25 = [70, 530, 25, 25]
coins26 = [50, 530, 25, 25]
coins27 = [80, 37, 25, 25]
coins28 = [100, 37, 25, 25]
coins29 = [120, 37, 25, 25]
coins30 = [140, 37, 25, 25]
coins31 = [160, 37, 25, 25]
coins32 = [180, 37, 25, 25]
coins33 = [200, 37, 25, 25]
coins34 = [40, 0, 25, 25]
coins35 = [60, 0, 25, 25]
coins36 = [80, 0, 25, 25]
coins37 = [100, 0, 25, 25]
coins38 = [120, 0, 25, 25]
coins39 = [140, 0, 25, 25]
coins40 = [160, 0, 25, 25]
coins41 = [180, 0, 25, 25]
coins42 = [200, 0, 25, 25]
coins43 = [220, 0, 25, 25]
coins44 = [240, 0, 25, 25]
coins45 = [260, 0, 25, 25]
coins46 = [280, 0, 25, 25]
coins47 = [300, 0, 25, 25]
coins48 = [320, 0, 25, 25]
coins49 = [220, 37, 25, 25]
coins50 = [240, 37, 25, 25]
coins51 = [260, 37, 25, 25]
coins52 = [280, 37, 25, 25]
coins53 = [300, 37, 25, 25]


def setup():
    global stage, time_remaining, ticks, score, score2, win, player1, player2, vel1, vel2, coins

    stage = START
    time_remaining = 120
    ticks = 0

    score = 0
    score2 = 0

    win = False

    player1 =  [680, 570, 17, 18]
    vel1 = [0, 0]
    player2 =  [0, 0, 17,18]
    vel2 = [0, 0]

    coins = [coins1, coins2, coins3, coins4, coins5, coins6, coins7, coins8, coins9,
             coins10, coins11, coins12, coins13, coins14, coins15, coins16, coins17,
             coins18, coins19, coins20, coins21, coins22, coins23, coins24, coins25,
             coins26, coins27, coins28, coins29, coins30, coins31, coins32, coins33,
             coins34, coins35, coins36, coins37, coins38, coins39, coins40, coins41,
             coins42, coins43, coins44, coins45, coins46, coins47, coins48, coins49,
             coins50, coins51, coins52, coins53]

    pygame.mixer.music.play(-1)

    
# Sound Effects
pygame.mixer.music.load("sounds/jellyfish-jam.ogg")
meow = pygame.mixer.Sound("sounds/beep.ogg")

# Game loop
setup()
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            
            if stage == START:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        stage = PLAYING

            elif stage == PLAYING:            
                pass

            elif stage == END:
                if event.key == pygame.K_SPACE:
                    setup()

                    
    if stage == PLAYING:
        ''' process player input '''
        pressed = pygame.key.get_pressed()

        up = pressed[pygame.K_UP]
        down = pressed[pygame.K_DOWN]
        left = pressed[pygame.K_LEFT]
        right = pressed[pygame.K_RIGHT]

        if left:
            vel1[0] = -player1_speed
        elif right:
            vel1[0] = player1_speed
        else:
            vel1[0] = 0

        if up:
            vel1[1] = -player1_speed
        elif down:
            vel1[1] = player1_speed
        else:
            vel1[1] = 0
            
        up = pressed[pygame.K_w]
        down = pressed[pygame.K_s]
        left = pressed[pygame.K_a]
        right = pressed[pygame.K_d]

        if left:
            vel2[0] = -player2_speed
        elif right:
            vel2[0] = player2_speed
        else:
            vel2[0] = 0

        if up:
            vel2[1] = -player2_speed
        elif down:
            vel2[1] = player2_speed
        else:
            vel2[1] = 0


        ''' move the players in horizontal direction '''
        player1[0] += vel1[0]
        player2[0] += vel2[0]
        
        ''' resolve collisions horizontally '''
        for w in walls:
            if intersects.rect_rect(player1, w):        
                if vel1[0] > 0:
                    player1[0] = w[0] - player1[2]
                elif vel1[0] < 0:
                    player1[0] = w[0] + w[2]
                    
        for w in walls:
            if intersects.rect_rect(player2, w):        
                if vel2[0] > 0:
                    player2[0] = w[0] - player2[2]
                elif vel2[0] < 0:
                    player2[0] = w[0] + w[2]
                    
        ''' move the players in vertical direction '''
        player1[1] += vel1[1]
        player2[1] += vel2[1]
        
        ''' resolve collisions vertically '''
        for w in walls:
            if intersects.rect_rect(player1, w):                    
                if vel1[1] > 0:
                    player1[1] = w[1] - player1[3]
                if vel1[1]< 0:
                    player1[1] = w[1] + w[3]

        for w in walls:
            if intersects.rect_rect(player2, w):                    
                if vel2[1] > 0:
                    player2[1] = w[1] - player2[3]
                if vel2[1]< 0:
                    player2[1] = w[1] + w[3]
        
        ''' here is where you should resolve player collisions with screen edges '''
        left = player1[0]
        right = player1[0] + player1[2]
        top = player1[1]
        bottom = player1[1] +player1[3]

        ''' if the block is moved out of the window, nudge it back on. '''
        if left < 0:
                player1[0] = 0
        elif right > WIDTH:
                player1[0] = WIDTH - player1[2]

        if top < 0:
                player1[1] = 0
        elif bottom > HEIGHT:
               player1[1] = HEIGHT - player1[3]

        left = player2[0]
        right = player2[0] + player2[2]
        top = player2[1]
        bottom = player2[1] +player2[3]
        
        if left < 0:
                player2[0] = 0
        elif right > WIDTH:
                player2[0] = WIDTH - player2[2]

        if top < 0:
                player2[1] = 0
        elif bottom > HEIGHT:
               player2[1] = HEIGHT - player2[3]

        ''' get the coins '''
        hit_list = []

        for c in coins:
            if intersects.rect_rect(player1, c):
                hit_list.append(c)
                
            elif intersects.rect_rect(player2, c):
                hit_list.append(c)
                
        for hit in hit_list:
            coins.remove(hit)
            score += 1
            meow.play()
            
        if len(coins) ==0 and wall40 in walls:
            walls.remove(wall40)

        ''' get chest '''
        if intersects.rect_rect(player1, chest):
            chest[4] = True
            win = True
            
        if intersects.rect_rect(player2, chest):
            chest[4] = True
            win = True
            
        ''' timer stuff '''
        ticks += 1

        if ticks % refresh_rate == 0:
            time_remaining -= 1

        if time_remaining == 0:
            stage = END
            
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(GREEN)

    loc = player1[:2]
    screen.blit(player1_img, loc)

    loc = player2[:2]
    screen.blit(player2_img, loc)
    
    for w in walls:
        pygame.draw.rect(screen, BROWN, w)

    for c in coins:
        loc = c[:2]
        screen.blit(coins_img, loc)

    loc = chest[:2]
    unlocked = chest[4]

    if unlocked:
        screen.blit(chest1_img, loc)
    else:
        screen.blit(chest2_img, loc)

    
    if win:
        font = pygame.font.Font(None, 48)
        text = font.render("You Win!", 1, WHITE)
        screen.blit(text, [400, 200])

    ''' timer text '''
    timer_text = MY_FONT.render(str(time_remaining), True, WHITE)
    screen.blit(timer_text, [340, 0])

    '''x to quit'''
    text1 = MY_FONT.render("(Press X to quit)", True, WHITE)
    screen.blit(text1, [525, 550])
    
    ''' begin/end game text '''
    if stage == START:
        screen.blit(startscreen, (0, 0))
        text1 = MY_FONT.render("(Press SPACE to play.)", True, WHITE)
        text2 = MY_FONT.render("(Press X to quit)", True, WHITE)
        text3 = MY_FONT.render("Play as Mr. Krabs(arrow keys) or Gary(a,w,s,d) to collect all",True, WHITE)
        text4 = MY_FONT.render("the coins to open the door to the treasure chest.", True, WHITE)
        screen.blit(text1, [250, 430])
        screen.blit(text2, [270, 500])
        screen.blit(text3, [20, 20])
        screen.blit(text4, [20, 40])
        
    elif stage == END:
        text1 = MY_FONT.render("Game Over", True, WHITE)
        text2 = MY_FONT.render("(Press SPACE to restart.)", True, WHITE)
        screen.blit(text1, [310, 150])
        screen.blit(text2, [210, 200])
    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
