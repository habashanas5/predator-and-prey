import matplotlib.pyplot as plt

predator_population = 15
prey_population = 100
prey_birth_fraction = 2
predator_birth_fraction = 0.01
predator_death_proportionality_constant = 1.06
prey_death_proportionality_constant = 0.02
dt = 0.01  # Time step
duration = 12  # Total duration of the simulation in months
iteration = int(duration / dt)
t= 0

Predator = []
Prey = []
T = []

for i in range(iteration):
    prey_births = prey_birth_fraction * prey_population
    prey_deaths = (prey_death_proportionality_constant * predator_population) * prey_population
    predator_births = (predator_birth_fraction * prey_population) * predator_population
    predator_deaths = predator_death_proportionality_constant * predator_population
    prey_population += (prey_births - prey_deaths) * dt
    predator_population += (predator_births - predator_deaths) * dt

    t = i * dt
    T.append(t)
    Prey.append(prey_population)
    Predator.append(predator_population)

plt.plot(T, Prey, color="red", label="Prey")
plt.plot(T, Predator, color="blue", label="Predator")

plt.xlabel("Time")
plt.ylabel("Population")
plt.title("predator & prey")
plt.legend()
plt.grid(True)
plt.show()
