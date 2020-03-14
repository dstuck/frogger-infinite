from game_engine.screen import Screen


class FroggerFieldsScreen(Screen):
    def setup_screen(self):
        self.draw_screen()
        self.adjacent_screens['north'] = 'frogger_main'

    def draw_screen(self):
        self.surface.fill((0, 100, 0))
