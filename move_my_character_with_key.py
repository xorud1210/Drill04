from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('Balrog.png')

def handle_events():
    global running, x_dir
    global x

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                x_dir += 1
            elif event.key == SDLK_LEFT:
                x_dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                x_dir -= 1
            elif event.key == SDLK_LEFT:
                x_dir += 1
        # fill here

running = True
frame = 0
x_dir = 0
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 185, 0, 185, 175, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 5
    x += x_dir * 10
    delay(0.05)

close_canvas()