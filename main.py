from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

#Create Black Magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 124, "black")
blizzard= Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 10, 1, "black")
quake = Spell("Quake", 10, 100, "black")

#Create White Magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

#Create some Items
potion = Item("Potion", 'potion', 'Heals 50 HP', 50)
hipotion = Item("Hi-Potion", 'potion', 'Heals 100 HP', 100)
superpotion = Item("Super-Potion", 'potion', 'Heals 500 HP', 500)
elixer = Item("Elixer", 'elixer', 'Fully restores HP/MP of one party member', 9999)
hielixer = Item("Mega-Elixer", 'elixer', 'Fully restores HP/MP of one party member', 9999)
grenade = Item("Grenade", "attack", "Deals 500 damage", 500)
player_spells = [fire, thunder, blizzard, meteor, quake, cure, cura]
player_items = [{'item': potion, 'quantity':15}, {'item':hipotion, 'quantity':5}, {'item':superpotion, 'quantity':5},{'item': elixer, 'quantity':5},{'item':hielixer, 'quantity':5},{'item':grenade, 'quantity':5}]

#Instantiate Items
player = Person(460, 65, 60,34, player_spells, player_items)
enemy = Person(1200, 65, 45, 25,[], [] )

running = True
i = 0
print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print("======================================")
    player.choose_action()
    choice = input("Choose action: ")
    index = int(choice) -1


    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for ", dmg, "points of damamge, Enemy HP : ", enemy.get_hp())
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose magic: ")) -1

        if magic_choice == -1:
            continue
        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(bcolors.FAIL + "\n Not enough MP\n" + bcolors.ENDC)
            continue
        player.reduce_mp(spell.cost)

        if spell.type == "white":
            player.heal(magic_dmg)
            print(bcolors.OKGREEN + "\n" + spell.name + " heals for", str(magic_dmg), "HP" + bcolors.ENDC)
        elif spell.type == "black":
            enemy.take_damage(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + ' deals', str(magic_dmg), "points of damage" + bcolors.ENDC)

    elif index == 2:
        player.choose_item()
        item_choice = int(input("Choose item: "))-1

        if item_choice == -1:
            continue
        item = player.items[item_choice]
        if player.items[item_choice]['quantity']== 0:
            print(bcolors.FAIL + '\n' + "None left..." + bcolors.ENDC)
            continue
        player.items[item_choice]['quantity'] -=1

        if item['item'].types == 'potion':
            player.heal(item['item'].prop)
            print(bcolors.OKGREEN + "\n" + item['item'].name + "heals for ", str(item['item'].prop), "HP" + bcolors.ENDC)
        elif item['item'].types == 'elixer':
            player.hp = player.maxhp
            player.mp = player.maxmp
            print(bcolors.OKGREEN + '\n' + item['item'].name + " fully restores HP/MP " + bcolors.ENDC)
        elif item['item'].types == 'attack':
            enemy.take_damage(item['item'].prop)
            print(bcolors.FAIL + "\n" + item['item'].name + ' deals', str(item['item'].prop), 'point of damage' + bcolors.ENDC)
    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemey attacts for ", enemy_dmg, "points of damage, Player HP: ", player.get_hp())

    print("-----------------------------------------------------------------------")
    print("ENEMY HP: ", bcolors.FAIL + str(enemy.get_hp())+ "/" + str(enemy.get_mx_hp())+ bcolors.ENDC)


    print("Your HP: ", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_mx_hp()) + bcolors.ENDC)
    print("Your MP: ", bcolors.OKGREEN + str(player.get_mp()) + "/" + str(player.get_mx_mp()) + bcolors.ENDC)
    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN  + "You win!" + bcolors.ENDC)
        running = False

    elif player.get_hp() == 0:
        print(bcolors.FAIL + "Your enemy has defeated you!" + bcolors.ENDC)
        running = False








