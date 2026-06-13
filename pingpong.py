from pygame import *

#escena del videojuego: 
back = (200, 255, 255) #Fondo azul claro
window_width = 600
window_height = 500
window = display.set_mode((window_width, window_height)) 
window.fill(back)

game = True 
finish = False 
clock = time.Clock() 
FPS = 60 

while game:
    
    display.update()
    clock.tick(FPS)



