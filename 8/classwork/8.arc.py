import pygame

# визначаємо константу затримки кадрів
# та інші константи
FPS = 60

WHITE = (255, 255, 255)  
ORANGE = (255, 150, 100)
BLUE = (0, 0, 255)
PINK = (230,50,230)
PI = 3.14
 
# ініціалізація та створення об'єктів
pygame.init()
# pygame.display.set_mode((600, 400))

screen = pygame.display.set_mode((640, 560), pygame.RESIZABLE)

pygame.display.set_caption("My first game")


done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done=True
    
    
    pygame.draw.arc(screen, WHITE, (10, 50, 280, 100), 0, PI)
    pygame.draw.arc(screen, PINK, (50, 30, 200, 150), PI, 2*PI, 3)
    
    
    pygame.display.update()
    clock.tick(FPS)