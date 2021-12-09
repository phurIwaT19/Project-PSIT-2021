import pygame
#Initialize Pygame
pygame.init() # เซตค่าเริ่มต้นโมดูลทั้งหมดที่จำเป็นสำหรับ pygame

WIDTH = 600 # เขียนตัวแปรในรูปแบบของค่าคงที่
HEIGHT = 600 # เก็บค่าที่เป็นตัวเลข ใช้ในการกำหนดขนาดหน้าจอของเกม

screen = pygame.display.set_mode( (WIDTH, HEIGHT) ) # สร้างหน้าจอสำหรับตัวเกม
pygame.display.set_caption( 'TIC TAC TOE') # เขียนหัวข้อบนกรอบหน้าต่างของตัวเกม

#ตัวแปรต่างๆที่เอาไว้ใช้
markers, positon = list(), list()
clicked = False
player = 1
winner = 0
game_over = False

#เรียกใช้ font              (ชื่อฟอนต์, ขนาด)
font = pygame.font.SysFont(None, 50)
font_2 = pygame.font.SysFont(None, 40)

#creat play again rect
again_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2, 200, 50)

def draw_board(): # ฟังก์ชั่นสำหรับใส่สี และเส้น
    #rgb = (red, green, blue)
    BG_COLOR = (102, 178, 255) # สีสำหรับ background
    LIGHT_PURPLE = (51, 153, 255) # สีสำหรับเส้นตาราง
    screen.fill( BG_COLOR ) # คำสั่งสำหรับใส่ background ลงไปในบอร์ด หรือหน้าต่างของตัวเกม

    #คำสั่งสำหรับวาดเส้น 
    #pygame.draw.line(หน้าต่างที่จะวาดเส้นลงไป, สีของเส้น, ตำแหน่งเริ่มต้นของเส้น, ตำแหน่งสิ้นสุดของเส้น, ขนาดของเส้น)
    #Vertical(แนวตั้ง)
    pygame.draw.line( screen, LIGHT_PURPLE, (200, 0), (200, 600), 20) #1
    pygame.draw.line( screen, LIGHT_PURPLE, (400, 0), (400, 600), 20) #2
    #Horizontal (แนวนอน)
    pygame.draw.line( screen, LIGHT_PURPLE, (0, 200), (600, 200), 20) #1
    pygame.draw.line( screen, LIGHT_PURPLE, (0, 400), (600, 400), 20) #2

#สร้าง list เอาไว้ตรวจสอบการแสดงของสัญลักษณ์ X กับ O ของแต่ละผู้เล่น
markers = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#list ที่ได้ >> [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def draw_markers():#สร้างฟังก์ชั่นสำหรับวาดตัว X O ลงบนบอร์ด มี x_pos กับ y_pos เป็นตัวระบุตำแหน่ง
    cross_width = 20
    circle_width = 15
    circle_radius = 60
    LIGHT_GREY = (192, 192, 192)
    DARK_GREY = (96, 96, 96)
    SPACE = 50
    x_pos = 0
    for x in markers:#ใช้ค่าใน list ที่ได้จาก marker เป็นตัวเช็ค
        y_pos = 0
        for y in x:#โดยกำหนดให้ ถ้า y เท่า 1 จะวาดตัว X  ส่วนถ้า y เท่า -1 จะวาดตัว O
            if y == 1:
                pygame.draw.line(screen, LIGHT_GREY, (x_pos * 200 + SPACE ,y_pos * 200 + 200 - SPACE), (x_pos * 200 + 200 - SPACE ,y_pos * 200 + SPACE), cross_width)
                pygame.draw.line(screen, LIGHT_GREY, (x_pos * 200 + SPACE, y_pos * 200 + SPACE), (x_pos * 200 + 200 - SPACE ,y_pos * 200 + 200 - SPACE), cross_width)
            if y == -1:
                pygame.draw.circle(screen, DARK_GREY, (x_pos * 200 + 100, y_pos * 200 + 100), circle_radius, circle_width)
            y_pos += 1 #บวกเพิ่มเพื่อเปลี่ยนตำแหน่ง
        x_pos += 1

def check_winner():#ฟังก์ชั่นสำหรับเงื่อนไขการชนะ และหาผู้ชนะ
    global winner #ทำให้ตัวแปร winner และ game_over เป็นตัวแปรแบบ global >>>ทำให้สามารถนำตัวแปรที่กำหนดไว้ในฟังก์ชั่น นำออกไปใช้ภายนอกได้
    global game_over #ค่าของตัวแปรในฟังก์ชั่นจะไปแทนค่าของตัวแปรที่เหมือนกันของตัวแปรภายนอก
    y_pos = 0
    for x in markers:#ไล่ทุกตัวใน list เพื่อ check
        # if sum(x) จะเป็นการเช็คในแนวตั้งโดยตรง ก็คือตัว listใน list [[1,1,1]<<<column,[],[]]
        if sum(x) == 3:
            winner = 1
            game_over = True
        if sum(x) == -3:
            winner = 2
            game_over = True
        #เช็กแนวนอน [[1,0,0],[1,0,0],[1,0,0]] <<<row
        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == 3:
            winner = 1
            game_over = True
        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == -3:
            winner = 2
            game_over = True
        y_pos += 1
    #เช็คแนวแทยง [[1,0,0],[0,1,0],[0,0,1]] <<<cross
    if markers[0][0] + markers[1][1] + markers[2][2] == 3 or markers[2][0] + markers[1][1] + markers[0][2] == 3:
        winner = 1
        game_over = True
    if markers[0][0] + markers[1][1] + markers[2][2] == -3 or markers[2][0] + markers[1][1] + markers[0][2] == -3:
        winner = 2
        game_over = True
def draw_winner(winner):#ฟังก์ชั่นสร้างกรอบแสดงผู้ชนะ และปุ่มเริ่มเล่นใหม่
    blue = (0, 0, 255)
    green = (0, 255, 0)
    win_text = 'Player ' + str(winner) + " wins!"
    win_img = font.render(win_text, True, blue) #คำสั่งในการโหลดหรือเรียกใช้ฟอนต์ >> font.render(คำที่จะแสดง, ลบรอยหยัก, สี)
    pygame.draw.rect(screen, green, (WIDTH // 2 - 150, HEIGHT // 2 - 100, 300, 80), 40, 20) #ใช้ module draw ของ pygame สร้างสี่เหลี่ยมเป็น background
    screen.blit(win_img, (WIDTH // 2 - 115, HEIGHT // 2 - 75)) #ลงฟอนต์
    #สร้างปุ่มสำหรับเล่นอีกครั้ง
    again_text = 'Play again'
    again_img = font_2.render(again_text, True, blue)
    pygame.draw.rect(screen, green, again_rect, 25, 20)
    screen.blit(again_img, (WIDTH // 2 - 70, HEIGHT // 2 + 10))

run = True
# สร้าง whileloop เพื่อให้ code รันต่อเนื่อง
while run:
    draw_board()#เรียกใช้ฟังก์ชันสำหรับแสดงบอร์ดของเกม
    draw_markers()#เรียกใช้ฟังก์ชันสำหรับการแสดง X และ O
    for event in pygame.event.get():#ใช้ forloop ในการเช็คดูเหตุการณ์ต่างๆที่เกิดขึ้นภายในเกม
        if event.type == pygame.QUIT:# หากมีการกดปิดเกมให้สั่งปิด (โดยการให้ออกจาก while loop)
            run = False
        if game_over == 0:
            # เมื่อคลิกเมาส์ลงไปบนเกมให้เปลี่ยนสถานนะ clicked เป็น True เพื่อนำไปเข้าเงื่อนไขเวลาปล่อยปุ่มที่คลิกเมาส์
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            # เมื่อปล่อยปุ่มคลิกเมาส์ จะเข้าเงื่อนไขนี้
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False #reset รอบการคลิกเมาส์
                position = pygame.mouse.get_pos()#เก็บค่าตำแหน่งของจุดที่คลิกเมาส์ในรูปแบบ (x, y)
                mark_x = position[0] #เก็บค่าตำแหน่ง x ของจุดที่คลิก
                mark_y = position[1] #เก็บค่าตำแหน่ง y ของจุดที่คลิก
                #เช็คตำแหน่งว่าตำแหน่งนั้นถูกคลิกไปหรือยัง
                if markers[mark_x // 200][mark_y // 200] == 0: #หากเป็น 0 คือยังไม่ถูกคลิก
                    markers[mark_x // 200][mark_y // 200] = player #เปลี่ยนสถานนะว่าตำแหน่งนั้นถูกคลิกแล้ว
                    player *= -1 #เปลี่ยนสถานะจาก 1 เป็น -1 และจาก -1 เป็น 1 เพื่อนำไปใช้ในเงื่อนไขของฟังก์ชั่น draw_markers()
                    check_winner()
    if game_over == True:
        draw_winner(winner)
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False
            pos = pygame.mouse.get_pos()
            if again_rect.collidepoint(pos):
                markers, pos = [], []
                clicked = False
                player = 1
                winner = 0
                game_over = False
                markers = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
     
    pygame.display.update()#อัพเดทสิ่งที่ใส่เข้าไปจากโค้ดไปยังหน้าจอแสดงผล

pygame.quit()#คำสั่งปิดการทำงานของ pygame
