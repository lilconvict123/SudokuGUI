import pygame
pygame.init()

window = pygame.display.set_mode((450,500))
pygame.display.set_caption("Sudoku")
class Cell:

    def __init__(self,x,y,number):
        self.x = x
        self.y = y
        self.number = number
        self.selected = False
    
    def draw(self):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(str(self.number), True, (0,0,0), (255,255,255))

        if self.selected:
            pygame.draw.rect(window,(0,0,255),(self.x+3,self.y+3,45,45))
        else:
            pygame.draw.rect(window,(255,255,255),(self.x+3,self.y+3,45,45))

        if self.number != None:
            window.blit(text, (self.x+16,self.y+14))
            
def generateCellObjects():

    y = -50;
    for row in range(9):
        currentRow = []
        x = -50
        y += 50
        for column in range(9):
            x += 50
            currentCell = Cell(x,y,None)
            currentRow.append(currentCell)
            if column == 8:
                cellArray.append(currentRow)
            
def drawBoard():

    y = 0
    for count in range(10):
        if count % 3 == 0:
            pygame.draw.line(window,(0,0,0),(0,y),(450,y),6)
        else:
            pygame.draw.line(window,(0,0,0),(0,y),(450,y))
        y += 50
    x = 0
    for count in range(10):
        if count % 3 == 0:
            pygame.draw.line(window,(0,0,0),(x,0),(x,450),6)
        else:
            pygame.draw.line(window,(0,0,0),(x,0),(x,450))

        x += 50

def iterateCellArray():
    for row in cellArray:
        for item in row:
            item.draw()

def changeCell(coordinates,inputNumber):
    
     if coordinates[1] > 450:
         return
     x = coordinates[0] // 50
     y = coordinates[1] // 50
     cellArray[y][x].number = inputNumber
     cellArray[y][x].selected = False

def changeCellColour(coordinates):
     unselectAll()
     if coordinates[1] > 450:
         return
     x = coordinates[0] // 50
     y = coordinates[1] // 50
     cellArray[y][x].selected = True
    

def generateSolveButton():
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render("Solve",True,(0,0,0),(255,255,255))
    window.blit(text,(185,457))

def unselectAll():
    for row in cellArray:
        for item in row:
            item.selected = False

def updateScreen():
    window.fill((255,255,255))
    drawBoard()
    generateSolveButton()
    iterateCellArray()
    pygame.display.update()



cellArray = []
generateCellObjects()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False;
        if pygame.mouse.get_pressed()[0]:
            coordinates = pygame.mouse.get_pos()
            changeCellColour(coordinates)
        if pygame.key.get_pressed()[pygame.K_0]:
            changeCell(coordinates,0)
        if pygame.key.get_pressed()[pygame.K_1]:
            changeCell(coordinates,1)
        if pygame.key.get_pressed()[pygame.K_2]:
            changeCell(coordinates,2)
        if pygame.key.get_pressed()[pygame.K_3]:
            changeCell(coordinates,3)
        if pygame.key.get_pressed()[pygame.K_4]:
            changeCell(coordinates,4)
        if pygame.key.get_pressed()[pygame.K_5]:
            changeCell(coordinates,5)
        if pygame.key.get_pressed()[pygame.K_6]:
            changeCell(coordinates,6)
        if pygame.key.get_pressed()[pygame.K_7]:
            changeCell(coordinates,7)
        if pygame.key.get_pressed()[pygame.K_8]:
            changeCell(coordinates,8)
        if pygame.key.get_pressed()[pygame.K_9]:
            changeCell(coordinates,9)
    updateScreen()
pygame.quit()