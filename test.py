from pygame import *


window = display.set_mode((700, 500))
display.set_caption("Догонялки")
background = transform.scale(image.load("background.jpg"), (700, 500))


#данные о спрайте-картинке
x1 = 100 #координаты 1ого спрайта
y1 = 300


x2 = 300    #координаты 2ого 
y2 = 300


sprite1 = transform.scale(image.load('sprite1.gif'), (100, 100)) # назначаем нашей моделе такие картинки 
sprite2 = transform.scale(image.load('sprite2.jpg'), (100, 100)) # назначаем нашей моделе такие картинки 
speed = 10


#игровой цикл
run = True
clock = time.Clock()
FPS = 60


while run:
   window.blit(background,(0, 0)) # отобразить фон в окне
   window.blit(sprite1, (x1, y1))  # отобразить спрайт в таких координатах
   window.blit(sprite2, (x2, y2)) # отобразить спрайт в таких координатах


   for e in event.get():
       if e.type == QUIT:   # пока не нажа красный крести игра продолжается, если нажат то все
           run = False


   keys_pressed = key.get_pressed()


   if keys_pressed[K_LEFT] and x1 > 5:
       x1 -= speed
   if keys_pressed[K_RIGHT] and x1 < 595:
       x1 += speed
   if keys_pressed[K_UP] and y1 > 5:
       y1 -= speed
   if keys_pressed[K_DOWN] and y1 < 395:
       y1 += speed


   if keys_pressed[K_a] and x2 > 5:
       x2 -= speed
   if keys_pressed[K_d] and x2 < 595:
       x2 += speed
   if keys_pressed[K_w] and y2 > 5:
       y2 -= speed
   if keys_pressed[K_s] and y2 < 395:
       y2 += speed


   display.update()
   clock.tick(FPS)
