
# module import
from pico2d import *

# 전역변수 선언
BGI_WIDTH, BGI_HEIGHT = 800, 600
x = BGI_WIDTH//2
y = BGI_HEIGHT//2
dir_x = 0
dir_y = 0
open_canvas(BGI_WIDTH, BGI_HEIGHT)
running = True
standing_sprite_x = [0, 185, 369, 557, 743, 929, 1119, 1308]
running_sprite_x = [0, 197, 395, 617, 809, 1003]
standing_frame = 0
running_frame = 0

# 리소스 파일
tuk_ground = load_image('TUK_GROUND.png')
monster = load_image('tauromacis.png')

# 함수 선언
def handle_events():
    global running, dir_x, dir_y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
            elif event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1

# 메인함수
while running:
    clear_canvas()
    tuk_ground.draw(BGI_WIDTH//2, BGI_HEIGHT//2)
    if (dir_x == 0) & (dir_y == 0):
        monster.clip_draw(standing_sprite_x[standing_frame], 1104-120, 186, 120, x, y)
    else:
        monster.clip_draw(running_sprite_x[running_frame], 1104-280, 193, 120, x, y)
    
    update_canvas()
    handle_events()
    standing_frame = (standing_frame + 1) % 8
    running_frame = (running_frame + 1) % 6
    x += dir_x * 5
    y += dir_y * 5
    delay(0.05)

close_canvas()
