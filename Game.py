import pgzrun

WIDTH = 800
HEIGHT = 600
TITLE = 'Maze Runner'

player = Rect(750, 550, 15, 15)

win = False
score = 0
current_level = 1
starting_position = Rect(750, 550, 15, 15)

started = False

walls_level_1 = [
    Rect(0, 0, 400, 10),  
    Rect(450, 0, 350, 10), 
    Rect(0, 0, 10, 300),  
    Rect(0, 350, 10, 240),  
    Rect(0, 590, 400, 10), 
    Rect(450, 590, 350, 10), 
    Rect(790, 0, 10, 200), 
    Rect(790, 250, 10, 300),  
    Rect(50, 50, 100, 10),
    Rect(50, 150, 10, 200),
    Rect(50, 350, 200, 10),
    Rect(250, 50, 10, 300),
    Rect(100, 100, 200, 10),
    Rect(300, 100, 10, 200),
    Rect(150, 150, 100, 10),
    Rect(450, 50, 10, 150),
    Rect(500, 200, 150, 10),
    Rect(550, 250, 10, 150),
    Rect(200, 350, 250, 10),
    Rect(600, 300, 10, 150),
    Rect(700, 100, 10, 200),
    Rect(400, 450, 200, 10),
    Rect(300, 500, 10, 100),
    Rect(150, 450, 200, 10),
    Rect(100, 400, 10, 100),
    Rect(300, 50, 10, 50),
    Rect(500, 500, 100, 10),
    Rect(600, 400, 100, 10),
    Rect(700, 500, 10, 100),
    Rect(100, 300, 100, 10),
    Rect(200, 250, 10, 100),
    Rect(450, 350, 150, 10),
    Rect(350, 250, 10, 100),
    Rect(250, 350, 100, 10),
    Rect(350, 450, 200, 10),
    Rect(100, 200, 10, 100),
    Rect(700, 400, 10, 100),
    Rect(650, 450, 50, 10),
    Rect(400, 150, 10, 100),
    Rect(300, 450, 10, 100),
    Rect(150, 100, 10, 200),
    Rect(550, 50, 10, 100),
    Rect(600, 150, 200, 10),
    Rect(650, 200, 150, 10),
    Rect(750, 250, 10, 100),
    Rect(600, 350, 10, 150),
    Rect(550, 450, 10, 100),
    Rect(500, 500, 10, 100),
    Rect(450, 550, 150, 10),
    Rect(350, 550, 10, 50),
    Rect(250, 500, 100, 10),
    Rect(150, 550, 100, 10),
    Rect(100, 500, 10, 100),
    Rect(300, 200, 150, 10),
    Rect(450, 150, 100, 10),
    Rect(550, 200, 150, 10),
    Rect(600, 250, 10, 100),
    Rect(650, 300, 100, 10),
    Rect(0, 0, 400, 10),
    Rect(450, 0, 350, 10),
    Rect(0, 0, 10, 300),
    Rect(650, 300, 100, 10),
]

walls_level_2 = [
    Rect(0, 0, 400, 10),
    Rect(450, 0, 350, 10),
    Rect(0, 0, 10, 300),
    Rect(0, 350, 10, 240),
    Rect(0, 590, 400, 10),
    Rect(450, 590, 350, 10),
    Rect(790, 0, 10, 200),
    Rect(790, 250, 10, 300),
    Rect(50, 50, 300, 10),
    Rect(50, 150, 10, 200),
    Rect(350, 50, 10, 300),
    Rect(100, 100, 200, 10),
    Rect(300, 150, 200, 10),
    Rect(500, 200, 10, 200),
    Rect(200, 400, 400, 10),
    Rect(700, 100, 10, 200),
    Rect(400, 450, 200, 10),
    Rect(300, 500, 10, 100),
    Rect(150, 450, 200, 10),
    Rect(100, 400, 10, 100),
    Rect(600, 400, 100, 10),
    Rect(700, 500, 10, 100),
    Rect(100, 300, 100, 10),
    Rect(650, 450, 10, 100),
    Rect(500, 50, 150, 10),
    Rect(600, 300, 150, 10),
    Rect(750, 250, 10, 100),
    Rect(400, 100, 200, 10),
    Rect(300, 350, 300, 10),
    Rect(200, 550, 200, 10),
    Rect(500, 550, 200, 10),
    Rect(700, 400, 10, 100),
    Rect(650, 450, 50, 10),
    Rect(400, 150, 10, 100),
    Rect(300, 450, 10, 100),
    Rect(150, 100, 10, 200),
    Rect(550, 50, 10, 100),
    Rect(600, 150, 200, 10),
    Rect(650, 200, 150, 10),
    Rect(750, 250, 10, 100),
    Rect(600, 350, 10, 150),
    Rect(550, 450, 10, 100),
    Rect(500, 500, 10, 100),
    Rect(450, 550, 150, 10),
    Rect(350, 550, 10, 50),
    Rect(0, 590, 400, 10), 
    Rect(450, 590, 350, 10), 
    Rect(790, 0, 10, 200), 
    Rect(790, 250, 10, 300),  
    Rect(50, 50, 100, 10),
    Rect(50, 150, 10, 200),
    Rect(50, 350, 200, 10),
    Rect(250, 50, 10, 300),
    Rect(100, 100, 200, 10),
    Rect(300, 100, 10, 200),
    Rect(150, 150, 100, 10),
    Rect(0, 590, 400, 10), 
    Rect(450, 590, 350, 10), 
    Rect(790, 0, 10, 200), 
    Rect(790, 250, 10, 300),  
    Rect(50, 50, 100, 10),
    Rect(50, 150, 10, 200),
    Rect(50, 350, 200, 10),
    Rect(700, 100, 10, 200),
    Rect(400, 450, 200, 10),
    Rect(300, 500, 10, 100),
    Rect(150, 450, 200, 10),
    Rect(150, 100, 10, 200),
    Rect(550, 50, 10, 100),
    Rect(600, 150, 200, 10),
    Rect(650, 200, 150, 10),
    Rect(750, 250, 10, 100),
    Rect(600, 350, 10, 150),
    Rect(550, 450, 10, 100),
    Rect(500, 500, 10, 100),
    Rect(450, 550, 150, 10),
    Rect(350, 550, 10, 50),
    Rect(250, 500, 100, 10),
    Rect(150, 550, 100, 10),
]

def draw():
    screen.clear()

    if not started:
        screen.draw.text("Click to Start", center=(WIDTH // 2, HEIGHT // 2), fontsize=60, color="white")
    else:
        if current_level == 1:
            walls = walls_level_1
        elif current_level == 2:
            walls = walls_level_2
        
        for wall in walls:
            screen.draw.filled_rect(wall, 'grey')
        screen.draw.filled_rect(player, 'red')
        screen.draw.text(f"Score: {score}", (10, 10), color="white", fontsize=30)
        
        if win:
            screen.draw.text("You Win!", center=(WIDTH // 2, HEIGHT // 2), fontsize=60, color="yellow")

def on_mouse_down(pos):
    global started
    started = True  

def update():
    global win, score, current_level
    if started and not win:
        if keyboard.left:
            player.x -= 2
        if keyboard.right:
            player.x += 2
        if keyboard.up:
            player.y -= 2
        if keyboard.down:
            player.y += 2

        if current_level == 1:
            walls = walls_level_1
        elif current_level == 2:
            walls = walls_level_2
        
        for wall in walls:
            if player.colliderect(wall):
                player.x = starting_position.x
                player.y = starting_position.y
                score -= 1

        if player.y < 0:
            if current_level == 1:
                current_level = 2 
                player.x = starting_position.x
                player.y = starting_position.y
                score += 10
            else:
                win = True
                score += 10
                sounds.win.play()

pgzrun.go()
