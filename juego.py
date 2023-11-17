import pygame
import random
import math
import sys
import os

#Iniciar pygame
pygame.init()

#Establece el  tamaño de la pantalla
screen_width = 800
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))

#Funcion para obtener la ruta de los recursos
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)
    
#Cargar imagen de fondo
assets_background= resource_path('assets/imagenes juego nave/background.png')
background = pygame.image.load(assets_background)

#cargar icono de ventana
assets_icon = resource_path('assets/imagenes juego nave/ufo.png')
icon = pygame.image.load(assets_icon)

#cargar sonido de fondo
assets_sound = resource_path('assets/audios/background_music.mp3')
background_sound = pygame.mixer.music.load(assets_sound) 


#Cargar imagen del jugador 
assets_playerimg = resource_path('assets/imagenes juego nave/space-invaders.png')
playerimg = pygame.image.load(assets_playerimg)
      
#Cargar imagen  de bala
assets_bulletimg = resource_path('assets/imagenes juego nave/bullet.png')
bulletimg = pygame.image.load(assets_bulletimg)

#cargar fuente para texto  de game over 
assets_over_font = resource_path('assets/fonts/RAVIE.TTF')
over_font = pygame.font.Font(assets_over_font, 60)

#cargar funte para texto de puntaje 
assets_font = resource_path('assets/fonts/comicbd.ttf')
font = pygame.font.Font(assets_font, 32)

#Establecer titulo de ventana 
pygame.display.set_caption('Ataque espacial')

#Establecer icono de ventana
pygame.display.set_icon(icon)

#Reproducir fondo en loop
pygame.mixer.music.play(-1)

#crear reloj para controlar la velocidad del juego
clock = pygame.time.Clock()

#Posicion inicial del jugador 
playerX = 370
playerY = 470
playerx_change = 0
playery_change = 0


#Lista de posiciones de los enemigos 
enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
no_of_enemies =10
 
#Varialbes para guardar posisciones de los enemigos 
for i in range(no_of_enemies):
    #carga imagen del enemigo 1
    enemy1 = resource_path('assets/imagenes juego nave/enemy1.png')
    enemyimg.append(pygame.image.load(enemy1))
    #carga imagen del enemigo 2 
    enemy2 = resource_path('assets/imagenes juego nave/enemy2.png')
    enemyimg.append(pygame.image.load(enemy2))
    
    #Asignacion de posicion aleatoria en X y Y para el enemigo 
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(0,150))
    
    #Estableciendo la velocidad del movimiennto del enemigo en X y Y
    enemyX_change.append(5)
    enemyY_change.append(20)
    
    #Inicio de las  variables para guardar la posicion de la bala 
    bulletX = 0
    bulletY = 480
    bulletX_change = 10
    bulletY_change = 10
    bullet_state = "ready"
    
    #Iniciando puntuacion en cero 
    score = 0
    
    #Fuincion para mostrar la puntuacion en la pantalla
    def show_score():
        score_value = font.render("SCORE " + str(score), True, (255, 255, 255))
        screen.blit(score_value, (10, 10))
        
    #Funcion para dibujar  al jugador en la pantalla 
    def player(x , y):
        screen.blit(playerimg, (x , y))
        
    #Funcion para dibujar al enemigo en la pantalla
    def enemy(x, y , i):
        screen.blit(enemyimg[i], (x , y))
        
    #Funcion para disparar la bala
    def fire_bullet(x, y):
        global bullet_state
        
        bullet_state = "fire"
        screen.blit(bulletimg, (x + 16, y + 10))
    
    #Funcion para ver si ha habido una colision entre la bala y el enemigo
    def isCollision(enemyX, enemyY, bulletX, bulletY):
        enemy_rect = pygame.Rect(enemyX, enemyY, enemyimg[i].get_width(), enemyimg[i].get_height())
        bullet_rect = pygame.Rect(bulletX, bulletY, bulletimg.get_width(), bulletimg.get_height())
        return bullet_rect.colliderect(enemy_rect)
    
    def show_pause_screen():
     # Esta función muestra la pantalla de pausa.
    # Puedes añadir aquí todo lo que quieras que aparezca en la pantalla de pausa, como opciones para guardar y cargar el juego, ajustar las opciones, etc.
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:  # Presiona la tecla 'p' para pausar y despausar el juego
                        paused = False
            #para dibujar la pantalla de pausa, como texto e imágenes
            font = pygame.font.Font(None, 36)  # Elige la fuente y el tamaño del texto
            text = font.render("PAUSE", True, (255, 255, 255))  # Elige el texto y el color del texto

            # Dibuja la superficie con el texto en el centro de la pantalla
            text_rect = text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
            screen.blit(text, text_rect)

            pygame.display.update()
            clock.tick(15)  # FPS de la pantalla de pausa

        
    #Funcion para mostrar el texto game over en la pantalla
    def game_over_text():
        over_text = over_font.render("GAME OVER", True, (255, 255, 255))
        text_rect = over_text.get_rect(
            center=(int(screen_width/2), int(screen_height/2)))
        screen.blit(over_text, text_rect)
        
        
    #Funcion principal del juego 
    def gameloop():
        
        #Declarando variables globales
        global score
        global playerX
        global playerx_change
        global bulletX
        global bulletY
        global Collision
        global bullet_state
        
        in_game = True
        while in_game:
            #Maneja eventos, actualiza y renderiza el juego
            #Limpia pantalla
            screen.fill((0, 0 ,0))
            screen.blit(background, (0, 0))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    in_game = False
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:  # Presiona la tecla 'p' para pausar el juego
                        show_pause_screen()
                    #Maneja el movimiento del jugador y el disparo 
                    if event.key == pygame.K_LEFT:
                        playerx_change = -5
                        
                    if event.key == pygame.K_RIGHT:
                        playerx_change =  5
                        
                    if event.key == pygame.K_x:
                        if bullet_state == "ready":
                            bulletX = playerX
                            fire_bullet(bulletX, bulletY)
                    
                if event.type == pygame.KEYUP:
                    playerx_change = 0
                        
            #Aqui  se esta actulizando la posicion del jugador 
            playerX += playerx_change
            
            if playerX <= 0:
                playerX = 0
            elif playerX >= 736:
                playerX = 736
                
            #Bucle que se ejecuta para cada enemigo
            for i in range(no_of_enemies):
                if enemyY[i] > 440:
                    for j in range(no_of_enemies):
                        enemyY[j] = 20
                    game_over_text()
                    
                enemyX[i] += enemyX_change[i]
                if enemyX[i] <= 0:
                    enemyX_change[i] = 5
                    enemyY[i] += enemyY_change[i]
                elif enemyX[i] >= 736:
                    enemyX_change[i] = -5
                    enemyY[i] += enemyY_change[i]
                    
                 #Aca se comprueba si ha habido una colision entre un enemigo y una bala
                
                collison = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
                if collison:
                    bulletY = 454
                    bullet_state = "ready" 
                    score += 1
                    enemyX[i] = random.randint(0, 736)
                    enemyY[i] = random.randint(0 , 150)
                enemy(enemyX[i], enemyY[i], i)
            
            if bulletY < 0:
                bulletY = 454
                bullet_state = "ready"
            if bullet_state == "fire":
                fire_bullet(bulletX, bulletY)
                bulletY -= bulletX_change
                
            player(playerX, playerY)
            show_score()
            
            pygame.display.update()
            
            clock.tick(120)
            
gameloop()