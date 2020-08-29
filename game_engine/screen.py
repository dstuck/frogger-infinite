import logging
from abc import abstractmethod

import pygame as pg

import game_engine.game_states as game_states

LOGGER = logging.getLogger(__name__)


UP_DIRECTIONS = set(['north', 'up'])
LEFT_DIRECTIONS = set(['west', 'left'])
DOWN_DIRECTIONS = set(['south', 'down'])
RIGHT_DIRECTIONS = set(['east', 'right'])

N_SUCCESS_FOR_VICTORY = 5

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
        self.new_screen = None
        self.successes = 0

        self.setup_screen()

    @abstractmethod
    def load_image(self):
        pass

    @property
    def entities(self):
        return [self.player, *self.dynamic_entities, *self.static_entities]

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
        """
        Update all entities in screen for this tic
        :return:
        """
        for entity in self.entities:
            entity.update()
            self.attempt_move(entity)

        if self.player.is_dead:
            self.new_state = game_states.DEAD
        elif self.player.is_home:
            self.successes += 1
            if self.successes >= N_SUCCESS_FOR_VICTORY:
                self.successes = 0
                self.new_state = game_states.VICTORY
            else:
                self.new_state = game_states.DEAD

        self.pressed_keys = set()
        self.check_player_for_adjacent_screen()
        if self.new_screen:
            screen = self.new_screen
            self.new_screen = None
            return screen

    def attempt_move(self, entity):
        if entity.next_move or entity == self.player:
            next_position = entity.pop_next_position()
            proposed_rect = entity.rect.copy()
            proposed_rect.center = next_position
            # TODO: inbounds should check after screen change
            if not self.check_entity_collisions(entity, proposed_rect) and self.in_bounds(proposed_rect):
                entity.position = next_position

    def draw(self):
        dirty_rects = []
        draw_methods_to_run = []
        for entity in reversed(self.entities):
            entity_dirty_rects = entity.get_rects_to_update()
            if entity_dirty_rects:
                dirty_rects.extend(entity_dirty_rects)
                self.draw_screen(entity_dirty_rects)
                # don't want to overwrite previous entities with background so draw entities later
                draw_methods_to_run.append(entity.draw)
        for draw_method in draw_methods_to_run:
            draw_method(self.surface)
        pg.display.update(dirty_rects)

    def draw_screen(self, rects):
        self.surface.blits(tuple((self.image, (rect.x, rect.y), rect) for rect in rects))

    def refresh_screen(self):
        self.surface.blit(self.image, (0, 0))
        for entity in self.entities:
            entity.draw(self.surface)

    def in_bounds(self, new_rect):
        return not (
            self._is_out_up(new_rect)
            or self._is_out_left(new_rect)
            or self._is_out_down(new_rect)
            or self._is_out_right(new_rect)
        )

    def check_entity_collisions(self, entity, proposed_rect):
        if not entity.is_solid():
            return False
        for other in self.entities:
            if other == entity:
                continue
            if other.rect.colliderect(proposed_rect):

                entity.collide(other)
                other.collide(entity)
                if other.is_solid():
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

    def _is_out_up(self, rect):
        return rect.bottom < 0

    def _is_out_left(self, rect):
        return rect.right < 0

    def _is_out_down(self, rect):
        return rect.top > self.get_size()[1]

    def _is_out_right(self, rect):
        return rect.left > self.get_size()[0]

    def check_player_for_adjacent_screen(self):
        rect = self.player.rect.copy()
        for key in self.adjacent_screens:
            if self.check_cardinal(rect, key) or self.check_custom_adjacent_screen(rect, key):
                LOGGER.info('switching screens {}: {}'.format(key, self.adjacent_screens[key]))
                self.new_screen = self.adjacent_screens[key]

    def check_cardinal(self, rect, direction):
        if direction in UP_DIRECTIONS and self._is_past_up(rect):
            self.player.rect.bottom = self.get_size()[1]
            return True
        elif direction in DOWN_DIRECTIONS and self._is_past_down(rect):
            self.player.rect.top = 0
            return True
        elif direction in LEFT_DIRECTIONS and self._is_past_left(rect):
            self.player.rect.left = self.get_size()[0]
            return True
        elif direction in RIGHT_DIRECTIONS and self._is_past_right(rect):
            self.player.rect.left = 0
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
