from game_engine.screen import Screen


class FroggerScreen(Screen):
    def setup_screen(self):
        self.draw_screen()

    def draw_screen(self):
        self.surface.fill((0, 40, 0))
