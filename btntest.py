import pygame as py, sys
import button
 
py.init()
py.font.init()

#Set khung hình
screen_size = (800, 600)
screen = py.display.set_mode(screen_size) 
py.display.set_caption('GAME GIẢI ĐỐ')
icon = py.image.load(r'assets\SGU_logo.png')
py.display.set_icon(icon)
#Set background screen 
scrBgr_img = py.image.load(r'assets\background.png')
gameName_img = py.image.load(r'assets\bg_gameName.png')
 
# Set framerate
fps = 60
framerate = py.time.Clock()

def get_font(size): #lấy font chữ
    return py.font.Font(r'assets\font.ttf', size)
def level_font(size):
    return py.font.Font(r'assets\Tricky_Jimmy.otf', size)
def add_font(text, x, y):
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)
def draw_img(x, y, img, scale):
    width = img.get_width()
    height = img.get_height()
    img = py.transform.scale(img, (int(width*scale), int(height*scale)))
    rect = img.get_rect()
    rect.topleft = (x, y)
    screen.blit(img,(rect.x, rect.y)) 

def main_menu():
    startBtn_img = py.image.load('assets\start_btn.png')
    startBtnHvr_img = py.image.load('assets\startBtn_hover.png')
    startBtnPrs_img = py.image.load('assets\startBtn_pressed.png')

    exitBtn_img = py.image.load('assets\exit_btn.png')
    exitBtnHvr_img = py.image.load('assets\exitBtn_hover.png')
    exitBtnPrs_img = py.image.load('assets\exitBtn_pressed.png')

    running = True
    while running:
        draw_img(0,0,scrBgr_img,1)
        draw_img(300,0,gameName_img,1)

        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
    
        left, middle, right = py.mouse.get_pressed()

        btn_start = button.Button(startBtn_img, (500, 300), None)
        if btn_start.rect.collidepoint(py.mouse.get_pos()):
            btn_start.hover(startBtnHvr_img)
            if left and btn_start.rect.collidepoint(py.mouse.get_pos()):
                btn_start.pressed(startBtnPrs_img)
                #py.time.delay(800)
                
            else:
                btn_start.hover(startBtnHvr_img)
            return level_1()
        else:
            btn_start.normal(startBtn_img)
        btn_start.draw_btn(screen)

        btn_exit = button.Button(exitBtn_img, (500,420), None)
        if btn_exit.rect.collidepoint(py.mouse.get_pos()):
            btn_exit.hover(exitBtnHvr_img)
    
            if left and btn_exit.rect.collidepoint(py.mouse.get_pos()):
                btn_exit.pressed(exitBtnPrs_img)
                #py.time.wait(800)
                #py.quit()
                #sys.exit()
            else:
                btn_exit.hover(exitBtnHvr_img)
        else:
            btn_exit.normal(exitBtn_img)
        btn_exit.draw_btn(screen)

        if event.type == py.QUIT:
                py.quit()
                sys.exit()    
    
        
        framerate.tick(fps)
        py.display.update()

def level_1():
    py.display.set_caption('Level 1')
    lv1Bgr_img = py.image.load(r'assets\level1_bg.png')
    draw_img(0,0,lv1Bgr_img,1)
    play_quest = get_font(35).render('Đâu là cục xương của chú chó?',True,'black')
    add_font(play_quest, 400, 66)
    lv1Item1_img = py.image.load(r'assets\lv1_item1.png')
    lv1Item2_img = py.image.load(r'assets\lv1_item2.png')
    lv1Item3_img = py.image.load(r'assets\lv1_item3.png')
    lv1Item4_img = py.image.load(r'assets\lv1_item4.png')
    draw_img(600,150,lv1Item1_img,0.7)
    draw_img(600,260,lv1Item2_img,0.7)
    draw_img(600,370,lv1Item3_img,0.7)
    draw_img(600,480,lv1Item4_img,0.7)
    cap_level1 = level_font(40).render('Level 1',True,'red')
    add_font(cap_level1, 400, 30)
        
    backBtn_img = py.image.load(r'assets\back.png')
    backBtnHvr_img = py.image.load(r'assets\back_hover.png')
    backBtnPrs_img = py.image.load(r'assets\back_pressed.png')
        
    restartBtn_img = py.image.load(r'assets\restart.png')
    btn_restart = button.Button(restartBtn_img, (80, 10), None)
    btn_restart.draw_btn(screen)

    hintBtn_img = py.image.load(r'assets\hint.png')
    btn_hint = button.Button(hintBtn_img, (150, 10), None)
    btn_hint.draw_btn(screen)

    musicBtn_img = py.image.load(r'assets\music.png')
    btn_music = button.Button(musicBtn_img, (700, 10), None)
    btn_music.draw_btn(screen)

    running = True
    while running:
        for event in py.event.get():
            mouse_pos = py.mouse.get_pos()
            left, middle, right = py.mouse.get_pressed()

            btn_back = button.Button(backBtn_img, (10, 10), None)
            if btn_back.rect.collidepoint(mouse_pos):
                btn_back.hover(backBtnHvr_img)
                if left and btn_back.rect.collidepoint(mouse_pos):
                    btn_back.pressed(backBtnPrs_img)
                    #py.time.wait(800)
                    main_menu()
                else:
                    btn_back.hover(backBtnHvr_img)
            else:
                btn_back.normal(backBtn_img)
            btn_back.draw_btn(screen)
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
            
        framerate.tick(fps)
        py.display.update()


main_menu()