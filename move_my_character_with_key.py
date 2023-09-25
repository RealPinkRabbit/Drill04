from pico2d import *

BGI_WIDTH, BGI_HEIGHT = 800, 600
open_canvas(BGI_WIDTH, BGI_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')

def handle_events():
    global running
    
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

running = True

while running:
    clear_canvas()
    tuk_ground.draw(BGI_WIDTH//2, BGI_HEIGHT//2)
    update_canvas()
    handle_events()
    delay(0.05)

close_canvas()
