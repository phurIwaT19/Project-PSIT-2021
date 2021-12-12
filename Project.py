import pygame, random

pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption( 'TIC TAC TOE' )

#define variable
markers = []
clicked = False
pos = []
player = 1
winner = 0
draw = False
game_over = False
playTwoPlayer = True
manu = True
#define font
font = pygame.font.SysFont(None, 50)
font_2 = pygame.font.SysFont(None, 40)

#creat rect
again_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2, 200, 50)
manu_rect_P1VSP2 = pygame.Rect(WIDTH // 2, HEIGHT // 2, 200, 50)
manu_rect_P1VSAI = pygame.Rect(WIDTH // 2 - 200, HEIGHT // 2, 200, 50)

#วาดตาราง 9 ช่อง
def draw_board():
    bg_color = (5, 5, 23)
    line_color = (16, 16, 65)
    screen.fill( bg_color ) #สีพื้นหลังจอ
    #Vertical
    pygame.draw.line( screen, line_color, (200, 0), (200, 600), 20) #1
    pygame.draw.line( screen, line_color, (400, 0), (400, 600), 20) #2
    #Horizontal
    pygame.draw.line( screen, line_color, (0, 200), (600, 200), 20) #1
    pygame.draw.line( screen, line_color, (0, 400), (600, 400), 20) #2

markers = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def draw_markers():
    cross_width = 20
    circle_width = 15
    circle_radius = 60
    x_color = (192, 192, 192)
    o_color = (165, 56, 96)
    space = 50
    x_pos = 0 
    for x in markers:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(screen, x_color, (x_pos * 200 + space ,y_pos * 200 + 200 - space), (x_pos * 200 + 200 - space ,y_pos * 200 + space), cross_width)
                pygame.draw.line(screen, x_color, (x_pos * 200 + space, y_pos * 200 + space), (x_pos * 200 + 200 - space ,y_pos * 200 + 200 - space), cross_width)
            if y == -1:
                pygame.draw.circle(screen, o_color, (x_pos * 200 + 100, y_pos * 200 + 100), circle_radius, circle_width)
            y_pos += 1
        x_pos += 1
def check_winner():
    global winner
    global game_over
    global draw
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
    if game_over == False and 0 not in markers[0] and 0 not in markers[1] and 0 not in markers[2]:
            draw = True

def draw_manu(winner):
    text_color = (32, 36, 154)
    box_color = (232, 191, 30)
    text_playagain = (32, 36, 154)
    box_playagain = (250, 227, 132)
    if game_over == True:
        win_text = 'Player ' + str(winner) + " wins!"
    elif draw == True and game_over != True:
        win_text = "      DRAW!!!"
    elif game_over != True and manu == True:
        win_text = "    • START •"
    win_img = font.render(win_text, True, text_color)
    pygame.draw.rect(screen, box_color, (WIDTH // 2 - 150, HEIGHT // 2 - 100, 300, 80), 40, 20)
    screen.blit(win_img, (WIDTH // 2 - 115, HEIGHT // 2 - 75))
    if manu == True:
        #P1VSAI
        manu_text1 = 'P1 VS AI'
        manu_img1 = font_2.render(manu_text1, True, text_playagain)
        pygame.draw.rect(screen, box_playagain, manu_rect_P1VSAI, 25, 20)
        screen.blit(manu_img1, (WIDTH // 2 - 160, HEIGHT // 2 + 12))
        #P1VSP2
        manu_text2 = 'P1 VS P2'
        manu_img2 = font_2.render(manu_text2, True, text_playagain)
        pygame.draw.rect(screen, box_playagain, manu_rect_P1VSP2, 25, 20)
        screen.blit(manu_img2, (WIDTH // 2 + 45, HEIGHT // 2 + 12))
    else:
        again_text = 'Play again'
        again_img = font_2.render(again_text, True, text_playagain)
        pygame.draw.rect(screen, box_playagain, again_rect, 25, 20)
        screen.blit(again_img, (WIDTH // 2 - 70, HEIGHT // 2 + 10))

#mainloop
run = True
started = True

def start():
    global playTwoPlayer
    global manu
    global clicked
    global started
    global event
    while started:
        draw_board()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                started = False
        if manu == True:
                draw_manu(winner)
                if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                    clicked = True
                if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                    clicked = False
                    pos = pygame.mouse.get_pos()
                    if manu_rect_P1VSAI.collidepoint(pos):
                        playTwoPlayer = False
                        manu = False
                        return started == False
                    if manu_rect_P1VSP2.collidepoint(pos):
                        playTwoPlayer = True
                        manu = False
                        return started == False
        pygame.display.update()

while run:
    if started == True:
        started = start()
    else:
        draw_board()
        draw_markers()
    #เปิดปิดหน้าต่าง
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if game_over == 0:
            if playTwoPlayer == True:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clicked = True
                    pos = pygame.mouse.get_pos()
                    mark_x = pos[0]
                    mark_y = pos[1]
                    if markers[mark_x // 200][mark_y // 200] == 0: #เท่ากับ 0 หมายถึงยังไม่ได้คลิก
                        markers[mark_x // 200][mark_y // 200] = player
                        player *= -1 #เป็นการสลับผู้เล่นระหว่าง 1 กับ -1
                        check_winner()
            elif playTwoPlayer == False:
                check, modify = False, False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clicked = True
                    pos = pygame.mouse.get_pos()
                    mark_x = pos[0]
                    mark_y = pos[1]
                    if markers[mark_x // 200][mark_y // 200] == 0: #เท่ากับ 0 หมายถึงยังไม่ได้คลิก
                        markers[mark_x // 200][mark_y // 200] = player
                        for i in range(3):
                            convert = random.choice(markers)
                            if modify == True:
                                break
                            if 0 in convert:
                                while True:
                                    if check == True:
                                        break
                                    keep = random.randint(0, 2)
                                    if convert[keep] == 0:
                                        convert[keep] = player*-1
                                        check = True
                                        modify = True
                        check_winner()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                pos = []
                clicked = False
                player = 1
                winner = 0
                game_over, draw = False, False
                markers = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                manu = True
                started = True
            if event.key == pygame.K_1:
                playTwoPlayer = False
            if event.key == pygame.K_2:
                playTwoPlayer = True
    if manu == True:
            draw_manu(winner)
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos()
                if manu_rect_P1VSAI.collidepoint(pos):
                    playTwoPlayer = False
                    manu = False
                if manu_rect_P1VSP2.collidepoint(pos):
                    playTwoPlayer = True
                    manu = False

    if game_over == True or (draw == True and game_over != True):
        draw_manu(winner)
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False
            pos = pygame.mouse.get_pos()
            if again_rect.collidepoint(pos):
                pos = []
                clicked = False
                player = 1
                winner = 0
                markers = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                game_over, draw = False, False

    pygame.display.update()

pygame.quit()
