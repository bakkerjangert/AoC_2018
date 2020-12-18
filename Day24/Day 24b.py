import operator
class Group(object):
    def __init__(self, units, hp, ap, init, att, imm, weak):
        self.units = units
        self.hp = hp
        self.ap = ap
        self.init = init
        self.att = att
        self.imm = imm
        self.weak = weak
        self.ep = units * ap

    def __repr__(self):
        print(f'Units = {self.units}, hp = {self.hp}, ap = {self.ap}, init = {self.init}, attack = {self.att}, weak = {self.weak}, immunes = {self.imm}')
        return ''

with open('input.txt') as f:
    lines = f.read().splitlines()

immunes = []
infections = []

boost = 82  # Determined iterative; mind infinite loop!

elements = ['cold', 'radiation', 'bludgeoning', 'fire', 'slashing']

imm = False
inf = False
for line in lines:
    if line == '':
        imm = False
    if imm or inf:
        units = int(line.split()[0])
        hp = line.split('with ')[1]
        hp = int(hp.split(' hit')[0])
        ap = line.split('attack that does ')[1]
        ap = int(ap.split(' ')[0])
        init = int(line.split(' ')[-1])
        att = line.split(' damage')[0]
        att = att.split(' ')[-1]
        if 'weak' in line:
            weak = line.split('weak to ')[1]
            if ';' in line:
                weak = weak.split(';')[0]
            else:
                weak = weak.split(')')[0]
            weak = tuple(weak.split(', '))
        else:
            weak = tuple()
        if 'immune' in line:
            immune = line.split('immune to ')[1]
            immune = immune.split(')')[0]
            immune = tuple(immune.split(', '))
        else:
            immune = tuple()
        if imm:
            immunes.append(Group(units, hp, ap + boost, init, att, immune, weak))
        if inf:
            infections.append(Group(units, hp, ap, init, att, immune, weak))
    if 'Immune' in line:
        imm = True
    if 'Infection' in line:
        inf = True



# print(f'---Infections---\n')
# for infection in infections:
#     print(infection)

while len(immunes) > 0 and len(infections) > 0:
    # Sort on ep and init
    immunes = sorted(immunes, key=operator.attrgetter('ep', 'init'), reverse=True)
    infections = sorted(infections, key=operator.attrgetter('ep', 'init'), reverse=True)
    imm_enemies = infections.copy()
    inf_enemies = immunes.copy()
    attacks = {}
    for immune in immunes:
        damage = 0
        target = None
        for enemy in imm_enemies:
            if immune.att in enemy.imm:
                # No damage
                pass
            elif immune.att in enemy.weak:
                if damage < immune.ep * 2:
                    damage = immune.ep * 2
                    target = enemy
            else:
                if damage < immune.ep:
                    damage = immune.ep
                    target = enemy
        if target is not None:
            imm_enemies.remove(target)
            attacks[immune] = target
    for infection in infections:
        damage = 0
        target = None
        for enemy in inf_enemies:
            if infection.att in enemy.imm:
                # No damage
                pass
            elif infection.att in enemy.weak:
                if damage < infection.ep * 2:
                    damage = infection.ep * 2
                    target = enemy
            else:
                if damage < infection.ep:
                    damage = infection.ep
                    target = enemy
        if target is not None:
            inf_enemies.remove(target)
            attacks[infection] = target

    attack_order = list(attacks.keys())
    attack_order = sorted(attack_order, key=operator.attrgetter('init'), reverse=True)
    for attacker in attack_order:
        enemy = attacks[attacker]
        factor = 1
        if attacker.att in enemy.weak:
            factor *= 2
        damage = attacker.ep * factor
        enemy.units -= damage // enemy.hp
        if enemy.units <= 0:
            if enemy in immunes:
                immunes.remove(enemy)
            else:
                infections.remove(enemy)
        else:
            enemy.ep = enemy.units * enemy.ap

answer = 0
win = None
if len(immunes) > 0:
    for immune in immunes:
        answer += immune.units
        win = 'immunes'
else:
    for infection in infections:
        answer += infection.units
        win = 'infections'
print(f'{win} wins. The answer is {answer}')

