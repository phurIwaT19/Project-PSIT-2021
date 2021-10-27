import pygame, sys
#Initialize Pygame
pygame.init() # เซตค่าเริ่มต้นโมดูลทั้งหมดที่จำเป็นสำหรับ pygame

WIDTH = 600  # เขียนตัวแปรในรูปแบบของค่าคงที่
HEIGHT = 600 # เก็บค่าที่เป็นตัวเลข ใช้ในการกำหนดขนาดหน้าจอของเกม
# สร้างหน้าจอสำหรับตัวเกม
screen = pygame.display.set_mode((WIDTH, HEIGHT))

FPS = 60

def draw_board():
    screen.fill( BG_COLOR )
    #Vertical
    pygame.draw.line( screen, LIGHT_PURPLE, (200, 0), (200, 600), 20) #1
    pygame.draw.line( screen, LIGHT_PURPLE, (400, 0), (400, 600), 20) #2
    #Horizontal
    pygame.draw.line( screen, LIGHT_PURPLE, (0, 200), (600, 200), 20) #1
    pygame.draw.line( screen, LIGHT_PURPLE, (0, 400), (600, 400), 20) #2
    pygame.display.update()

# สร้าง whileloop เพื่อให้ code รันต่อเนื่อง
def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        for event in pygame.event.get(): #ใช้ forloop ในการเช็คดูเหตุการณ์ต่างๆที่เกิดขึ้นภายในเกม
            if event.type == pygame.QUIT: # หากมีการกดปิดเกมให้สั่งปิด
                run = False
        draw_board()
    pygame.quit()

