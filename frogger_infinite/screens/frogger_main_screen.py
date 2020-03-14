from game_engine.screen import Screen


class FroggerMainScreen(Screen):
    def setup_screen(self):
        self.draw_screen()
        self.adjacent_screens['south'] = 'frogger_fields'

    def draw_screen(self):
        self.surface.fill((0, 0, 40))
