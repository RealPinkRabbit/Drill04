from pico2d import *

BGI_WIDTH, BGI_HEIGHT = 800, 600
open_canvas(BGI_WIDTH, BGI_HEIGHT)

tuk_ground = load_image('TUK_GROUND.png')
monster = load_image('tauromacis.png')




def handle_events():
    global running
    
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

running = True
standing_sprite_x = [0, 185, 369, 557, 743, 929, 1119, 1308]
running_sprite_x = [0, 197, 395, 617, 809, 1003]
standing_frame = 0
running_frame = 0


while running:
    clear_canvas()
    tuk_ground.draw(BGI_WIDTH//2, BGI_HEIGHT//2)
#    monster.clip_draw(standing_sprite_x[standing_frame], 1104-120, 186, 120, 400, 300)
    monster.clip_draw(running_sprite_x[running_frame], 1104-280, 193, 120, 400, 300)
    
    update_canvas()
    handle_events()
    delay(0.05)
    standing_frame = (standing_frame + 1) % 8
    running_frame = (running_frame + 1) % 6

close_canvas()
