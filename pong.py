import pygame, sys, random

def ball_animation():
    global ball_speed_x, ball_speed_y, score_play, score_opp
    ball.x += ball_speed_x
    ball.y += ball_speed_y      

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_restart()   

    if ball.colliderect(player):
        score_play +=1  
        ball_speed_x *= -1
    if ball.colliderect(opponent):
        score_opp +=1
        ball_speed_x *= -1    

def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height        

def opponent_ai():
    global score_opp
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom >ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def ball_restart():
    global ball_speed_y, ball_speed_x
    ball.center = (screen_width/2, screen_height/2)
                   
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))


#general setup
pygame.init()
clock = pygame.time.Clock()
score_play = 0
score_opp = 0

#setting up the main window
screen_width = 1000
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')


#Game Rects
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_width - 10, screen_height/2 - 70,10, 140)
opponent = pygame.Rect(0, screen_height/2 -70, 10, 140)

bg_color = pygame.Color('grey12')
WHITE = pygame.Color('white')
light_grey = (200, 200, 200)

ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 7

while True:
    #Handling the input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed +=7
            if event.key == pygame.K_UP:
                player_speed -=7   
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -=7
            if event.key == pygame.K_UP:
                player_speed +=7      
              


    ball_animation()
    player_animation()   
    opponent_ai()    

    #visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, (screen_width/2 - 100, screen_height/2 - 100, 200, 200) ) 
    pygame.draw.ellipse(screen, bg_color, (screen_width/2 - 98, screen_height/2 - 98, 196, 196) ) 
    pygame.draw.ellipse(screen, light_grey, ball)       
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_height))


    #display scores
    font = pygame.font.Font(None , 40)
    text = font.render(str(score_opp), 1, WHITE)
    screen.blit(text, (250,10))
    text = font.render(str(score_play), 1, WHITE)
    screen.blit(text, (750,10))
    

    #updating the window
    pygame.display.flip()
    clock.tick(60)        
