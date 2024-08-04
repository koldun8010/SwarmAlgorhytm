import random


class Particle:
    def __init__(self, pos):
        self.pos = pos
        self.speed = [random.uniform(-0.01, 0.01) for _ in range(len(pos))]
        self.best_pos = pos
        self.best_fitness = float('inf')

    def update_velocity(self, glb_best_pos, local_wgh, glb_wgh):
        for i in range(len(self.speed)):
            r1 = random.random()
            r2 = random.random()
            local = local_wgh * r1 * (self.best_pos[i] - self.pos[i])
            glb = glb_wgh * r2 * (glb_best_pos[i] - self.pos[i])
            self.speed[i] = self.speed[i] + local + glb

    def update_position(self):
        for i in range(len(self.pos)):
            if self.pos[i] + self.speed[i] > 5.12:
                self.pos[i] = 5.12
            elif self.pos[i] + self.speed[i] < -5.12:
                self.pos[i] = -5.12
            else:
                self.pos[i] += self.speed[i]

    def evaluate_fitness(self, fitness_function):
        fitness = fitness_function(self.pos[0], self.pos[1])
        if fitness < self.best_fitness:
            self.best_pos = self.pos
            self.best_fitness = fitness
