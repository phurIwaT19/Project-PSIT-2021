import pygame, sys

pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode( (WIDTH, HEIGHT) ) #ขนาดหน้าจอ
pygame.display.set_caption( 'TIC TAC TOE') #ชื่อเกม

#define variable
markers = []
clicked = False
pos = []
player = 1
winner = 0
game_over = False
#define font
font = pygame.font.SysFont(None, 50)
font_2 = pygame.font.SysFont(None, 40)

#creat play again rect
again_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2, 200, 50)

#วาดตาราง 9 ช่อง
def draw_board(): 
    BG_COLOR = (102, 178, 255)
    LIGHT_PURPLE = (51, 153, 255)
    screen.fill( BG_COLOR ) #สีพื้นหลังจอ
    #Vertical
    pygame.draw.line( screen, LIGHT_PURPLE, (200, 0), (200, 600), 20) #1
    pygame.draw.line( screen, LIGHT_PURPLE, (400, 0), (400, 600), 20) #2
    #Horizontal
    pygame.draw.line( screen, LIGHT_PURPLE, (0, 200), (600, 200), 20) #1
    pygame.draw.line( screen, LIGHT_PURPLE, (0, 400), (600, 400), 20) #2

for x in range(3):
    row = [0]*3
    markers.append(row)

def draw_markers():
    cross_width = 20
    circle_width = 15
    circle_radius = 60
    LIGHT_GREY = (192, 192, 192)
    DARK_GREY = (96, 96, 96)
    SPACE = 50
    x_pos = 0
    for x in markers:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(screen, LIGHT_GREY, (x_pos * 200 + SPACE ,y_pos * 200 + 200 - SPACE), (x_pos * 200 + 200 - SPACE ,y_pos * 200 + SPACE), cross_width)
                pygame.draw.line(screen, LIGHT_GREY, (x_pos * 200 + SPACE, y_pos * 200 + SPACE), (x_pos * 200 + 200 - SPACE ,y_pos * 200 + 200 - SPACE), cross_width)
            if y == -1:
                pygame.draw.circle(screen, DARK_GREY, (x_pos * 200 + 100, y_pos * 200 + 100), circle_radius, circle_width)
            y_pos += 1
        x_pos += 1
def check_winner():
    global winner
    global game_over
    y_pos = 0
    for x in markers:
        #check column
        if sum(x) == 3:
            winner = 1
            game_over = True
        if sum(x) == -3:
            winner = 2
            game_over = True
        #check row
        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == 3:
            winner = 1
            game_over = True
        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == -3:
            winner = 2
            game_over = True
        y_pos += 1
    #check cross
    if markers[0][0] + markers[1][1] + markers[2][2] == 3 or markers[2][0] + markers[1][1] + markers[0][2] == 3:
        winner = 1
        game_over = True
    if markers[0][0] + markers[1][1] + markers[2][2] == -3 or markers[2][0] + markers[1][1] + markers[0][2] == -3:
        winner = 2
        game_over = True
def draw_winner(winner):
    blue = (0, 0, 255)
    green = (0, 255, 0)
    win_text = 'Player ' + str(winner) + " wins!"
    win_img = font.render(win_text, True, blue)
    pygame.draw.rect(screen, green, (WIDTH // 2 - 150, HEIGHT // 2 - 100, 300, 80), 40, 20)
    screen.blit(win_img, (WIDTH // 2 - 115, HEIGHT // 2 - 75))

    again_text = 'Play again'
    again_img = font_2.render(again_text, True, blue)
    pygame.draw.rect(screen, green, again_rect, 25, 20)
    screen.blit(again_img, (WIDTH // 2 - 70, HEIGHT // 2 + 10))
#mainloop
run = True
while run:
    draw_board()
    draw_markers()
    #เปิดปิดหน้าต่าง
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if game_over == 0:
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP:
                clicked = False
                pos = pygame.mouse.get_pos()
                mark_x = pos[0]
                mark_y = pos[1]
                if markers[mark_x // 200][mark_y // 200] == 0:
                    markers[mark_x // 200][mark_y // 200] = player
                    player *= -1
                    check_winner()
    if game_over == True:
        draw_winner(winner)
        #check 
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False
            pos = pygame.mouse.get_pos()
            if again_rect.collidepoint(pos):
                markers = []
                clicked = False
                pos = []
                player = 1
                winner = 0
                game_over = False
                for x in range(3):
                    row = [0]*3
                    markers.append(row)
    pygame.display.update()

pygame.quit()

for x in range(3):
    row = [0]*3
    markers.append(row)

def draw_markers():
    x_pos = 0
    for x in markers:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(screen, LIGHT_GREY, (x_pos * 200 + SPACE ,y_pos * 200 + 200 - SPACE), (x_pos * 200 + 200 - SPACE ,y_pos * 200 + SPACE), cross_width)
                pygame.draw.line(screen, LIGHT_GREY, (x_pos * 200 + SPACE, y_pos * 200 + SPACE), (x_pos * 200 + 200 - SPACE ,y_pos * 200 + 200 - SPACE), cross_width)
            if y == -1:
                pygame.draw.circle(screen, DARK_GREY, (x_pos * 200 + 100, y_pos * 200 + 100), circle_radius, circle_width)
            y_pos += 1
        x_pos += 1
#mainloop
run = True
while run:
    draw_board()
    draw_markers()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False
            pos = pygame.mouse.get_pos()
            mark_x = pos[0]
            mark_y = pos[1]
            if markers[mark_x // 200][mark_y // 200] == 0:
                markers[mark_x // 200][mark_y // 200] = player
                player *= -1
    pygame.display.update()

pygame.quit()

