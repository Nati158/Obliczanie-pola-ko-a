import math

def oblicz_pole_kola(promien):
    return math.pi * promien ** 2

promien = float(input("Podaj promień koła: "))
pole = oblicz_pole_kola(promien)
print("Pole koła o promieniu", promien, "to:", pole)
