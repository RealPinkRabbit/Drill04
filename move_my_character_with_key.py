from pico2d import *

BGI_WIDTH, BGI_HEIGHT = 800, 600
open_canvas(BGI_WIDTH, BGI_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')

running = True

while running:
    clear_canvas()
    tuk_ground.draw(BGI_WIDTH//2, BGI_HEIGHT//2)
    update_canvas()
    delay(0.05)

close_canvas()
