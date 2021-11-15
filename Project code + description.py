import pygame, sys
#Initialize Pygame
pygame.init() # เซตค่าเริ่มต้นโมดูลทั้งหมดที่จำเป็นสำหรับ pygame

WIDTH = 600 # เขียนตัวแปรในรูปแบบของค่าคงที่
HEIGHT = 600 # เก็บค่าที่เป็นตัวเลข ใช้ในการกำหนดขนาดหน้าจอของเกม

screen = pygame.display.set_mode( (WIDTH, HEIGHT) ) # สร้างหน้าจอสำหรับตัวเกม
pygame.display.set_caption( 'TIC TAC TOE') # เขียนหัวข้อบนกรอบหน้าต่างของตัวเกม

#ตัวแปรต่างๆที่เอาไว้ใช้
cross_width = 20
circle_width = 15
circle_radius = 60
markers = []
clicked = False
positon = []
player = 1
#สี
LIGHT_GREY = (192, 192, 192)
DARK_GREY = (96, 96, 96)
SPACE = 50

FPS = 60

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

#สร้าง list ของแถวตาราง xo
for x in range(3):
    row = [0]*3
    markers.append(row)
    print(markers)
#ตารางที่ได้ >> [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#ตารางนี้จะเอาไว้ตรวจสอบการแสดงของสัญลักษณ์ X กับ O ของแต่ละผู้เล่น

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

run = True
# สร้าง whileloop เพื่อให้ code รันต่อเนื่อง
while run:
    draw_board()
    draw_markers()
    for event in pygame.event.get():#ใช้ forloop ในการเช็คดูเหตุการณ์ต่างๆที่เกิดขึ้นภายในเกม
        if event.type == pygame.QUIT:# หากมีการกดปิดเกมให้สั่งปิด (โดยการให้ออกจาก while loop)
            run = False
        # เมื่อคลิกเมาส์ลงไปบนเกมให้เปลี่ยนสถานนะ clicked เป็น True เพื่อนำไปเข้าเงื่อนไขเวลาปล่อยปุ่มที่คลิกเมาส์
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        # เมื่อปล่อยปุ่มคลิกเมาส์ จะเข้าเงื่อนไขนี้
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False #reset รอบการคลิกเมาส์
            position = pygame.mouse.get_pos()#เก็บค่าตำแหน่งของจุดที่คลิกเมาส์ในรูปแบบ (x, y)
            mark_x = position[0]#เก็บค่าตำแหน่ง x ของจุดที่คลิก
            mark_y = position[1]#เก็บค่าตำแหน่ง y ของจุดที่คลิก
            #
            if markers[mark_x // 200][mark_y // 200] == 0:
                markers[mark_x // 200][mark_y // 200] = player
                player *= -1

    pygame.display.update()#อัพเดทสิ่งที่ใส่เข้าไปจากโค้ดไปยังหน้าจอแสดงผล
pygame.quit()#คำสั่งปิดการทำงานของ pygame
