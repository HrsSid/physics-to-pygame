# Libraries
import pygame
import sys

# Classes and extra features
class ImageSprite(pygame.sprite.Sprite):
    def __init__(self, image:pygame.image, x:int, y:int):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self, newCenter:tuple) -> None:
        self.rect.center = newCenter

class MovingSprite(pygame.sprite.Sprite):
    def __init__(self, image:pygame.image=pygame.image.load("assets/Objects/tile_0026.png"), x:int=0, y:int=0, velocity:list=[0, 0], acceleration:list=[0, 0]) -> pygame.sprite.Sprite:
        """Args:
            image (pygame.image, optional): The image sprite to be used. Defaults to pygame.image.load("assets/Objects/tile_0026.png").
            x (int, optional): The initial x position of the sprite. Defaults to 0.
            y (int, optional): The initial y position of the sprite. Defaults to 0.
            velocity (list, optional): The initial velocity of the sprite. Defaults to [0, 0].
            acceleration (list, optional): The initial acceleration of the sprite. FIXME - not yet utilized. Defaults to [0, 0].

        Returns:
            pygame.sprite.Sprite: A rectangular sprite that can be moved around the screen.
        """
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
        self.velocity = velocity
        self.acceleration = acceleration
    
    def get_velocity(self) -> list:
        """Returns:
            list: the velocity of the sprite
        """
        return [self.velocity[0], self.velocity[1]]
    def set_velocity(self, newVelocity:list) -> None:
        """Args:
            newVelocity (list): The new velocity values of the sprite
        """
        self.velocity = [newVelocity[0], newVelocity[1]*-1]

    def update(self, newCenter:tuple) -> None:
        """Args:
            newCenter (tuple): The new center values of the sprite
        """
        self.rect.center = newCenter
