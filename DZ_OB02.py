from abc import ABC, abstractmethod


class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

    # Возвращаем урон, который оружие наносит
    @abstractmethod
    def damage(self) -> int:
        pass


class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

    def damage(self) -> int:
        return 20  # Предположим, урон меча составляет 20 HP


class Bow(Weapon):
    def attack(self):
        return "Боец наносит удар из лука."

    def damage(self) -> int:
        return 15  # Урон из лука - 15 HP


class Fighter:
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def attack(self):
        print(self.weapon.attack())

    def inflict_damage(self, monster):
        monster.take_damage(self.weapon.damage())

    def changeWeapon(self, weapon: Weapon):
        self.weapon = weapon


class Monster:
    def __init__(self, health: int):
        self.health = health

    def take_damage(self, damage: int):
        self.health -= damage
        if self.health > 0:
            print(f"Монстру осталось {self.health} HP.")
        else:
            print("Монстр побежден!\n")


def demonstrate_battle(fighter, monster):
    fighter.attack()
    fighter.inflict_damage(monster)

# Создаем монстра с 50 HP
monster = Monster(50)

# Создание бойца с мечом
fighter = Fighter(Sword())

# Демонстрация боя с мечом
demonstrate_battle(fighter, monster)

# Меняем оружие на лук и снова демонстрируем боевые действия
fighter.changeWeapon(Bow())
demonstrate_battle(fighter, monster)