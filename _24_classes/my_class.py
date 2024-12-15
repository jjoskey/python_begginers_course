# class Ork:
#     def __init__(self, *, level: int) -> None:
#         self.level = level
#         self.health_points = 100 * level
#         self.attack_power = 10 * level
    
#     def attack(self):
#         print(f'Ork attacks with {self.attack_power} power')

#     def __str__(self) -> str:
#         return f'Ork (level: {self.level}), hp: {self.health_points}'
    
#     def level_up(self, level):
#         self.level += level


# ork = Ork(level=2)
# print(ork.level)
# print(ork.health_points)

# ork.attack()

# ork.level_up(2)

# print(ork.level)
# print(ork)


# class Elf:
#     def __init__(self, *, level: int) -> None:
#         self.level = level
#         self.health_points = 50 * level
#         self.attack_power = 15 * level

#     def attack(self):
#         print(f'Elf attacks with {self.attack_power} power')
    
#     def __str__(self) -> str:
#         return f'Elf (level: {self.level}), hp: {self.health_points}'
    






# class Character:
#     def __init__(self, *, level: int) -> None:
#         self.level = level
#         self.health_points = self.base_health_points * level
#         self.attack_power = self.base_attack_power * level

#     def attack(self, *, target: 'Character') -> None:
#         print(
#             f'{self.character_name} attacks {target.character_name} ({target.health_points} health_points) '
#             f'with {self.attack_power} power.'
#         )
#         target.health_points -= self.attack_power
#         print(f'After attack {target.character_name} hp has {target.health_points}')

#     def is_alive(self) -> bool:
#         return self.health_points > 0

#     def __str__(self) -> str:
#         return f'{self.character_name} (level: {self.level}, hp: {self.health_points})'
    
# class Ork(Character):
#     base_health_points = 100
#     base_attack_power = 10
#     character_name = 'Ork'


# class Elf(Character):
#     base_health_points = 50
#     base_attack_power = 15
#     character_name = 'Elf'


# def fight(*, character_1: Character, character_2: Character) -> None:
#     while character_1.is_alive() and character_2.is_alive():
#         character_1.attack(target=character_2)
#         if character_2.is_alive():
#             character_2.attack(target=character_1)
    
#     print(f'Character 1: {character_1}, is_alive: {character_1.is_alive()}')
#     print(f'Character 2: {character_2}, is_alive: {character_2.is_alive()}')


# ork = Ork(level=1)
# elf = Elf(level=3)

# fight(character_1=ork, character_2=elf)





class Character:
    def __init__(self, *, level: int) -> None:
        self.level = level
        self.health_points = self.base_health_points * level
        self.attack_power = self.base_attack_power * level

    def attack(self, *, target: 'Character') -> None:
        target.got_damage(damage=self.attack_power)

    def got_damage(self, *, damage: int) -> None:
        damage = damage * (100 - self.defence) / 100
        damage = round(damage)
        self.health_points -= damage

    def is_alive(self) -> bool:
        return self.health_points > 0
    
    @property
    def defence(self) -> int:
        defence = self.base_defence * self.level
        return defence
    
    @property
    def max_health_points(self) -> int:
        return self.level * self.base_health_points
    
    def health_point_percent(self):
        return self.health_points / self.max_health_points * 100

    def __str__(self) -> str:
        return f'{self.character_name} (level: {self.level}, hp: {self.health_points})'
    
class Ork(Character):
    base_health_points = 100
    base_attack_power = 10
    base_defence = 15
    character_name = 'Ork'

    @property
    def defence(self) -> int:
        defence = super().defence
        if self.health_points < 50:
            defence *= 3

        return defence


class Elf(Character):
    base_health_points = 50
    base_attack_power = 15
    base_defence = 10
    character_name = 'Elf'

    def attack(self, *, target: Character) -> None:
        attack_power = self.attack_power
        if target.health_point_percent() < 60:
            attack_power = self.attack_power * 3
        target.got_damage(damage=attack_power)


def fight(*, character_1: Character, character_2: Character) -> None:
    while character_1.is_alive() and character_2.is_alive():
        character_1.attack(target=character_2)
        if character_2.is_alive():
            character_2.attack(target=character_1)
    
    print(f'Character 1: {character_1}, is_alive: {character_1.is_alive()}')
    print(f'Character 2: {character_2}, is_alive: {character_2.is_alive()}')


ork = Ork(level=1)
elf = Elf(level=1)

fight(character_1=ork, character_2=elf)