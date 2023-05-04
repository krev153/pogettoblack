import sizeinfo
import pygame


with open("values.txt", "r") as file:
    lines = file.readlines()
    N = int(lines[3].strip().split(":")[1].strip())





# inizializza pygame
pygame.init()

# ottieni le dimensioni dello schermo
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

# crea la finestra di gioco a schermo intero
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

# definisci le coordinate dei pallini bianchi

veroSeDestra = True

if veroSeDestra:
    placeholder = sizeinfo.spawnright(N)
    spawns = placeholder[0]
    vert = placeholder[2]  # retta x=vert inizio
    finevert = placeholder[3]  # retta x=vert fine
    temporale = placeholder[4]  # salto orizzontale
else:
    placeholder = sizeinfo.spawnleft(N)
    spawns = placeholder[0]
    vert = placeholder[2]  # retta x=vert inizio
    finevert = placeholder[3]  # retta x=vert fine
    temporale = -placeholder[4]  # salto orizzontale

# crea i pallini bianchi
white = (255, 255, 255)
radius = 10

for x in spawns[:-1]:
    y = spawns[-1]
    pygame.draw.circle(screen, white, (x[0], y), radius)
    pygame.draw.circle(screen, white, (x[0], y+(screen_height/2)), radius)
for k in range(N):
    pygame.draw.line(screen, pygame.Color("coral"), (vert, 0), (vert, finevert), 5)
    vert = vert + temporale


# aggiorna la finestra di gioco
pygame.display.update()

# attende che l'utente chiuda la finestra
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()


