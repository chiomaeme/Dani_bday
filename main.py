@namespace
class SpriteKind:
    Selector = SpriteKind.create()
    CurrentPlayer = SpriteKind.create()
    astronautPlayer = SpriteKind.create()
    Door1 = SpriteKind.create()
    Door2 = SpriteKind.create()
    portalKey = SpriteKind.create()
@namespace
class StatusBarKind:
    Speed = StatusBarKind.create()
    Durability = StatusBarKind.create()
    Capacity = StatusBarKind.create()
def choiceMade():
    if choose.overlaps_with(fastest_spaceship):
        info.set_score(0)
        fastToCurrent()
        spawnMap1Key()
        spawnCoins()
    elif choose.overlaps_with(durable_spaceship):
        info.set_score(0)
        durableToCurrent()
        spawnMap1Key()
        spawnCoins()
    elif choose.overlaps_with(capacity_spaceship):
        info.set_score(0)
        capacityToCurrent()
        spawnMap1Key()
        spawnCoins()

def on_a_pressed():
    choiceMade()
    # Add another condition to check for, if the astronaut is on top of a wall in order to not have him fly around.
    if choiceScene != 1 and astronaut.is_hitting_tile(CollisionDirection.BOTTOM):
        astronaut.vy = -150
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def spawnCoins():
    global coin1, coin2
    coin1 = sprites.create(assets.image("""
        myImage
    """), SpriteKind.player)
    animation.run_image_animation(None, assets.animation("""
        myAnim
    """), 500, True)
    tiles.place_on_tile(coin1, tiles.get_tile_location(5, 19))
    coin2 = sprites.create(assets.image("""
        myImage
    """), SpriteKind.player)
    tiles.place_on_tile(coin2, tiles.get_tile_location(4, 18))

def on_left_pressed():
    # Add another condition to check for, if the astronaut is on top of a wall in order to not have him fly around.
    if choiceScene != 1:
        astronaut.set_image(assets.image("""
            AstronautLeft
        """))
        astronaut.vx += astronautSpeed * -1
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_on_overlap(sprite, otherSprite):
    global currentPortalKey
    if info.score() < 15:
        currentPortalKey.say_text("You did not collect enough gold")
    else:
        music.play(music.melody_playable(music.ba_ding),
            music.PlaybackMode.UNTIL_DONE)
        sprites.destroy(otherSprite, effects.cool_radial, 750)
        currentPortalKey = portalDoor1Key
sprites.on_overlap(SpriteKind.astronautPlayer,
    SpriteKind.portalKey,
    on_on_overlap)

def on_right_released():
    # Add another condition to check for, if the astronaut is on top of a wall in order to not have him fly around.
    if choiceScene != 1:
        astronaut.vx = 0
controller.right.on_event(ControllerButtonEvent.RELEASED, on_right_released)

def createCapacitySpaceship():
    global capacity_spaceship, capSpace_SpeedStatusBar, capSpace_CapStatusBar, capSpace_DurStatusBar
    capacity_spaceship = sprites.create(assets.image("""
            CAPACITY_SPACESHIP
        """),
        SpriteKind.player)
    capacity_spaceship.set_position(120, 60)
    capSpace_SpeedStatusBar = statusbars.create(15, 4, StatusBarKind.Speed)
    capSpace_SpeedStatusBar.max = 75
    capSpace_SpeedStatusBar.value = 75
    capSpace_SpeedStatusBar.position_direction(CollisionDirection.BOTTOM)
    capSpace_SpeedStatusBar.set_label("S")
    capSpace_SpeedStatusBar.attach_to_sprite(capacity_spaceship, 0, 0)
    capSpace_CapStatusBar = statusbars.create(20, 4, StatusBarKind.Capacity)
    capSpace_CapStatusBar.max = 100
    capSpace_CapStatusBar.value = 100
    capSpace_CapStatusBar.position_direction(CollisionDirection.BOTTOM)
    capSpace_CapStatusBar.set_label("C")
    capSpace_CapStatusBar.attach_to_sprite(capacity_spaceship, 10, 0)
    capSpace_DurStatusBar = statusbars.create(10, 4, StatusBarKind.Durability)
    capSpace_DurStatusBar.max = 50
    capSpace_DurStatusBar.value = 50
    capSpace_DurStatusBar.position_direction(CollisionDirection.BOTTOM)
    capSpace_DurStatusBar.set_label("D")
    capSpace_DurStatusBar.attach_to_sprite(capacity_spaceship, 20, 0)

def on_left_released():
    # Add another condition to check for, if the astronaut is on top of a wall in order to not have him fly around.
    if choiceScene != 1:
        astronaut.vx = 0
controller.left.on_event(ControllerButtonEvent.RELEASED, on_left_released)

def spawnMap1Key():
    global portalDoor1Key
    portalDoor1Key = sprites.create(img("""
            ........................
                    ........................
                    ....fff.................
                    ...f118ff...............
                    ..f188881f..............
                    .f188f8881fffffffffffff.
                    .f88f1f8888888888888811f
                    .f88f1f888888888888f888f
                    .f888f8888fffffff8f.f88f
                    ..f888881f......f8f.f81f
                    ...f881ff........f...ff.
                    ....fff.................
                    ........................
                    ........................
                    ........................
                    ........................
        """),
        SpriteKind.portalKey)
    tiles.place_on_tile(portalDoor1Key, tiles.get_tile_location(28, 18))
def durableToCurrent():
    global currentSpaceship, astronaut, choiceScene, current_tilemap
    durable_spaceship.set_kind(SpriteKind.CurrentPlayer)
    currentSpaceship = durable_spaceship
    fastest_spaceship.vy = -50
    capacity_spaceship.vy = -50
    sprites.destroy_all_sprites_of_kind(SpriteKind.player, effects.spray, 2000)
    sprites.destroy_all_sprites_of_kind(SpriteKind.Selector, effects.spray, 2000)
    pause(2750)
    astronaut = sprites.create(assets.image("""
            AstronautRight
        """),
        SpriteKind.astronautPlayer)
    choiceScene = 3
    tiles.set_current_tilemap(first_tilemap)
    current_tilemap = first_tilemap
    tiles.place_on_tile(currentSpaceship, tiles.get_tile_location(1, 28))
    tiles.place_on_tile(astronaut, tiles.get_tile_location(3, 28))
    scene.camera_follow_sprite(astronaut)

def on_right_pressed():
    # Add another condition to check for, if the astronaut is on top of a wall in order to not have him fly around.
    if choiceScene != 1:
        astronaut.set_image(assets.image("""
            AstronautRight
        """))
        astronaut.vx += astronautSpeed
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_on_overlap2(sprite2, otherSprite2):
    global current_tilemap, portalDoor2
    if controller.B.is_pressed() and (currentSpaceship == fastest_spaceship and fastSpace_DurStatusBar.value > 0 and currentPortalKey == portalDoor1Key):
        tiles.set_current_tilemap(second_tilemap)
        current_tilemap = second_tilemap
        fastSpace_DurStatusBar.value += -15
    if current_tilemap == second_tilemap:
        sprites.destroy_all_sprites_of_kind(SpriteKind.Door1)
        portalDoor2 = sprites.create(assets.image("""
            Portal2
        """), SpriteKind.Door2)
        tiles.place_on_random_tile(portalDoor2, assets.tile("""
            portalDoorLocation
        """))
        tiles.place_on_tile(currentSpaceship, tiles.get_tile_location(1, 37))
        tiles.place_on_tile(astronaut, tiles.get_tile_location(3, 37))
        astronaut.say_text("I have landed!", 1000, False)
sprites.on_overlap(SpriteKind.astronautPlayer, SpriteKind.Door1, on_on_overlap2)

def on_a_released():
    if choiceScene != 1:
        astronaut.ay = 200
controller.A.on_event(ControllerButtonEvent.RELEASED, on_a_released)

def createDurableSpaceship():
    global durable_spaceship, durSpace_SpeedStatusBar, durSpace_CapStatusBar, durSpace_DurStatusBar
    durable_spaceship = sprites.create(assets.image("""
            DURABLE_SPACESHIP
        """),
        SpriteKind.player)
    durable_spaceship.set_position(80, 60)
    durSpace_SpeedStatusBar = statusbars.create(10, 4, StatusBarKind.Speed)
    durSpace_SpeedStatusBar.max = 50
    durSpace_SpeedStatusBar.value = 50
    durSpace_SpeedStatusBar.position_direction(CollisionDirection.BOTTOM)
    durSpace_SpeedStatusBar.set_label("S")
    durSpace_SpeedStatusBar.attach_to_sprite(durable_spaceship, 0, 0)
    durSpace_CapStatusBar = statusbars.create(15, 4, StatusBarKind.Capacity)
    durSpace_CapStatusBar.max = 75
    durSpace_CapStatusBar.value = 75
    durSpace_CapStatusBar.position_direction(CollisionDirection.BOTTOM)
    durSpace_CapStatusBar.set_label("C")
    durSpace_CapStatusBar.attach_to_sprite(durable_spaceship, 10, 0)
    durSpace_DurStatusBar = statusbars.create(20, 4, StatusBarKind.Durability)
    durSpace_DurStatusBar.max = 100
    durSpace_DurStatusBar.value = 100
    durSpace_DurStatusBar.position_direction(CollisionDirection.BOTTOM)
    durSpace_DurStatusBar.set_label("D")
    durSpace_DurStatusBar.attach_to_sprite(durable_spaceship, 20, 0)
def capacityToCurrent():
    global currentSpaceship, astronaut, choiceScene, current_tilemap
    capacity_spaceship.set_kind(SpriteKind.CurrentPlayer)
    currentSpaceship = capacity_spaceship
    fastest_spaceship.vy = -50
    durable_spaceship.vy = -50
    sprites.destroy_all_sprites_of_kind(SpriteKind.player, effects.spray, 2000)
    sprites.destroy_all_sprites_of_kind(SpriteKind.Selector, effects.spray, 2000)
    pause(2750)
    astronaut = sprites.create(assets.image("""
            AstronautRight
        """),
        SpriteKind.astronautPlayer)
    choiceScene = 4
    tiles.set_current_tilemap(first_tilemap)
    current_tilemap = first_tilemap
    tiles.place_on_tile(currentSpaceship, tiles.get_tile_location(1, 28))
    tiles.place_on_tile(astronaut, tiles.get_tile_location(3, 28))
    scene.camera_follow_sprite(astronaut)
def fastToCurrent():
    global currentSpaceship, astronaut, choiceScene, current_tilemap
    fastest_spaceship.set_kind(SpriteKind.CurrentPlayer)
    currentSpaceship = fastest_spaceship
    durable_spaceship.vy = -50
    capacity_spaceship.vy = -50
    sprites.destroy_all_sprites_of_kind(SpriteKind.player, effects.spray, 2000)
    sprites.destroy_all_sprites_of_kind(SpriteKind.Selector, effects.spray, 2000)
    pause(2750)
    astronaut = sprites.create(assets.image("""
            AstronautRight
        """),
        SpriteKind.astronautPlayer)
    choiceScene = 2
    tiles.set_current_tilemap(first_tilemap)
    current_tilemap = first_tilemap
    tiles.place_on_tile(currentSpaceship, tiles.get_tile_location(1, 28))
    tiles.place_on_tile(astronaut, tiles.get_tile_location(3, 28))
    scene.camera_follow_sprite(astronaut)
def createFastestSpaceShip():
    global fastest_spaceship, fastSpace_SpeedStatusBar, fastSpace_CapStatusBar, fastSpace_DurStatusBar
    fastest_spaceship = sprites.create(assets.image("""
        FAST_SPACESHIP
    """), SpriteKind.player)
    fastest_spaceship.set_position(40, 60)
    fastSpace_SpeedStatusBar = statusbars.create(20, 4, StatusBarKind.Speed)
    fastSpace_SpeedStatusBar.max = 100
    fastSpace_SpeedStatusBar.value = 100
    fastSpace_SpeedStatusBar.position_direction(CollisionDirection.BOTTOM)
    fastSpace_SpeedStatusBar.set_label("S")
    fastSpace_SpeedStatusBar.attach_to_sprite(fastest_spaceship, 0, 0)
    fastSpace_CapStatusBar = statusbars.create(10, 4, StatusBarKind.Capacity)
    fastSpace_CapStatusBar.max = 50
    fastSpace_CapStatusBar.value = 50
    fastSpace_CapStatusBar.position_direction(CollisionDirection.BOTTOM)
    fastSpace_CapStatusBar.set_label("C")
    fastSpace_CapStatusBar.attach_to_sprite(fastest_spaceship, 10, 0)
    fastSpace_DurStatusBar = statusbars.create(15, 4, StatusBarKind.Durability)
    fastSpace_DurStatusBar.max = 75
    fastSpace_DurStatusBar.value = 75
    fastSpace_DurStatusBar.position_direction(CollisionDirection.BOTTOM)
    fastSpace_DurStatusBar.set_label("D")
    fastSpace_DurStatusBar.attach_to_sprite(fastest_spaceship, 20, 0)
portalDoor1: Sprite = None
fastSpace_CapStatusBar: StatusBarSprite = None
fastSpace_SpeedStatusBar: StatusBarSprite = None
durSpace_DurStatusBar: StatusBarSprite = None
durSpace_CapStatusBar: StatusBarSprite = None
durSpace_SpeedStatusBar: StatusBarSprite = None
portalDoor2: Sprite = None
fastSpace_DurStatusBar: StatusBarSprite = None
current_tilemap: tiles.TileMapData = None
currentSpaceship: Sprite = None
capSpace_DurStatusBar: StatusBarSprite = None
capSpace_CapStatusBar: StatusBarSprite = None
capSpace_SpeedStatusBar: StatusBarSprite = None
portalDoor1Key: Sprite = None
currentPortalKey: Sprite = None
astronautSpeed = 0
coin2: Sprite = None
coin1: Sprite = None
astronaut: Sprite = None
capacity_spaceship: Sprite = None
durable_spaceship: Sprite = None
fastest_spaceship: Sprite = None
choose: Sprite = None
second_tilemap: tiles.TileMapData = None
first_tilemap: tiles.TileMapData = None
choiceScene = 0
scene.set_background_color(15)
choiceScene = 1
first_tilemap = tilemap("""
    level1
""")
second_tilemap = tilemap("""
    level3
""")
third_tilemap = tilemap("""
    level5
""")
# High Speed
# Low Capacity
# Medium Durable
createFastestSpaceShip()
# Low Speed
# Medium Capacity
# High Durability
createDurableSpaceship()
# Medium Speed
# High Capacity
# Low Durability
createCapacitySpaceship()
choose = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . 2 . . . . . . . . . 
            . . . . . 2 2 2 . . . . . . . . 
            . . . . 2 2 2 2 2 . . . . . . . 
            . . . 2 2 2 2 2 2 2 . . . . . . 
            . . 2 2 2 2 2 2 2 2 2 . . . . . 
            . . . . 2 2 2 2 2 . . . . . . . 
            . . . . 2 2 2 2 2 . . . . . . . 
            . . . . 2 2 2 2 2 . . . . . . . 
            . . . . 2 2 2 2 2 . . . . . . . 
            . . . . 2 2 2 2 2 . . . . . . . 
            . . . . . 2 . 2 . . . . . . . . 
            . . . . . 1 . 1 . . . . . . . . 
            . . . . . 1 . 1 . . . . . . . .
    """),
    SpriteKind.Selector)
controller.move_sprite(choose, 100, 100)
choose.set_position(80, 95)
game.show_long_text("Choose a spaceship with the A button when arrow is on ",
    DialogLayout.TOP)

def on_forever():
    global portalDoor1, astronautSpeed
    if current_tilemap == first_tilemap:
        portalDoor1 = sprites.create(assets.image("""
            Portal1
        """), SpriteKind.Door1)
        tiles.place_on_random_tile(portalDoor1, assets.tile("""
            portalDoorLocation
        """))
    elif currentSpaceship == capacity_spaceship:
        astronautSpeed = capSpace_SpeedStatusBar.value
    elif currentSpaceship == fastest_spaceship:
        astronautSpeed = fastSpace_SpeedStatusBar.value
    elif currentSpaceship == durable_spaceship:
        astronautSpeed = durSpace_SpeedStatusBar.value
forever(on_forever)
