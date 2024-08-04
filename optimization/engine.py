import random

from particles.Particle import Particle


def engine(fitness_func, num, k,
           dim, local_wgh, glb_wgh):
    particles = []
    glb_best_pos = [0] * dim
    glb_best_fitness = float('inf')

    for _ in range(num):
        pos = [random.uniform(-5.12, 5.12) for _ in range(dim)]
        particle = Particle(pos)
        particles.append(particle)

    for _ in range(k):
        for particle in particles:
            particle.update_velocity(glb_best_pos, local_wgh, glb_wgh)
            particle.update_position()
            particle.evaluate_fitness(fitness_func)

            if particle.best_fitness < glb_best_fitness:
                glb_best_pos = particle.best_pos
                glb_best_fitness = particle.best_fitness

    return glb_best_fitness
