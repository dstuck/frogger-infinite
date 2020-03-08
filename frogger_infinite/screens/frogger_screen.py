from frogger_infinite.entities.player import Player
from game_engine.screen import Screen


class FroggerScreen(Screen):

    def setup_screen(self):
        init_position = (
            self.surface.get_size()[1]*0.5,
            self.surface.get_size()[0] - Player.IMAGE_SIZE[0] * 0.5,
        )
        player = Player(init_position)
        self.entities.append(player)
        self.draw_screen()

    def draw_screen(self):
        self.surface.fill((0, 40, 0))
