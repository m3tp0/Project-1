from sprite_object import *
from npc import *
from random import choices, randrange


class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_sprite_path = 'resources/sprites/npc/'
        self.static_sprite_path = 'resources/sprites/static_sprites/'
        self.anim_sprite_path = 'resources/sprites/animated_sprites/'
        add_sprite = self.add_sprite
        add_npc = self.add_npc
        self.npc_positions = {}

        # spawn npc
        self.enemies = 20  # npc count
        self.npc_types = [SoldierNPC, CacoDemonNPC, CyberDemonNPC]
        self.weights = [70, 20, 10]
        self.restricted_area = {(i, j) for i in range(10) for j in range(10)}
        self.spawn_npc()

        # sprite map
        # Area 1
        add_sprite(AnimatedSprite(game))
        add_sprite(AnimatedSprite(game, pos=(1.5, 1.5)))
        add_sprite(AnimatedSprite(game, pos=(1.5, 8.5)))
        add_sprite(AnimatedSprite(game, pos=(14.5, 1.5)))
        add_sprite(AnimatedSprite(game, pos=(1.5, 17.5)))
        add_sprite(AnimatedSprite(game, pos=(14.5, 17.5)))
        add_sprite(AnimatedSprite(game, pos=(14.5, 15.5)))
        add_sprite(AnimatedSprite(game, pos=(14.5, 13.5)))
        add_sprite(AnimatedSprite(game, pos=(14.5, 8.5)))
        add_sprite(AnimatedSprite(game, pos=(11.5, 4.5)))
        add_sprite(AnimatedSprite(game, pos=(1.5, 10.5)))

        # Area 2
        add_sprite(AnimatedSprite(game, pos=(35.5, 4.5)))
        add_sprite(AnimatedSprite(game, pos=(35.5, 23.5)))
        add_sprite(AnimatedSprite(game, pos=(18.5, 23.5)))
        add_sprite(AnimatedSprite(game, pos=(18.5, 10.5)))
        add_sprite(AnimatedSprite(game, pos=(24.5, 13.5)))
        add_sprite(AnimatedSprite(game, pos=(29.5, 13.5)))
        add_sprite(AnimatedSprite(game, pos=(24.5, 20.5)))
        add_sprite(AnimatedSprite(game, pos=(29.5, 20.5)))

        # Area 3
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(26.5, 28.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(1.5, 28.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(1.5, 42.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(25.5, 42.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(25.5, 35.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(1.5, 35.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(7.5, 32.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(14.5, 30.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(8.5, 44.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(11.5, 44.5)))

        # Area 4
        add_sprite(AnimatedSprite(game, pos=(14.5, 46.5)))
        add_sprite(AnimatedSprite(game, pos=(4.5, 47.5)))
        add_sprite(AnimatedSprite(game, pos=(4.5, 57.5)))
        add_sprite(AnimatedSprite(game, pos=(25.5, 57.5)))
        add_sprite(AnimatedSprite(game, pos=(25.5, 47.5)))
        add_sprite(AnimatedSprite(game, pos=(17.5, 57.5)))

        # Area 5
        add_sprite(AnimatedSprite(game, pos=(1.5, 62.5)))
        add_sprite(AnimatedSprite(game, pos=(1.5, 74.5)))
        add_sprite(AnimatedSprite(game, pos=(36.5, 74.5)))
        add_sprite(AnimatedSprite(game, pos=(36.5, 62.5)))
        add_sprite(AnimatedSprite(game, pos=(16.5, 65.5)))
        add_sprite(AnimatedSprite(game, pos=(20.5, 65.5)))
        add_sprite(AnimatedSprite(game, pos=(20.5, 69.5)))
        add_sprite(AnimatedSprite(game, pos=(16.5, 69.5)))
        add_sprite(AnimatedSprite(game, pos=(7.5, 67.5)))
        add_sprite(AnimatedSprite(game, pos=(29.5, 67.5)))
        add_sprite(AnimatedSprite(game, pos=(29.5, 58.5)))
        add_sprite(AnimatedSprite(game, pos=(31.5, 58.5)))

        # Area 6
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(27.5, 57.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(35.5, 60.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(35.5, 57.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(27.5, 29.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(35.5, 29.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(35.5, 38.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(35.5, 41.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(27.5, 41.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(82.5, 36.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(30.5, 46.5)))

    def spawn_npc(self):
        for i in range(self.enemies):
            npc = choices(self.npc_types, self.weights)[0]
            pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)
            while (pos in self.game.map.world_map) or (pos in self.restricted_area):
                pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)
            self.add_npc(npc(self.game, pos=(x + 0.5, y + 0.5)))

    def check_win(self):
        if not len(self.npc_positions):
            self.game.object_renderer.win()
            pg.display.flip()
            pg.time.delay(1500)
            self.game.new_game()

    def update(self):
        self.npc_positions = {npc.map_pos for npc in self.npc_list if npc.alive}
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]
        self.check_win()

    def add_npc(self, npc):
        self.npc_list.append(npc)

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)
