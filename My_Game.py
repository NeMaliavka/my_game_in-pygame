import pygame
#import buildozer as bui
import random

#bui.init()
pygame.init()
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (0,0,0)
BLACK = (255,255,255)

FPS = 30
WIDTH = 1180
HEIGHT = 550
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #, flags=pygame.NOFRAME — чтобы убрать рамку с кнопками

pygame.display.set_caption("My Game")
icon = pygame.image.load('img/icon.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

myfont = pygame.font.Font("fonts/Babylonica-Regular.ttf", 40)
text = myfont.render('My text for Game in PyGame', False, (117, 201, 34))

bg = pygame.image.load('img/bd2.jpeg')
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
bg_x = 0

#steps_sound = pygame.mixer.Sound("sounds/s5.mp3")
piy_sound = pygame.mixer.Sound("sounds/piu.mp3")
oi_sound = pygame.mixer.Sound("sounds/oi.mp3")
titry_sound = pygame.mixer.Sound("sounds/titry.mp3")
ops_sound = pygame.mixer.Sound("sounds/c5.mp3")
o_no_sound = pygame.mixer.Sound("sounds/o_no.mp3")
bird_sound_1 = pygame.mixer.Sound("sounds/pisk-plyushevoy-igrushki-30098_Y918H12a.mp3")
bird_sound_2 = pygame.mixer.Sound("sounds/vzryv.mp3")
bag_sound = pygame.mixer.Sound("sounds/a021308398f5fe6.mp3")
bam_sound = pygame.mixer.Sound("sounds/bam.mp3")
yh_sound = pygame.mixer.Sound("sounds/zvuk-oi-35-mult.mp3")

#steps_sound.play()
pygame.mixer.music.load("sounds/s5.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)

player_speed = 25
player_x = 300
player_y = 273

#данные для прыжка
is_jump =False
j = 9
jump_count = j

#player = pygame.image.load("img/r_1.png")
walk_right = [pygame.image.load("img/r_1.png"),
              pygame.image.load("img/r_2.png"),
              pygame.image.load("img/r_3.png"),
              pygame.image.load("img/r_4.png")]

walk_left = [pygame.image.load("img/l_1.png"),
              pygame.image.load("img/l_2.png"),
              pygame.image.load("img/l_3.png"),
              pygame.image.load("img/l_4.png")]

player_anim_count = 0

#создаём монстра
#monster_1 = pygame.image.load('img/monster.png')
over_monster = [pygame.image.load('img/m1.png'),
                pygame.image.load('img/m2.png'),
                pygame.image.load('img/m3.png'),
                pygame.image.load('img/m4.png'),
                pygame.image.load('img/m5.png'),
                pygame.image.load('img/m6.png')]
monster_1 = random.choice(over_monster)

#Какртинка очень большая и мы уменьшаем её в 5 раз
#monster_1 = pygame.transform.scale(monster_1, (monster_1.get_width() // 5, monster_1.get_height() // 5))
monster_1_x = 1200
monster_1_y = random.randint(150, 450)
#Создаём список для новых монстров
monster_list = []

#monster timer
#Подключаем сам таймер
monster_timer = pygame.USEREVENT +1
#Настраиваем таймер (1000 милисекунд, или 1 секунда)
pygame.time.set_timer(monster_timer, 15000)

#Шрифт для  надписи на экране меню
label =  pygame.font.Font("fonts/Valisca.ttf", 55)
text_lose = label.render("YOU LOSE!", True, (255,255,255))
restart_text = label.render('NEW GAME', False, (255,255,255))
restart_text_rect =restart_text.get_rect(topleft=(WIDTH/2, HEIGHT/2+55))
restart_text_1 = label.render('NEW GAME', False, (255,0,0))
quit_text = label.render('EXIT', False, (255,255,255))
quit_text_rect =quit_text.get_rect(topleft=(WIDTH/2, HEIGHT/2+110))
quit_text_1 = label.render('EXIT', False, (255,0,0))

#снаряды-камни
stone = pygame.image.load("img/Stone_gold.png")
stone = pygame.transform.scale(stone, (stone.get_width() // 2, stone.get_height() // 2))
stones = []
new_stone =False

#количество камней
stone_count = 25
my_stones = label.render("stones: " +str(stone_count), False, (255,0,0))
no_stones = label.render("stones: ran out", False, (255,0,0))

#мешочек с камнями
bag_stones = pygame.image.load("img/bag.png")
bag_list = []
#настраиваем таймер для появления мешочков
bag_timer = pygame.USEREVENT +2
pygame.time.set_timer(bag_timer, 5000)

bird = pygame.image.load("img/51492_bird_icon.png")
bird_list = []
bird_timer = pygame.USEREVENT +3
pygame.time.set_timer(bird_timer, 3500)
bird_zriv = pygame.image.load("img/perya_2-PhotoRoom-transformed (1).png")

#данные для очков
score_count = 0
score_text = label.render("score: " +str(score_count), False, (255,0,0))

#работа с жизнями
live_count = 3
live_img = pygame.image.load("img/285639_heart_icon.png")

'''
#Платформы
platform = pygame.image.load("img/platforma_1.png")
platform = pygame.transform.scale(platform, (350, 100))
platform_timer = pygame.USEREVENT +4
pygame.time.set_timer(platform_timer, 2000)
platform_list = []
'''

#Отслеживание игры
game_play = True

run = True
while run:
    
    screen.blit(bg, (bg_x,0))
    screen.blit(bg, (bg_x+1180,0))
    #отображение надписи счета
    screen.blit(score_text, (870, 5))
 
    if live_count == 3:
        screen.blit(live_img, (WIDTH//2+35, 5))
        screen.blit(live_img, (WIDTH//2, 5))
        screen.blit(live_img, (WIDTH//2 -35, 5))
    elif live_count == 2:
        screen.blit(live_img, (WIDTH//2-35, 5))
        screen.blit(live_img, (WIDTH//2, 5))
    elif live_count == 1:
        screen.blit(live_img, (WIDTH//2-35, 5))
    
    if stone_count>0:
        screen.blit(my_stones, (5, 5))
    else:
        screen.blit(no_stones, (5, 5))
    
    if game_play:
        #Помещаем игрока и монстра в квадраты для дальнейшего взаимосдействия
        player_rect =walk_left[0].get_rect(topleft = (player_x,player_y))
        
        #птицы
        if bird_list:
            for (i, bd) in enumerate(bird_list):
                screen.blit(bird, (bd.x, bd.y))
                if bd.y < 300:                
                    bd.x -= random.randint(3, 9)
                    bd.y += random.randint(7, 11)
                    #if bd.x < WHIDTH/2+10 and :
                        
                if player_rect.colliderect(bd):
                    bird_sound_1.play()
                    bird = bird_zriv
                    screen.blit(bird, (bd.x-50, bd.y-80))
                    bird_list.pop(i)
                    bird = pygame.image.load("img/51492_bird_icon.png")
                if bd.y >= 300 or bd.x < WIDTH/2+10:                 
                    
                    bd.x -= random.randint(8, 15)
                    bd.y -= random.randint(9, 17)
                
                if bd.x<0:
                    bird_list.pop(i)
                    
        #монстры вокругб монстры вокруууг
        if monster_list:
            #для получения индекса элемента вводим функцию enumerate
            for i, el in enumerate(monster_list):
                #выводим монстра на экран (первый blit убираем)
                screen.blit(monster_1, el)
                #Передвигаем монстра
                el.x -= 10

                #Удаляем енужных врагов
                if el.x < -50:
                    monster_list.pop(i)
            
                #Отслеживаем соприкосновения
                if player_rect.colliderect(el):
                    #print('you lose')
                    live_count-=1
                    bam_sound.play()
                    monster_list.pop(i)
                    yh_sound.play()
                    if live_count==0:                        
                        pygame.mixer.music.stop()
                        titry_sound.play()
                        game_play = False
    
        keys = pygame.key.get_pressed() 
    
        #изменяем картинки в зависимости от направления движения
        if keys[pygame.K_LEFT]:
            screen.blit(walk_left[player_anim_count], (player_x,player_y))
        else:
            screen.blit(walk_right[player_anim_count], (player_x,player_y))
        
        #Прыжок
        if not is_jump:
            if keys[pygame.K_UP]:
                oi_sound.play()
                is_jump = True
        else:
            if jump_count >= -j:
                if jump_count > 0:
                    player_y -= (jump_count**2)//2 #возведение в степень для явного прыжка, а деление для плавности 
                    #print(player_y)
                else:
                    player_y += (jump_count**2)//2
                    #print(player_y)
                jump_count -=1
            else:
                is_jump = False
                jump_count = j
        '''
        if platform_list:            
            for i, p in enumerate(platform_list):
                screen.blit(platform, (p.x, p.y))
                p.x -= 2
                if player_rect.colliderect(p):
                    print('yes')
                if player_rect.x >= p.x:                        
                    player_rect.move_ip(-2, 0)
                    print("pl r", player_rect.right,
                          "plat l", p.left)
                    print("rect", player_rect.right,
                          'x', player_x)
                #print("p.x", p.x)               
                
                if player_rect.colliderect(p):
                    if player_rect.right>=p.left:
                        player_x -= 2
                        if keys[pygame.K_RIGHT]:
                            player_x = p.x-60
                    if player_rect.left>=p.right:
                        if keys[pygame.K_RIGHT]:
                            player_x = p.x+160
                    if player_rect.bottom>=p.top and player_rect.bottom <p.bottom:
                        pass
                        
                   print('player right: ', player_rect.right,
                          'platform left: ', p.left,
                          'player left: ', player_rect.left,
                          'platform right: ', p.right)
                    if p.left <= player_rect.right and p.right>=player_rect.left:
                        player_x -= 2
                        if keys[pygame.K_RIGHT]:
                            player_x = p.x-60
                        if player_rect.bottom>= p.top and player_rect.bottom < p.bottom:
                            
                            print('yes')
                            if keys[pygame.K_LEFT]:
                                player_speed = 0
                            player_speed = 25
                        if p.top<= player_rect.bottom:
                            print(player_rect.y, p.y)
                    #player_x += player_speed
                        
                        
                    #if player_rect.x >= p.x:
                        #print(player_rect.x, p.left)
                        #player_x = p.x-60'''
    
        #Ограничиваем игрока в пределах поля, а такж позволяем его передвигать
        if keys[pygame.K_LEFT] and player_x > 50 :
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH-130:
            player_x += player_speed
     
        if player_anim_count==3:
            player_anim_count=0
        else:
            player_anim_count+=1

        #зацикливание координаты Х заднего фона
        bg_x -= 2
        if bg_x == -WIDTH:
            bg_x = 0

        
        #кидание камней при нажатии на z
        if new_stone:            
            stones.append(stone.get_rect(topleft=(player_x +5, player_y +35)))
            #ограничитель камней, см event.type
            new_stone = False
            stone_count -=1
            my_stones = label.render("stones: " +str(stone_count), False, (255,0,0))
            
        if stones:
            for (i, my_stone) in enumerate(stones):                
                screen.blit(stone, (my_stone.x, my_stone.y))
                my_stone.x +=50

                #удаление пули, когда она улетает за экран
                if my_stone.x > WIDTH:
                    stones.pop(i)

                #проверяем есть ли монстры на экране
                if monster_list:
                    #запускаем цикл по списку с монстрами
                    for index,my_monster in enumerate(monster_list):
                        #ИЩЕМ СОПРИКОСНОВЕНИЯ МОНСТРА И КАМНЯ
                        if my_stone.colliderect(my_monster):
                            #удаляем и мнстра, и камень
                            ops_sound.play()
                            score_count +=1
                            score_text = label.render("score: " +str(score_count), False, (255,0,0))                            
                            monster_list[index] = pygame.image.load("img/vzriv1.png")
                            monster_list[index] = pygame.transform.scale(monster_list[index], (monster_list[index].get_width()+17, monster_list[index].get_height()+17))
                            screen.blit(monster_list[index], (my_monster.x-50, my_monster.y-50))                            
                            monster_list.pop(index)
                            stones.pop(i)
                if bird_list:                    
                    for id_b, bad_birds in enumerate(bird_list):
                        if my_stone.colliderect(bad_birds):
                            bird_sound_2.play()
                            bird = bird_zriv
                            screen.blit(bird, (bd.x-50, bd.y-80))
                            bird_list.pop(id_b)
                            stones.pop(i)
                            bird = pygame.image.load("img/51492_bird_icon.png")
                        
        
                    
                    
        #работа со взаимодействием с сумкой камней                   
        if bag_list:
            for (i,b) in enumerate(bag_list):
                screen.blit(bag_stones, (b.x, b.y))
                b.x -= 2
                if player_rect.colliderect(b):
                    bag_sound.play()
                    stone_count += random.randint(3,10)
                    #устранение проблемы индексации элементов в сумке
                    if bag_list:                        
                        bag_list.pop(i)
                    my_stones = label.render("stones: " +str(stone_count), False, (255,0,0))

        
        
            

        

    #Прекращение игры
    else:
        #окрашиваем экран в красный
        screen.fill((0,0,0))
        screen.blit(text_lose, (WIDTH/2, HEIGHT/2))
        screen.blit(restart_text, restart_text_rect)
        screen.blit(quit_text, quit_text_rect)
        
        #Находим позицию мышки
        mouse = pygame.mouse.get_pos()
        press = pygame.mouse.get_pressed()
        #Соприкасается ли квадрат надписи с мышкой
        if restart_text_rect.collidepoint(mouse):
            screen.blit(restart_text_1, restart_text_rect)
            if press[0]:
                titry_sound.stop()
                pygame.mixer.music.play(-1)
                game_play = True
                #Очищаем данные
                player_x = 300
                monster_list.clear()
                stones.clear()
                #обновляем камни, иначе снарядов не будет при перезапуске
                stone_count = 5
                live_count = 3
        elif quit_text_rect.collidepoint(mouse):
            screen.blit(quit_text_1, quit_text_rect)
            if press[0]:
                run = False
                pygame.quit()
    
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

        #нажатие z для запуска пули. Производит звук и меняет значение переменной 
        if game_play and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                if stone_count>0:
                    piy_sound.play()
                    new_stone = True
                else:
                    o_no_sound.play()
                
        #отслеживание таймер для создания новых монстров
        if event.type == monster_timer:
            #print(monster_timer)
            monster_1=random.choice(over_monster)
            monster_1 = pygame.transform.scale(monster_1, (monster_1.get_width() // 3, monster_1.get_height() // 3))
            monster_list.append(monster_1.get_rect(topleft=(monster_1_x, random.randint(90, 280))))
        
        #отслеживание таймер для создания новых мешочков   
        if event.type == bag_timer:
            #print(bag_timer)
            new_bag = random.randint(0, 10)
            if new_bag == 5 or new_bag == 7:
                #print("yes")
                bag_list.append(bag_stones.get_rect(topleft = (monster_1_x, 313)))
        
        #отслеживание таймер для создания новых птиц       
        if event.type == bird_timer:
            bird_list.append(bird.get_rect(topleft = (random.randint(500, 1185), -1)))
        '''
        if event.type == platform_timer:
            p_count = random.randint(0, 5)
            p_y = random.randint(200, 300)
            p_x = WIDTH -1
            if p_count == 5:                
                platform_list.append(platform.get_rect(topleft =( p_x, p_y)))
                new_bag = random.randint(0, 3)
                if new_bag == 2 or new_bag == 3:
                #print("yes")
                    bag_list.append(bag_stones.get_rect(topleft = (p_x+155, p_y-28)))'''
                                 
      
    clock.tick(15)     
