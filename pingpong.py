from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()        
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < window_height - 80:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < window_height - 80:
            self.rect.y += self.speed
                    
font.init()
font = font.Font(None, 35)
perdiste1 = font.render('Jugador 1 perdió!', True, (180, 0, 0))
perdiste2 = font.render('Jugador 2 perdió!', True, (180, 0, 0))

raqueta1 = Player('raqueta.png', 30, 200, 4, 50, 150)
raqueta2 = Player('raqueta.png', 520, 200, 4, 50, 150)
pelota = GameSprite('ball.png', 200, 200, 4, 50, 50)


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

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(back)          
        raqueta1.update_l()
        raqueta2.update_r()
        pelota.rect.x += speed_x
        pelota.rect.y += speed_y

    if sprite.collide_rect(raqueta1, pelota) or sprite.collide_rect(raqueta2, pelota):
        speed_x *= -1
        speed_y *= 1

    # Si la pelota toca el borde superior o inferior, invierte su dirección vertical
    if pelota.rect.y > window_height - 50 or pelota.rect.y < 0:
        speed_y *= -1

    # Si la pelota toca el borde izquierdo, termina el juego
    if pelota.rect.x < 0 :
        finish = True
        window.blit(perdiste1, (200, 200))
        game = True

    # Si la pelota toca el borde derecho, termina el juego
    if pelota.rect.x > window_width:
        finish = True
        window.blit(perdiste2, (200, 200))
        game = True
        
    raqueta1.reset()
    raqueta2.reset()   
    pelota.reset()

    display.update()
    clock.tick(FPS)
