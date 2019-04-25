# project_AI_class
In order to design a UI interface for our Gobang game, we have learnt how to use pygame. According to the source, at first, we should need use some codes to initial the framework of game.
import pyagme
from pygame.locals import *
from sys import exit
First, the source author initials the widow and gives necessary parameters like resolution ratio and color and show the game name on the title. 
pygame.init()
screen = pygame.display.set_mode((1024,768),0, 32 )
pygame.display.set_caption (Gomoku)
imagePath = 'xxx'
imBackground = pygame.image.load(imagePath+'background.jpg').convert()
imChessboard = pygame.image.load(imagePath+'chessboard.jpg').convert()
imBlackPiece = pygame.image.load(imagePath+'blackpiece.png').convert_alpha()
imWhitePiece = pygame.image.load(imagePath+'whitepiece.png').convert_alpha()
screen.blit(imBackground, (0,0))  ##draw the chessboard 
chessboard_start_x =(1024-(1024-540)/2-1
chessboard_start_y = 768-(768-540)/2-1
screen.blit(imChessboard,(241,113))    ##put the chessboard in the center
Second, the function convert () can change the picture into the Surface type, convert_aplha can do the same thing but this function keeps the value of alpha, so that we can realize some part of picture are transparent and get a circle chess. 
Using bits function to transfer the Surface object. Through these steps, the author has got an interface for chessboard. 
 
Next, how dose the computer know whether the player has put the chess which means the player has pushed the button? In pygame,  pygame.mouse can record the current motion of mouse. When we set the correct mode, the computer will record the mouse motion. When player click the button, the pygame.MouseButtonDown event will happen. In contrary, if player release the button, pygame.MouseButtonUp event will engage.
The author use these codes to judge the mouse status:
 pressed_mouse = pygame.mouse.get_pressed()
And then, getting the position and coordinate of mouse down event, 
if pressed_mouse[0]:
        pressed_x,pressed_y = pygame.mouse.get_pos()

At last, we should know what the chess position is in the chessboard. 
mouse_chessboard_x,mouse_chessboard_y = pressed_x-chessboard_start_x,pressed_y-chessboard_start_y

And calculate the closest point to the mouse click down position. 
d = (518-22)/14
i_tmp,j_tmp = round((mouse_chessboard_y-22)/d)+1,round((mouse_chessboard_x-22)/d)+1

Work out the chess position in the chessboard
piece_chessboard_x,piece_chessboard_y = 22+(j-1)*d,22+(i-1)*d  [1]

When the computer finishes them all, it is the computer turn to play.
For our project, we set the MouseButtonDown event is player put the chess, and MouseButtonUp event is player has already finished his round. Each round, computer should do these steps and use the score system we designed to determine where the next white chess should be put. 

Reference
[1]https://blog.csdn.net/qq_25072387/article/details/77478043


After entering the game, there are three buttons which links the the level of computer. Three buttons shows on the interface. After choosing in level, a game is ready to begin. If the player thinks it is difficult to win, he can click the "back" button and return to the previous interface and choose a new level. 
