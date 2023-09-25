
# module_inport

from pico2d import *



### 리소스파일 불러오기

tuk_ground = load_image('TUK_GROUND.png')
monster = load_image('tauromacis.png')



### 전역변수 선언

BGI_WIDTH, BGI_HEIGHT = 800, 600
x = BGI_WIDTH // 2
y = BGI_HEIGHT // 2
x_dir = 0
y_dir = 0
open_canvas(BGI_WIDTH, BGI_HEIGHT)
running = True
standing_sprite_x = [0, 185, 369, 557, 743, 929, 1119, 1308]
running_sprite_x = [0, 197, 395, 617, 809, 1003]



### 함수 선언/정의

def handle_events():
    global running
    global y_dir
    global x_dir
    
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_UP:
                y_dir += 1
            elif event.key == SDLK_DOWN:
                y_dir -= 1
            elif event.key == SDLK_RIGHT:
                x_dir += 1
            elif event.key == SDLK_LEFT:
                x_dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_UP:
                y_dir -= 1
            elif event.key == SDLK_DOWN:
                y_dir += 1
            elif event.key == SDLK_RIGHT:
                x_dir -= 1
            elif event.key == SDLK_LEFT:
                x_dir += 1


### 메인함수
            
while running:
    clear_canvas()
    tuk_ground.draw(BGI_WIDTH//2, BGI_HEIGHT//2)
#    monster.clip_draw(standing_sprite_x[standing_frame], 1104-120, 186, 120, 400, 300)
    monster.clip_draw(running_sprite_x[running_frame], 1104-280, 193, 120, x, y)
    
    update_canvas()
    handle_events()
    x += x_dir * 5
    y += y_dir * 5
    delay(0.05)

close_canvas()
