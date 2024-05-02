import pygame, math, random

pygame.init()


width, heigth = 1920, 1080
screen = pygame.display.set_mode((width,heigth))
running = True
clock = pygame.time.Clock()
dt = 0
fps = 240
carpisma = True
hiz1 = 0
hiz2 = 0




def main():
    global dt
    global fps
    global running
    global carpisma
    global hiz1
    global hiz2
  

        
    stars = []
    for _ in range(150):
        x = random.randint(0, width)
        y = random.randint(0, heigth)
        stars.append((x, y))


    konum1 = pygame.Vector2(width/2+width/4,heigth/2)
    konum2 = pygame.Vector2(width/2-width/4,heigth/2)
    kutle1 = 100
    kutle2 = 10
    

    

    def kuvvetHesaplayici(m1,m2,d):
        G_sabiti = (6670 / 1000) * 200
        return G_sabiti * ((m1*m2)/(d*d))
    
    def ivmeHesaplayici(f,m):
        return f/m

    
        
    def carpismaKontrol():
        global carpisma

        if max(konum1.x,konum2.x)-min(konum1.x,konum2.x)-kutle1-kutle2 < 0:
            carpisma = True

    

    def drawPlanet():
        global hiz1
        global hiz2
        global carpisma

        hiz1 += ivme1
        hiz2 += ivme2

        if carpisma ==  False:
            konum1.x -= hiz1 * dt
            konum2.x += hiz2 * dt
        pygame.draw.circle(screen,"dark blue",konum1,kutle1,kutle1)
        pygame.draw.circle(screen,"orange",konum2,kutle2,kutle2)

   

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        

        kuvvet = kuvvetHesaplayici(kutle1,kutle2,abs(konum2.x-konum1.x))
        ivme1 = ivmeHesaplayici(kuvvet,kutle1)
        ivme2 = ivmeHesaplayici(kuvvet,kutle2)

        
 
        
        screen.fill("black")
        for star in stars:
            pygame.draw.circle(screen, "white", star, random.randrange(2,4))
        carpismaKontrol()
        drawPlanet()
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            konum1 = pygame.Vector2(width/2+width/4,heigth/2)
            konum2 = pygame.Vector2(width/2-width/4,heigth/2)
            carpisma = False
            hiz1 = 0
            hiz2 = 0
            ivme1 = 0
            ivme2 = 0
        if keys[pygame.K_w]:
            if kutle1 < 480:
                kutle1 += 1
        if keys[pygame.K_s]:
            if kutle1 > 5:
                kutle1 -= 1
        if keys[pygame.K_UP]:
            if kutle2 < 480:
                kutle2 += 1
        if keys[pygame.K_DOWN]:
            if kutle2 > 5:
                kutle2 -= 1
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
        
        pygame.display.flip()

        dt = clock.tick(fps) / 500

    pygame.quit()


main()