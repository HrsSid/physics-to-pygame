# Libraries
import pygame
import sys

import random

import pygameExtra

# Main class
class Sim:    
    def __init__(self, screenSize:tuple="FULLSCREEN", fps:int=120, customCursor:pygame.image=pygame.image.load("assets/Cursors/pointer_a.png")):
        """This function initializes the game window and some basic game variables.

        Args:
            screenSize (tuple, optional): The screen width and height. Defaults to "FULLSCREEN".
        """
        # initializing pygame
        pygame.init()
        
        # creating the screen
        self.screen_size = screenSize # globalizing the screen_size variable
        if self.screen_size == "FULLSCREEN": # checking if the screen should be fullscreen
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) # if it should be fullscreen, set the screen to fullscreen
        else: # otherwise set the screen to the specified size
            self.screen = pygame.display.set_mode(screenSize)
        
        # making the cursor invisible
        pygame.mouse.set_visible(0)
        
        # color variables -> RGB format
        self.color_white = (255, 255, 255)
        self.color_black = (0, 0, 0)
        self.color_red = (255, 0, 0)
        self.color_green = (0, 255, 0)
        self.color_blue = (0, 0, 255)
        self.color_yellow = (255, 255, 0)
        self.color_cyan = (0, 255, 255)
        self.color_magenta = (255, 0, 255)
        self.color_pink = (255, 192, 203)
        self.color_brown = (165, 42, 42)
        
        # cursor variables
        self.cursor_arrow = pygame.image.load("assets/Cursors/pointer_a.png")
        self.cursor_arrow_nw = pygame.image.load("assets/Cursors/pointer_e.png")
        self.cursor_pointer = pygame.image.load("assets/Cursors/hand_small_point.png")
        self.cursor_text = pygame.image.load("assets/Cursors/bracket_a_vertical.png")
        self.cursor_busy_circle = pygame.image.load("assets/Cursors/busy_circle_fade.png")
        self.cursor_busy_hourglass = pygame.image.load("assets/Cursors/busy_hourglass_outline_detail.png")
        self.cursor_disabled = pygame.image.load("assets/Cursors/disabled.png")
        self.cursor_hand_open = pygame.image.load("assets/Cursors/hand_small_open.png")
        self.cursor_hand_closed = pygame.image.load("assets/Cursors/hand_small_closed.png")
        self.cursor_zoom_in = pygame.image.load("assets/Cursors/zoom_in.png")
        self.cursor_zoom_out = pygame.image.load("assets/Cursors/zoom_out.png")
        self.cursor_x = pygame.image.load("assets/Cursors/cross_small.png")
        self.cursor_eye_open = pygame.image.load("assets/Cursors/look_a.png")
        self.cursor_plus = pygame.image.load("assets/Cursors/line_cross.png")
        self.cursor_minus = pygame.image.load("assets/Cursors/line_horizontal.png")
        self.cursor_target = pygame.image.load("assets/Cursors/target_a.png")
        self.cursor_direction_n = pygame.image.load("assets/Cursors/navigation_n.png")
        self.cursor_direction_e = pygame.image.load("assets/Cursors/navigation_e.png")
        self.cursor_direction_s = pygame.image.load("assets/Cursors/navigation_s.png")
        self.cursor_direction_w = pygame.image.load("assets/Cursors/navigation_w.png")
        
        # variables
        self.background = self.color_black # setting the default background color
        self.customCursor = pygameExtra.ImageSprite(customCursor, self.screen.get_width() / 2, self.screen.get_height() / 2) # setting the custom cursor
        self.customCursor.rect.size = (15, 15)
        
        self.clock = pygame.time.Clock() # creating a clock
        self.fps = fps # setting the max fps
    
    def run(self):
        # variables
        self.key = pygame.key.get_pressed() # getting the pressed keys if any
        
        sim.box.set_velocity([2, 1]) # resetting the velocity, you can set the velocity of the box here
        
        # applying the forces to the sprite
        self.box.rect.x += self.box.velocity[0]
        self.box.rect.y += self.box.velocity[1]
        
        # collision handler
        self.border_bottom = pygame.Rect(0, self.screen.get_height() - 10, self.screen.get_width(), 10) # creating the hit-box of the bottom border
        self.border_top = pygame.Rect(0, 0, self.screen.get_width(), 10) # creating the hit-box of the top border
        self.border_left = pygame.Rect(0, 0, 10, self.screen.get_height()) # creating the hit-box of the left border
        self.border_right = pygame.Rect(self.screen.get_width() - 10, 0, 10, self.screen.get_height()) # creating the hit-box of the right border
        
        if self.box.rect.colliderect(self.border_bottom): # checking if the box collides with the bottom border
            self.box.set_velocity([self.box.velocity[0], 0]) # setting the velocity to 0 if the box hits the bottom border
            self.box.rect.y = self.screen.get_height() - self.box.rect.height - 10 # putting the box on the correct position against the bottom border
        if self.box.rect.colliderect(self.border_top): # checking if the box collides with the top border
            self.box.set_velocity([self.box.velocity[0], 0]) # setting the velocity to 0 if the box hits the top border
            self.box.rect.y = 10 # putting the box on the correct position against the top border
        if self.box.rect.colliderect(self.border_left): # checking if the box collides with the left border
            self.box.set_velocity([0, self.box.velocity[1]]) # setting the velocity to 0 if the box hits the left border
            self.box.rect.x = 10 # putting the box on the correct position against the left border
        if self.box.rect.colliderect(self.border_right): # checking if the box collides with the right border
            self.box.set_velocity([0, self.box.velocity[1]]) # setting the velocity to 0 if the box hits the right border
            self.box.rect.x = self.screen.get_width() - self.box.rect.width - 10 # putting the box on the correct position against the right border
        
        # render handler
        self.screen.blit(self.box.image, (self.box.rect.x, self.box.rect.y)) # drawing the box onto the screen
        
        # exiting the project
        for event in pygame.event.get(): # checking for events
            if event.type == pygame.QUIT: # if the event is quit
                return False # then return false
        if self.key[pygame.K_ESCAPE]: # alternatively if the escape key is pressed
            return False # return false
        
        # rendering project defaults
        self.screen.blit(self.customCursor.image, (self.customCursor.rect.x, self.customCursor.rect.y)) # drawing the custom cursor onto the screen
        self.customCursor.update(pygame.mouse.get_pos()) # updating the custom cursor position to the mouse position
        
        # updating the screen
        self.clock.tick(self.fps) # ticking the clock
        pygame.display.update() # updating the screen
        self.screen.fill(self.background) # filling the screen with the background color to prevent flickering
        
        # returning true so the program continues to run
        return True
        

# Main
if __name__ == "__main__":
    sim = Sim(screenSize="FULLSCREEN", fps=120) # initializing the project
    sim.customCursor.image = sim.cursor_arrow_nw # setting the custom cursor
    
    sim.box = pygameExtra.MovingSprite(image=pygame.image.load("assets/Objects/tile_0026.png"), x=sim.screen.get_width() / 2, y=sim.screen.get_height() / 2, velocity=(0, 0), acceleration=(0, 0)) # initializing the moving sprite
    sim.box.rect.size = (15, 15) # changing the size of the hit-box
    
    running = True # creating the running variable
    while running: # while the running variable is true the project will continue to run
        running = sim.run() # if the project returns false the running variable will be set to false and therefore the while loop will stop
        
    # force quitting pygame
    pygame.quit()
