
# module import
from pico2d import *

# 전역변수 선언
BGI_WIDTH, BGI_HEIGHT = 800, 600 
x = BGI_WIDTH//2
y = BGI_HEIGHT//2
dir_x = 0
dir_y = 0
running = True
standing_sprite_x = [0, 185, 369, 557, 743, 929, 1119, 1308]
running_sprite_x = [0, 197, 395, 617, 809, 1003]
monster_width = 180
monster_height = 100
standing_frame = 0
running_frame = 0

# 캔버스 열기
open_canvas(BGI_WIDTH, BGI_HEIGHT)

# 리소스 파일 불러오기
tuk_ground = load_image('TUK_GROUND.png')
monster = load_image('tauromacis.png')

# 이벤트 발생 확인 함수 선언
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
    # x축 바깥 화면으로 나가지 못함
    if (x < monster_width//2):
        x = monster_width//2
    elif (x > BGI_WIDTH - monster_width//2):
        x = BGI_WIDTH - monster_width//2
    # y축 바깥 화면으로 나가지 못함
    if (y < monster_height//2):
        y = monster_height//2
    elif (y > BGI_HEIGHT - monster_height//2):
        y = BGI_HEIGHT - monster_height//2
    # 멈춤/움직임 스프라이트 구분
    if (dir_x == 0) & (dir_y == 0):
        monster.clip_draw(standing_sprite_x[standing_frame], 1104-120, 186, 120, x, y, monster_width, monster_height)
    else:
        monster.clip_draw(running_sprite_x[running_frame], 1104-280, 193, 120, x, y, monster_width, monster_height)
    update_canvas()
    handle_events()
    standing_frame = (standing_frame + 1) % 8
    running_frame = (running_frame + 1) % 6
    x += dir_x * 10
    y += dir_y * 10
    delay(0.05)

# 캔버스 닫기
close_canvas()
