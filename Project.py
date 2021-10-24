import pygame, sys
#Initialize Pygame
pygame.init() # เซตค่าเริ่มต้นโมดูลทั้งหมดที่จำเป็นสำหรับ pygame

WIDTH = 600  # เขียนตัวแปรในรูปแบบของค่าคงที่
HEIGHT = 600 # เก็บค่าที่เป็นตัวเลข ใช้ในการกำหนดขนาดหน้าจอของเกม
# สร้างหน้าจอสำหรับตัวเกม
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# สร้าง whileloop เพื่อให้ code รันต่อเนื่อง
while True:
    for event in pygame.event.get(): #ใช้ forloop ในการเช็คดูเหตุการณ์ต่างๆที่เกิดขึ้นภายในเกม
        if event.type == pygame.QUIT: # หากมีการกดปิดเกมให้สั่งปิด
            sys.exit()
