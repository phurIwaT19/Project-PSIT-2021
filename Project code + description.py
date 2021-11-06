import pygame, sys
#Initialize Pygame
pygame.init() # เซตค่าเริ่มต้นโมดูลทั้งหมดที่จำเป็นสำหรับ pygame

WIDTH = 600 # เขียนตัวแปรในรูปแบบของค่าคงที่
HEIGHT = 600 # เก็บค่าที่เป็นตัวเลข ใช้ในการกำหนดขนาดหน้าจอของเกม

screen = pygame.display.set_mode( (WIDTH, HEIGHT) ) # สร้างหน้าจอสำหรับตัวเกม
pygame.display.set_caption( 'TIC TAC TOE') # เขียนหัวข้อบนกรอบหน้าต่างของตัวเกม

#define variable
markers = []
clicked = False
positon = []

FPS = 60

def draw_board(): # ฟังก์ชั่นสำหรับใส่สี และเส้น
    #rgb = (red, green, blue)
    BG_COLOR = (102, 178, 255) # สีสำหรับ background
    LIGHT_PURPLE = (51, 153, 255) # สีสำหรับเส้นตาราง
    screen.fill( BG_COLOR )
    #Vertical ( แนวตั้ง )
    pygame.draw.line( screen, LIGHT_PURPLE, (200, 0), (200, 600), 20) #1
    pygame.draw.line( screen, LIGHT_PURPLE, (400, 0), (400, 600), 20) #2
    #Horizontal ( แนวนอน )
    pygame.draw.line( screen, LIGHT_PURPLE, (0, 200), (600, 200), 20) #1
    pygame.draw.line( screen, LIGHT_PURPLE, (0, 400), (600, 400), 20) #2

for x in range(3):
    row = [0]*3
    markers.append(row)

#mainloop
def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        draw_board()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                position = pygame.mouse.get_position()
                mark_x = position[0]
                mark_y = position[1]
                if markers[mark_x // 100]


        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()