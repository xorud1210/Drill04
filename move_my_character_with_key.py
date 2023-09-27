from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('Balrog.png')

def handle_events():
    global running, x_dir, y_dir
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
            elif event.key == SDLK_UP:
                y_dir += 1
            elif event.key == SDLK_DOWN:
                y_dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                x_dir -= 1
            elif event.key == SDLK_LEFT:
                x_dir += 1
            elif event.key == SDLK_UP:
                y_dir -= 1
            elif event.key == SDLK_DOWN:
                y_dir += 1


running = True
frame = 0
x_dir = 0
y_dir = 0
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if x_dir == 0 and y_dir == 0:
        character.clip_draw(frame * 185, 200, 185, 175, x, y)
    elif x_dir == 1:
        character.clip_composite_draw(frame * 185, 0, 185, 175, 0, 'h', x, y, 185, 175)
    else:
        character.clip_draw(frame * 185, 0, 185, 175, x, y)
    update_canvas()
    handle_events()

    # 애니메이션에 따라 프레임 조절
    if x_dir == 0 and y_dir == 0:
        frame = (frame + 1) % 2
    else:
        frame = (frame + 1) % 5

    #경계면 넘어가지 않기
    if x > TUK_WIDTH:
        x = TUK_WIDTH
    elif x < 0:
        x = 0
    else:
        x += x_dir * 10

    #경계면 넘어가지 않기
    if y > TUK_HEIGHT:
        y = TUK_HEIGHT
    elif y < 0:
        y = 0
    else:
        y += y_dir * 10


    delay(0.05)


close_canvas()