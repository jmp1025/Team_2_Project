import arcade

class PhysicsEngine():
    def __init__(self, entity, gravity_const, ground_friction_const, air_resistance_const=1, initial_velocity=[0,0], max_move_speed=None):
        self.entity = entity
        self.gravity_const = gravity_const
        self.ground_friction_const = ground_friction_const
        self.air_resistance_const = air_resistance_const
        self.velocity = initial_velocity
        self.max_move_speed = max_move_speed
        self.in_free_fall = False

    def update(self, walls):
        # check for floors
        self.check_for_floors(walls)
        
        if self.in_free_fall: # entity in free fall
            self.velocity[0] = self.velocity[0] / self.air_resistance_const # calculate change in velocity for air resistance
            self.velocity[1] += self.gravity_const # calculate change in velocity for gravity
        else: # entity on ground
            self.velocity[0] = self.velocity[0] / self.ground_friction_const # calculate friction
            self.velocity[1] = self.entity.change_y # entity jump

        # movement in x direction
        self.velocity[0] += self.entity.change_x
        
        #check for walls
        self.check_for_walls(walls)

        # maximum movement speed calculation
        if self.max_move_speed != None:
            if self.velocity[0] > self.max_move_speed:
                self.velocity[0] = self.max_move_speed
            elif abs(self.velocity[0]) > self.max_move_speed:
                self.velocity[0] = -self.max_move_speed

        # change position based on the calculated velocity
        self.entity.center_x += self.velocity[0]
        self.entity.center_y += self.velocity[1]

    def check_for_walls(self, walls):
        """ check for collisions with walls """
        for wall in walls.sprite_list:           
            if ((self.entity.top - 10) > wall.bottom) and ((self.entity.bottom + 10) < wall.top) and ((wall.left - self.entity.right) <= 0) and ((wall.left - self.entity.right) > -60):
                # left
                self.entity.right = wall.left
                self.velocity[0] = self.velocity[0] * -0.5
            if ((self.entity.top - 10) > wall.bottom) and ((self.entity.bottom + 10) < wall.top) and ((self.entity.left - wall.right) <= 0) and ((self.entity.left - wall.right) > -60):
                # right
                self.entity.left = wall.right
                self.velocity[0] = self.velocity[0] * -0.5

    def check_for_floors(self, walls):
        """ Check for collisions with floors and ceilings """
        for wall in walls.sprite_list:
            if (self.entity.right - 1 > wall.left) and (self.entity.left + 1 < wall.right) and ((wall.bottom - self.entity.top) <= 0) and ((wall.bottom - self.entity.top) > -60):
                self.velocity[1] = self.velocity[1] * (-0.4)
            else:
                self.in_free_fall = True
            if self.in_free_fall and (self.entity.right - 1 > wall.left) and (self.entity.left + 1 < wall.right) and ((self.entity.bottom - wall.top) <= 0) and ((self.entity.bottom - wall.top) > -60):
                self.entity.bottom = wall.top
                self.velocity[1]
                self.in_free_fall = False
                break