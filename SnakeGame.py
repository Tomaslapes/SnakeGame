import pygame

class cell:
    def __init__(self,width,height,color,position= (0,0),parent = None):
        self.width = width
        self.height = height
        self.color = color
        self.position = position
        self.nextPos = (0,0)
        self.parent = parent

    def calcPos(self,direction = (0,0)):
        if self.parent is not None:
            self. nextPos = self.parent.position
            return
        self.nextPos = tuple((self.position[0] + self.width*direction[0],self.position[1] + self.height*direction[1]))
        print(self.position)
        print(self.nextPos)

    def draw(self,surface):
        x_ = self.nextPos[0]-self.width/2
        y_ = self.nextPos[1]-self.height/2
        pygame.draw.rect(surface,self.color,(x_,y_,self.width,self.height))
        self.position = self.nextPos

def main():
    # initialize the pygame module
    pygame.init()
    # load and set the logo

    pygame.display.set_caption("minimal program")

    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((720, 480))

    # define a variable to control the main loop
    running = True
    testCell = cell(20,20,(71, 165, 74),(360,240))
    test2Cell = cell(20,20,(47, 96, 49),(360,240),parent = testCell)
    test3Cell = cell(20, 20, (47, 96, 49), (480, 220), parent=test2Cell)

    DIRECTION = (0,1)
    # main loop
    while running:
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

        # run the main function only if this module is executed as the main script
        testCell.calcPos(DIRECTION)
        test2Cell.calcPos(DIRECTION)
        test3Cell.calcPos(DIRECTION)
        testCell.draw(screen)
        test2Cell.draw(screen)
        test3Cell.draw(screen)
        pygame.display.update()
        screen.fill((0, 0, 0))
        pygame.time.wait(100)
        # (if you import this as a module then nothing is executed)


if __name__ == "__main__":
    # call the main function
    main()