#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Gao hongfei
# Time: 2018.03.01

# 全局变量
SCREEN_SIZE = (640, 480)
NEST_POSITION = (320, 240)
NEST_SIZE = 40
ANT_COUNT = 20

import pygame
from pygame.locals import *
from gameobjects.vector2 import Vector2
from random import randint, choice
from sys import exit


class Entity(object):
    def __init__(self, world, name, image):
        self.speed = 0
        self.name = name
        self.image = image
        self.world = world
        self.location = Vector2(0, 0)
        self.brain = StateMachine()
        self.destination = Vector2(0, 0)

    def render(self, surface):
        x, y = self.location
        w, h = self.image.get_size()
        # TODO CHANGE AFTER
        surface.blit(self.image, (x, y))

    def process(self, time_passed):
        self.brain.think()
        if self.speed > 0 and self.location != self.destination:
            vec_to_destination = self.destination - self.location
            distance_to_destination = vec_to_destination.get_length()
            heading = vec_to_destination.get_normalized()
            travel_distance = min(
                distance_to_destination,
                time_passed * self.speed)
            self.location = self.location + heading * travel_distance


class World(object):
    def __init__(self):
        self.entities = {}
        self.entity_id = 0
        self.background = pygame.surface.Surface(SCREEN_SIZE).convert()
        self.background.fill((255, 255, 255))
        pygame.draw.circle(self.background, (200, 255, 200),
                           NEST_POSITION, int(NEST_SIZE))

    def process(self, time_passed):
        time_passed_seconds = time_passed / 1000.0
        for entity in self.entities.itervalues():
            entity.process(time_passed_seconds)

    def render(self, surface):
        surface.blit(self.background, (0, 0))
        for entity in self.entities.itervalues():
            entity.render(surface)

    def add_entity(self, entity):
        self.entities[self.entity_id] = entity
        entity.id = self.entity_id
        self.entity_id += 1

    def remove_entity(self, entity):
        del self.entities[entity.id]

    def get_close_entity(self, name, location, range=100.):
        location = Vector2(*location)
        for entity in self.entities.itervalues():
            if entity.name == name:
                distance = location.get_distance_to(entity.location)
                if distance < range:
                    return entity
        return None


class Ant(Entity):
    def __init__(self, world, image):
        Entity.__init__(self, world, "ant", image)
        self.carry_image = None
        exploring_state = AntStateExploring(self)
        # seeking_state = AntStateSeeking(self)
        # delivering_state = AntStateDelivering(self)
        # hunting_state = AntStateHunting(self)
        self.brain.add_state(exploring_state)
        # self.brain.add_state(seeking_state)
        # self.brain.add_state(delivering_state)
        # self.brain.add_state(hunting_state)
        self.carry_image = None

    def carry(self, image):
        self.carry_image = image

    def render(self, surface):
        Entity.render(self, surface)
        if self.carry_image:
            x, y = self.location
            w, h = self.carry_image.get_size()
            surface.blit(self.carry_image, (x - w, y - h / 2))

    def drop(self, surface):
        if self.carry_image:
            x, y = self.location
            w, h = self.carry_image.get_size()
            surface.blit(self.carry_image, (x - w, h - h / 2))
            self.carry_image = None


class Spider(Entity):
    def __init__(self):
        pass


class Leaf(Entity):
    def __init__(self, world, image):
        Entity.__init__(self, world, "leaf", image)


class State(object):
    def __init__(self, name):
        self.name = name

    def do_action(self):
        pass

    def check_conditions(self):
        pass

    def entry_actions(self):
        pass

    def exit_actions(self):
        pass


class AntStateExploring(State):
    def __init__(self, ant):
        State.__init__(self, "exploring")
        self.ant = ant

    def random_destination(self):
        w, h = SCREEN_SIZE
        self.ant.destination = Vector2(randint(0, w), randint(0, h))

    def do_actions(self):
        if randint(1, 20) == 1:
            self.random_destination()

    def check_conditions(self):
        leaf = self.ant.world.get_close_entity("leaf", self.ant.location)
        if leaf is not None:
            self.ant.leaf_id = leaf.id
            return "seeking"
        spider = self.ant.world.get_close_entity(
            "spider", NEST_POSITION, NEST_SIZE)
        if spider is not None:
            if self.ant.location.get_distance_to(spider.location) < 100.:
                self.ant.spider_id = spider.id
                return "hunting"
        return None

    def entry_actions(self):
        self.ant.speed = 120. + randint(-30, 30)
        self.random_destination()


class StateMachine(object):
    def __init__(self):
        self.states = {}
        self.active_state = None

    def add_state(self, state):
        self.states[state.name] = state

    def think(self):
        if self.active_state is None:
            return
        self.active_state.do_actions()
        new_state_name = self.active_state.check_conditions()
        if new_state_name is not None:
            self.set_state(new_state_name)

    def set_state(self, new_state_name):
        if self.active_state is not None:
            self.active_state.exit_actions()
        self.active_state = self.states[new_state_name]
        self.active_state.entry_actions()


def run_game():
    pygame.init()
    w, h = SCREEN_SIZE
    screen = pygame.display.set_mode((SCREEN_SIZE), 0, 32)
    world = World()
    world.render(screen)
    ant_image = pygame.image.load("ant.png").convert_alpha()
    leaf_image = pygame.image.load("leaf.png").convert_alpha()
    clock = pygame.time.Clock()

    # generate ant
    for i in range(ANT_COUNT):
        ant = Ant(world, ant_image)
        ant.location = Vector2(randint(0, w), randint(0, h))
        # ant.render(screen)
        ant.brain.set_state("exploring")
        world.add_entity(ant)

    done = True
    while done:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        time_passed = clock.tick(30)
        # if randint(1,10) == 1:
        #     leaf = Leaf(world, leaf_image)
        #     # leaf.render(screen)
        #     leaf.location = Vector2(randint(0,w),randint(0,h))
        #     world.add_entiyt(leaf)

        world.process(time_passed)
        world.render(screen)
        pygame.display.update()


if __name__ == "__main__":
    run_game()
