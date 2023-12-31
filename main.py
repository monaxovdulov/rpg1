import random

WARRIOR = "бОГАТЫРЬ"
MAGE = "ТРАВНИК"
HUNTER = "БРОДЯЖНИК"

print("Выберете своего героя")
print(f"1 - {WARRIOR}")
print(f"2 - {MAGE}")
print(f"3 - {HUNTER}")
print()
choice = input("Введите номер вашего героя: ")

while choice not in ("1", "2", "3"):
    print("Нет такого варианта")
    choice = input("Введите номер вашего героя: ")

if choice == "1":
    print("Вы выбрали героя-воина!")
    name_hero = "Ваг-Дур Бесстрашный"
    class_hero = WARRIOR
    hp = 100
    power_attack = 15
    armor = 5
    ability_used = False  # Флаг для отслеживания использования способности
elif choice == "2":
    print("Вы выбрали героя-Мага!")
    name_hero = "Гаррик Вселенский Поработитель Огня"
    class_hero = MAGE
    hp = 70
    power_attack = 12
    armor = 5
    ability_used = False
elif choice == "3":
    print("Вы выбрали героя-Лучника!")
    name_hero = "Анг Свистящий Ветер"
    class_hero = HUNTER
    hp = 100
    power_attack = 15
    armor = 5
    ability_used = False

print("Ваше имя:", name_hero)
print("Ваш класс:", class_hero)
print("Здоровье:", hp)
print("Сила атаки:", power_attack)
print("Броня:", armor)

monsters = [
    {"name": "Гоблин", "hp": 30, "power_attack": 8},
    {"name": "Орк", "hp": 60, "power_attack": 15},
    {"name": "Дракон", "hp": 150, "power_attack": 30},
]

game_loop = True
while game_loop:
    monster = random.choice(monsters)
    print(f"\nВы встретили монстра: {monster['name']}")
    print("Бой начинается!")

    while True:
        print("\nВаш ход:")
        print("1 - Атаковать")
        print("2 - Поставить блок")
        if not ability_used:  # Если способность не использована
            print("3 - Использовать способность (одноразово)")

        choice = input("Выберите действие: ")
        armor_use = False
        if choice == "1":
            monster["hp"] = monster["hp"] - power_attack
            print(f"Вы атакуете монстра и наносите {power_attack} урона. У монстра осталось {monster['hp']} здоровья.")
        elif choice == "2":
            armor_use = True
            print("Вы ставите блок и снижаете получаемый урон.")
        elif choice == "3" and not ability_used:
            power_attack *= 2  # Удвоение силы атаки при использовании способности
            ability_used = True
            print("Вы использовали способность и удвоили свою силу атаки.")
        else:
            print("Вы ничего не сделали.")

        if monster["hp"] <= 0:
            print(f"Вы победили {monster['name']}!")
            print("Ваши характеристики увеличены + 3")
            hp += 3
            power_attack += 3
            armor += 3
            ability_used = False
            break

        # Ход монстра
        print(f"Ход: {monster['name']}")

        if armor_use:
            damage = max(0, monster['power_attack'] + armor)
            hp = hp - damage
        else:
            damage = monster['power_attack']
            hp = hp - damage
        print(f"Монстр атакует и наносит {damage } урона."
              f" У {name_hero} осталось {hp} здоровья.")

        if hp <= 0:
            print(f"Вы проиграли! Игра окончена!")
            game_loop = False
            break

