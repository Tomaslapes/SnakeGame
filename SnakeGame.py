import pygame
import random
import pygame.freetype

CHEATS = True

class cell:
    def __init__(self,width,height,color,position= (0,0),parent = None):
        self.width = width
        self.height = height
        self.color = color
        self.position = position
        self.nextPos = (0,0)
        self.parent = parent
        self.rect = None

    def calcPos(self,direction = (0,0)):
        if self.parent is not None: # following cell logic
            self. nextPos = self.parent.position
            return
        # Main head logic
        self.nextPos = tuple((self.position[0] + self.width*direction[0],self.position[1] + self.height*direction[1]))
        print(self.position)
        print(self.nextPos)

    def draw(self,surface):
        x_ = self.nextPos[0]-self.width/2
        y_ = self.nextPos[1]-self.height/2
        self. rect = pygame.draw.rect(surface,self.color,(x_,y_,self.width,self.height))
        self.position = self.nextPos

class pickup:
    def __init__(self,size,color,surface, location = (0,0)):
        self.size = size
        self.color = color
        self.sound = None
        self.location = location
        self.rect = pygame.draw.rect(surface,self.color,(self.location[0],self.location[1],self.size,self.size))

    def getLoc(self):
        return self.location

    def draw(self,surface):
        self.rect = pygame.draw.rect(surface,self.color,(self.location[0],self.location[1],self.size,self.size))

def pause(screen,screenWidth,screenHeight):
    paused = True
    gameOverText = pygame.freetype.Font("airstrikeacad.ttf", 86)
    gameOverText.render_to(screen,(screenWidth/2-245,screenHeight/2-25),"Game OVER",(255, 255, 255))
    pygame.display.update()
    while paused: 
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                paused = False
                return False


def main():
    # initialize the pygame module
    pygame.init()
    # load and set the font
    GAME_FONT = pygame.freetype.Font("airstrikeacad.ttf", 64)
    scoreText = pygame.freetype.Font("airstrikeacad.ttf", 32)
    pygame.display.set_caption("Snake")

    # create a surface on screen that has the size of 240 x 180
    screenWidth = 720
    screenHeight = 480
    screen = pygame.display.set_mode((screenWidth, screenHeight))

    # define a variable to control the main loop
    running = True
    squareSize = 20
    cellList = []
    pickupList = []
    testCell = cell(squareSize,squareSize,(71, 165, 74),(350,230))
    test2Cell = cell(squareSize,squareSize,(47, 96, 49),(0,250),parent = testCell)
    test3Cell = cell(squareSize, squareSize, (47, 96, 49), (350, 0), parent=test2Cell)
    cellList.append(testCell)
    cellList.append(test2Cell)
    cellList.append(test3Cell)
    DIRECTION = (0,1)
    SCORE = 0
    # main loop
    countDown = 0
    while running:
        if countDown > 50:
            pickupList.append(pickup(10,(155,10,10),screen,(random.randint(10,screenWidth-10),random.randint(10,screenHeight-10))))
            countDown = 0
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            if event.type == pygame.KEYDOWN:
                if(event.key == pygame.K_a or event.key == pygame.K_LEFT):
                    DIRECTION = (-1,0)
                if (event.key == pygame.K_s or event.key == pygame.K_DOWN):
                    DIRECTION = (0, 1)
                if (event.key == pygame.K_d or event.key == pygame.K_RIGHT):
                    DIRECTION = (1, 0)
                if (event.key == pygame.K_w or event.key == pygame.K_UP):
                    DIRECTION = (0, -1)
                if event.key ==pygame.K_g and CHEATS:
                    cellList.append(cell(squareSize, squareSize, (47, 96, 49), (480, 220), parent=cellList[-1]))
        # run the main function only if this module is executed as the main script
        for pickups in pickupList:
            if cellList[0].rect.colliderect(pickups):
                pickupList.remove(pickups)
                cellList.append(cell(squareSize, squareSize, (47, 96, 49), (480, 220), parent=cellList[-1]))
                SCORE += 1
            pickups.draw(screen)

        for items in cellList:
            items.calcPos(DIRECTION)

        for items in cellList:
            items.draw(screen)
            if cellList[0].rect.colliderect(items) and items != cellList[0]:
                running = pause(screen,screenWidth,screenHeight)


        GAME_FONT.render_to(screen, (120, 20), str(SCORE), (255, 255, 255))
        scoreText.render_to(screen,(0,30),"SCORE:", (255, 255, 255))
        
        pygame.display.update()
        screen.fill((0, 0, 0))
        countDown += 1 + random.randint(-1,2)
        pygame.time.wait(80)
        # (if you import this as a module then nothing is executed)


if __name__ == "__main__":
    # call the main function
    main()