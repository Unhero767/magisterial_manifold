import pygame
class PhysicsEngine:
    def check_collision(self, player_rect, walls):
        for wall in walls:
            if wall.stability > 0.5:
                w_rect = pygame.Rect(wall.start[0], wall.start[1], 
                                    abs(wall.end[0]-wall.start[0])+5, 
                                    abs(wall.end[1]-wall.start[1])+5)
                if player_rect.colliderect(w_rect): return True
        return False
