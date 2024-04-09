class Personaje:
    def __init__(self, vida, ataque, defensa, alcance):
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.alcance = alcance

class Caballero(Personaje):
    def __init__(self):
        super().__init__(vida=4, ataque=2, defensa=4, alcance=2)

class Guerrero(Personaje):
    def __init__(self):
        super().__init__(vida=2, ataque=4, defensa=2, alcance=4)

class Arquero(Personaje):
    def __init__(self):
        super().__init__(vida=2, ataque=4, defensa=1, alcance=8)

caballero = Caballero()
guerrero = Guerrero()
arquero = Arquero()

print("Propiedades del Caballero:")
print(f"Vida: {caballero.vida}")
print(f"Ataque: {caballero.ataque}")
print(f"Defensa: {caballero.defensa}")
print(f"Alcance: {caballero.alcance}")

print("\nPropiedades del Guerrero:")
print(f"Vida: {guerrero.vida}")
print(f"Ataque: {guerrero.ataque}")
print(f"Defensa: {guerrero.defensa}")
print(f"Alcance: {guerrero.alcance}")

print("\nPropiedades del Arquero:")
print(f"Vida: {arquero.vida}")
print(f"Ataque: {arquero.ataque}")
print(f"Defensa: {arquero.defensa}")
print(f"Alcance: {arquero.alcance}")