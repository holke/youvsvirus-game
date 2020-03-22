import pygame
from img_lib import get_image
from pygame.time import get_ticks as time_now


class AbstractHuman(object):
    """
        Common Base Class for Human and Player
    """

    def __init__(self):
        self.posx = 0
        self.posy = 0
        self.movx = 0
        self.movy = 0
        self.state = 'well'
        self.collisions_active = True
        self.time_infected = None
        self.img = None

        self.imgcode = None

    def check_state(self):
        """
            Check and update this human's infection state, based on time elapsed since infection.
        """
        self.model.set_state(self)

        if (self.state == 'dead'):
            self.change_speed(0)
            self.collisions_active = False

        self.img = pygame.transform.scale(get_image(self.imgcode[self.state]), (2*self.r, 2*self.r))

    def infection(self):
        """
            Infects this human with the virus.
        """
        if self.state in ['recovered','ill','dead']: 
            return
        self.state = 'infected'
        self.time_infected = time_now()

    def render_img(self):
        """
            Render this human to the screen.
        """
        self.screen.blit(self.img, (self.posx, self.posy) )