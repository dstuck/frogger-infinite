import logging
from abc import abstractmethod

import pygame as pg

import game_engine.game_states as game_states

LOGGER = logging.getLogger(__name__)


UP_DIRECTIONS = set(['north', 'up'])
LEFT_DIRECTIONS = set(['west', 'left'])
DOWN_DIRECTIONS = set(['south', 'down'])
RIGHT_DIRECTIONS = set(['east', 'right'])

class Screen:
    def __init__(self, surface):
        self.surface = surface
        self.adjacent_screens = {}
        self.player = None
        self.static_entities = []
        self.dynamic_entities = []
        self.pressed_keys = set()
        self.image = self.load_image()
        self.new_state = None

        self.setup_screen()

    @abstractmethod
    def load_image(self):
        pass

    @property
    def entities(self):
        return [self.player, *self.static_entities, *self.dynamic_entities]

    def get_size(self):
        return self.surface.get_width(), self.surface.get_height()

    def set_player(self, player):
        self.player = player

    @abstractmethod
    def setup_screen(self):
        pass

    def process_event(self, event):
        for entity in self.entities:
            entity.process_event(event)

    def update(self):
        new_rect = self.player.propose_move()
        if new_rect:
            new_screen = self.check_for_new_screen(new_rect)
            if new_screen:
                return new_screen

            if self.in_bounds(new_rect) and not self.check_collisions(new_rect):
                self.player.set_rect(new_rect)
        else:
            self.check_collisions(self.player.rect)

        for entity in self.entities:
            entity.update()
        self.pressed_keys = set()

    def draw(self):
        dirty_rects = []
        for entity in self.entities:
            entity_dirty_rects = entity.get_rects_to_update()
            if entity_dirty_rects:
                dirty_rects.extend(entity_dirty_rects)
                self.draw_screen(entity_dirty_rects)
                entity.draw(self.surface)
        ## Update vision
        # for rect in dirty_rects:
        #     self.surface.fill((60, 0, 0), rect)
        pg.display.update(dirty_rects)

    def draw_screen(self, rects):
        self.surface.blits(tuple((self.image, (rect.x, rect.y), rect) for rect in rects))
        # test_image = pg.Surface(self.get_size())
        # test_image.fill((100, 100, 100))
        # self.surface.blit(test_image, (0,0), pg.Rect(224, 454, 53, 39))

    def refresh_screen(self):
        self.surface.blit(self.image, (0, 0))
        for entity in self.entities:
            entity.draw(self.surface)

    def in_bounds(self, new_rect):
        return not (
            self._is_past_up(new_rect)
            or self._is_past_left(new_rect)
            or self._is_past_down(new_rect)
            or self._is_past_right(new_rect)
        )

    def check_collisions(self, new_rect):
        for entity in self.entities:
            if entity != self.player and entity.is_solid() and entity.rect.colliderect(new_rect):
                if entity.is_deadly():
                    self.new_state = game_states.DEAD
                LOGGER.debug("Colliding with", entity)
                return True
        return False

    def _is_past_up(self, rect):
        return rect.top < 0

    def _is_past_left(self, rect):
        return rect.left < 0

    def _is_past_down(self, rect):
        return rect.bottom > self.get_size()[1]

    def _is_past_right(self, rect):
        return rect.right > self.get_size()[0]

    def check_for_new_screen(self, rect):
        for key in self.adjacent_screens:
            if self.check_cardinal(rect, key) or self.check_custom_adjacent_screen(rect, key):
                LOGGER.debug('switching screens {}: {}'.format(key, self.adjacent_screens[key]))
                return self.adjacent_screens[key]

    def check_cardinal(self, rect, direction):
        if (
            (direction in UP_DIRECTIONS and self._is_past_up(rect))
            or (direction in DOWN_DIRECTIONS and self._is_past_down(rect))
        ):
            self.flip_vertically(self.player)
            return True
        if (
            (direction in LEFT_DIRECTIONS and self._is_past_left(rect))
            or (direction in RIGHT_DIRECTIONS and self._is_past_right(rect))
        ):
            self.flip_horizontally(self.player)
            return True
        return False

    def flip_horizontally(self, entity):
        initial_position = entity.position
        entity.position = (self.get_size()[0] - initial_position[0], initial_position[1])

    def flip_vertically(self, entity):
        initial_position = entity.position
        entity.position = (initial_position[0], self.get_size()[1] - initial_position[1])

    def check_custom_adjacent_screen(self, rect, key):
        return False
