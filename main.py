# Click Detect Challenge 
import pygame 
import random 

# Define colors 
RED = [255, 0, 0] 
GREEN = [0, 255, 0] 
BLACK = [0, 0, 0]  

# Circle Class 
class Circle():
    def __init__(self, x, y, w, h):  
        self.h = h
        self.w = w 
        self.x = x 
        self.y = y 
    def drawCircle(self, screen):
        pygame.draw.ellipse(screen, GREEN, [self.x, self.y, self.w, self.h], 2)  

# Rectangle 
class Rect():
    def __init__(self, x, y, w, h):
        self.x = x 
        self.y = y 
        self.w = w 
        self.h = h 
    def drawRect(self, screen):
        pygame.draw.rect(screen, RED, [self.x, self.y, self.w, self.h], 2)


# List of Circles 
circles = [] 
for i in range(10): 
    wHRan = random.randrange(30, 50)
    circles.append(Circle(random.randrange(0, 800), random.randrange(0, 600), wHRan, wHRan))  

# List of Rectangles 
rects = [] 
for i in range(10):
    wHRan = random.randrange(30, 50)
    rects.append(Rect(random.randrange(0, 800), random.randrange(0, 600), wHRan, wHRan))

# Mouse Collision  
def mouse_position():
    pos = pygame.mouse.get_pos() 
    mouse_x = pos[0]
    mouse_y = pos[1]
    return mouse_x, mouse_y   

def mouseCollision(rect):
   return mouse_position()[0] < rect.x + rect.w and mouse_position()[1] < rect.y + rect.h and mouse_position()[0] > rect.x and mouse_position()[1] > rect.y

def mouse_check(list):
    for i in range (len(list)):
        if mouseCollision(list[i]): 
            return i 
    return -1 

# Main function 
def main():
    pygame.init() 
    # Canvas
    size = (800, 600)
    screen = pygame.display.set_mode(size) 
    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock() 
    print(circles)
 
    # Main Program Loop 
    while not done:
        # Main event loop
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                done = True 
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if mouse_check(circles) != -1:
                    circles.pop(mouse_check(circles))  
                elif mouse_check(rects) != -1: 
                    pygame.quit() 
                    print("Game Over - You Lose.")
        
        screen.fill(BLACK)
        for i in range(len(circles)):
            circles[i].drawCircle(screen)  
        for i in range(len(rects)): 
            rects[i].drawRect(screen)
        pygame.display.flip() 
    
        # --- Limit frames
        clock.tick(60)

# Close window
pygame.quit() 

main()
