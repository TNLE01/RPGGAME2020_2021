import pygame, sys, itertools

pygame.init()

clock = pygame.time.Clock()

'''Stuff for text'''

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

def fontstuff(size):
    return pygame.font.SysFont(None, size)

'''Stuff to make buttons and images work'''

class Button(object):

    def __init__(self, w, x, y, z, color, text, fontsize, hovercolor, invisible = None):
        self.text = text
        self.fontsize = fontsize
        self.w = w
        self.x = x
        self.y = y
        self.z = z
        self.color = color
        self.hovercolor = hovercolor
        self.invisible = invisible
        self.rect = pygame.Rect((0,0), (y, z))
        self.rect.topleft = (w, x)

    def draw(self):
        b = pygame.Rect(self.w, self.x, self.y, self.z)
        mouse = pygame.mouse.get_pos()
        if self.invisible != None:
            draw_text(self.text, fontstuff(self.fontsize), (50, 100, 150), screen, (self.w + (self.y / 2)), (self.x + (self.z / 2)))
        else:
            if self.w + self.y > mouse[0] > self.w and self.x + self.z > mouse[1] > self.x:
                pygame.draw.rect(screen, self.hovercolor, b)
            else:
                pass
                pygame.draw.rect(screen, self.color, b)
            draw_text(self.text, fontstuff(self.fontsize), (50, 100, 150), screen, (self.w + (self.y / 2)), (self.x + (self.z / 2)))

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                return self.rect.collidepoint(event.pos)

def B(w, x, y, z, color, text, fontsize = 50, hovercolor = (255, 255, 0), image = None, invisible = None):
    Button(w, x, y, z, color, text, fontsize, hovercolor, invisible).draw()
    if image != None:
        loadimages(w, x, y, z, image)
    return Button(w, x, y, z, color, text, fontsize, hovercolor)

def B2(button, action, event, *actioncommand):
    if button.is_clicked(event):
        if actioncommand != None:
            action(*actioncommand)
        else:
            action()

def loadimages(w, x, y, z, image):
    screen.blit(pygame.transform.scale(pygame.image.load(image), (int(y) - 10, int(z) - 10)), (int(w) + 5,int(x) +5))

def closing():
    pygame.quit()
    sys.exit()

# def bv(w, x, y, z, text, color): #, action=None):
#     b = pygame.Rect(w, x, y, z)
#     mouse = pygame.mouse.get_pos()
#     if w + y > mouse[0] > w and x + z > mouse[1] > x:
#         pygame.draw.rect(screen, (255, 255, 0), b)
#         # if click[0] == 1 and action != None:
#         #     print('work')
#         #     action()
#     else:
#         pygame.draw.rect(screen, color, b)
#     draw_text(text, fontstuff(50), (50, 100, 150), screen, (w + (y / 2)), (x + (z / 2)))


#screen

'''Stuff for pygame window'''

screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption('Coliseum')
icon = pygame.image.load('GAMEICON.png')
pygame.display.set_icon(icon)
gridscreen = 'off'

'''Player stats'''

SHOPLASTOPEN = 'Heros'
TEAMLASTOPEN = 'Team'
GOLD = 0
XP = 0
currentlevel = 1

def XPBAR():
    global currentlevel
    global XP
    XPTOBAR = (currentlevel*100)/200
    B(650, 5, 200, 20, (200, 200, 200), 'Level ' + str(currentlevel), 20, (200, 200, 200))
    B(650, 5, XP/XPTOBAR, 20, (55, 200, 55), '', 20, (55, 200, 55))
    if XP >= currentlevel*100:
        XP = XP - currentlevel*100
        currentlevel = currentlevel + 1
    draw_text('Level ' + str(currentlevel), fontstuff(20), (50, 100, 150), screen, (650 + (200 / 2)), (5 + (20 / 2)))

def basicheading(title, headingcolor = (0, 211, 222), screencolor = (255, 255, 255), size = 500 / 5):
    screen.fill(screencolor)
    pygame.draw.rect(screen, headingcolor, pygame.Rect(0, 0, 1000, size))
    draw_text(title, fontstuff(100), (0, 0, 0), screen, 500, 50)
    draw_text('$: ' + str(GOLD), fontstuff(25), (0, 0, 0), screen, 900, 15)
    XPBAR()
    makegrid()

'''Main game loop'''

def menu():
    while True:

        basicheading('', size = 250)
        draw_text('Coliseum', fontstuff(300), (0, 0, 0), screen, 500, 125)

        BMAP = B(100, 500/2 + 50, 200, 50, (0, 242, 255), 'Map')
        BTEAM = B(400, 500/2 + 50, 200, 50, (0, 242, 255), 'Team')
        BSHOP = B(700, 500/2 + 50, 200, 50, (0, 242, 255), 'Shop')
        BMONSTERS = B(100, 500/2 + 150, 200, 50, (0, 242, 255), 'Monsters')
        BCREDITS = B(400, 500/2 + 150, 200, 50, (0, 242, 255), 'Credits')
        BEXIT = B(700, 500/2 + 150, 200, 50, (0, 242, 255), 'Exit')

        '''test code in a loop'''
        # img_path = os.path.join("Game Stuff - Python", "game_ax_icon.png")
        # image = pygame.image.load(img_path).convert()
        # pygame.image.load('Game Stuff - Python/game_ax_icon.png').convert()
        # loadimages(105, 305, 190, 40, 'Game Stuff - Python/game_ax_icon.png')
        # cropped_image = pygame.transform.chop(pygame.image.load(ALPIN.icon), (150, 100, 200, 200))
        # cropped_image22 = pygame.image.load(ALPIN.icon).subsurface(((2375/26), 0, (4125/13), 500))
        # loadimages(100, 100, 300, 100, ALPIN.icon)
        # screen.blit(pygame.transform.scale(pygame.image.load(SWAMP.icon), (int(300) - 10, int(100) - 10)), (int(100) + 5, int(100) + 5))
        # screen.blit(pygame.transform.scale(pygame.image.load(ALPIN.icon).subsurface(((2375/26), 0, (4125/13), 500)), (200, 100)), (500, 200))
        # screen.blit(cropped_image22, (600,100))


        makegrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                closing()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    closing()
            B2(BMAP, map, event)
            B2(BTEAM, team, event, TEAMLASTOPEN)
            B2(BSHOP, shop, event, SHOPLASTOPEN)
            B2(BMONSTERS, monsters, event)
            B2(BCREDITS, c, event)
            B2(BEXIT, closing, event)
        pygame.display.flip()
        clock.tick(30)

def map():
    running = True
    while running:
        basicheading('Map')

        BBACK = B(25, 25, 150, 50, (200, 20, 20), 'Back')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                closing()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if BBACK.is_clicked(event):
                running = False


        pygame.display.update()
        clock.tick(30)

def characteronteam(x, y, image = None):
    if image != None:
        screen.blit(pygame.transform.scale(pygame.image.load(image).subsurface(((2375 / 26), 0, (4125 / 13), 500)), (165, 260)), (x, y))

def team(slide):
    openshop = True
    while openshop:
        running = True
        button_dict = {}
        XVALUEFORBUTTON = [100, 280, 460, 640, 820]
        YVALUEFORBUTTON = [215]*5 + [310]*5 + [405]*5
        if slide == 'Team':
            while running:
                basicheading('Team')
                pygame.draw.rect(screen, (0, 211, 222), pygame.Rect(40, 100, 230, 500 / 5))

                BBACK = B(25, 25, 150, 50, (200, 20, 20), 'Back')
                B(80, 125, 150, 50, (0, 211, 222), 'Team', 55, (0, 211, 222))
                BHEROS = B(310, 125, 150, 50, (0, 242, 255), 'Heros', 30)
                BWEAPONS = B(540, 125, 150, 50, (0, 242, 255), 'Weapons', 30)
                BUPGRADES = B(770, 125, 150, 50, (0, 242, 255), 'Upgrades', 30)

                buttonslist = ['B10', 'B11', 'B12', 'B13', 'B20', 'B21', 'B22', 'B23', 'B30', 'B31', 'B32', 'B33']
                XVALUEFORBUTTONTEAM = [47.5, 365, 682.5]
                XVALUEFORBUTTONWEAPONS = [237.5, 555, 872.5]
                YVALUEFORBUTTONWEAPONS = [215, 310, 405]

                onteamimages = [None, None, None, None, None, None, None, None, None, None, None, None]
                for weapon, hero in zip(fullweaponslist, fullheroslist):
                    if weapon.onteam != None:
                        onteamimages.pop(weapon.teamcode)
                        onteamimages.insert(weapon.teamcode, weapon.icon)
                    if hero.onteam != None:
                        onteamimages.pop(hero.teamcode)
                        onteamimages.insert(hero.teamcode, hero.icon)

                buttonmark = 0
                for teamslot, Xweaponslot in zip(XVALUEFORBUTTONTEAM, XVALUEFORBUTTONWEAPONS):
                    button_dict[buttonslist[buttonmark]] = B(teamslot, 215, 175, 270, (0, 211, 222), '')
                    characteronteam(teamslot + 5, 220, onteamimages[buttonmark])
                    buttonmark += 1
                    for Yweaponslot in YVALUEFORBUTTONWEAPONS:
                        button_dict[buttonslist[buttonmark]] = B(Xweaponslot, Yweaponslot,80, 80, (0, 211, 222), '', image = onteamimages[buttonmark])
                        buttonmark += 1

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        closing()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            openshop = False
                            running = False
                    if BBACK.is_clicked(event):
                        openshop = False
                        running = False
                    if BHEROS.is_clicked(event):
                        slide = 'Heros'
                        running = False
                    if BWEAPONS.is_clicked(event):
                        slide = 'Weapons'
                        running = False
                    if BUPGRADES.is_clicked(event):
                        slide = 'Upgrades'
                        running = False
                    for button, index in zip(button_dict, range(0, 12)):
                        if button_dict[button].is_clicked(event):
                            print(button, index)
                pygame.display.update()
                clock.tick(30)
        if slide == 'Heros':
            while running:
                basicheading('Team')
                pygame.draw.rect(screen, (0, 211, 222), pygame.Rect(270, 100, 230, 500 / 5))

                BBACK = B(25, 25, 150, 50, (200, 20, 20), 'Back')
                BTEAM = B(80, 125, 150, 50, (0, 242, 255), 'Team', 30)
                B(310, 125, 150, 50, (0, 211, 222), 'Heros', 55, (0, 211, 222))
                BWEAPONS = B(540, 125, 150, 50, (0, 242, 255), 'Weapons', 30)
                BUPGRADES = B(770, 125, 150, 50, (0, 242, 255), 'Upgrades', 30)

                buttonslist = ['BPLAYER', 'BALPIN', 'BGAR', 'BMARKSON', 'BSWAMP', 'BSISTER', 'BTORPEDO', 'BREAPER', 'BMINER', 'BRAZOR', 'BPHANTASM', 'BSTALKER', 'BVIVI', 'BCLYPEUS', 'BEXECUTIONER']
                for button, hero, x, y in zip(buttonslist, fullheroslist, itertools.cycle(XVALUEFORBUTTON), YVALUEFORBUTTON):
                    button_dict[button] = B(x, y, 80, 80, (0, 211, 222), requirements(hero), 25, image = hero.inventory('self'))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        closing()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            openshop = False
                            running = False
                    if BBACK.is_clicked(event):
                        openshop = False
                        running = False
                    if BTEAM.is_clicked(event):
                        slide = 'Team'
                        running = False
                    if BWEAPONS.is_clicked(event):
                        slide = 'Weapons'
                        running = False
                    if BUPGRADES.is_clicked(event):
                        slide = 'Upgrades'
                        running = False
                    for button, hero in zip(button_dict, fullheroslist):
                        B2(button_dict[button], selectionbox, event, hero, 'hero', 'team', requirements(hero))

                pygame.display.update()
                clock.tick(30)
        if slide == 'Weapons':
            while running:
                basicheading('Team')
                pygame.draw.rect(screen, (0, 211, 222), pygame.Rect(500, 100, 230, 500 / 5))

                BBACK = B(25, 25, 150, 50, (200, 20, 20), 'Back')
                BTEAM = B(80, 125, 150, 50, (0, 242, 255), 'Team', 30)
                BHEROS = B(310, 125, 150, 50, (0, 242, 255), 'Heros', 30)
                B(540, 125, 150, 50, (0, 211, 222), 'Weapons', 55, (0, 211, 222))
                BUPGRADES = B(770, 125, 150, 50, (0, 242, 255), 'Upgrades', 30)

                buttonslist = ['BSWORD', 'BBOW', 'BDUALBLADE', 'BCHAINKUNAI', 'BSPEAR', 'BAX', 'BMACE', 'BHAMMER', 'BNUNCHUCKS', 'BPICKAXE', 'BMAGIC', 'BCLUB', 'BBLOWGUN', 'BSCYTHE', 'BHEAL']
                for button, weapon, x, y in zip(buttonslist, fullweaponslist, itertools.cycle(XVALUEFORBUTTON), YVALUEFORBUTTON):
                    button_dict[button] = B(x, y, 80, 80, (0, 211, 222), requirements(weapon), 25, image = weapon.inventory('self'))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        closing()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            openshop = False
                            running = False
                    if BBACK.is_clicked(event):
                        openshop = False
                        running = False
                    if BTEAM.is_clicked(event):
                        slide = 'Team'
                        running = False
                    if BHEROS.is_clicked(event):
                        slide = 'Heros'
                        running = False
                    if BUPGRADES.is_clicked(event):
                        slide = 'Upgrades'
                        running = False
                    for button, weapon in zip(button_dict, fullweaponslist):
                        B2(button_dict[button], selectionbox, event, weapon, 'weapon', 'team', requirements(weapon))
                pygame.display.update()
                clock.tick(30)
        if slide == 'Upgrades':
            while running:
                basicheading('Team')
                pygame.draw.rect(screen, (0, 211, 222), pygame.Rect(730, 100, 230, 500 / 5))

                BBACK = B(25, 25, 150, 50, (200, 20, 20), 'Back')
                BTEAM = B(80, 125, 150, 50, (0, 242, 255), 'Team', 30)
                BHEROS = B(310, 125, 150, 50, (0, 242, 255), 'Heros', 30)
                BWEAPONS = B(540, 125, 150, 50, (0, 242, 255), 'Weapons', 30)
                B(770, 125, 150, 50, (0, 211, 222), 'Upgrades', 55, (0, 211, 222))

                B(25, 265, 170, 170, (0, 242, 255), '', image = 'GAMEUPGRADES/game_upgrades_attack.png')
                B(220, 265, 170, 170, (0, 242, 255), '', image = 'GAMEUPGRADES/game_upgrades_defense.png')
                B(415, 265, 170, 170, (0, 242, 255), '', image = 'GAMEUPGRADES/game_upgrades_health.png')
                B(610, 265, 170, 170, (0, 242, 255), '', image = 'GAMEUPGRADES/game_upgrades_crit_rate.png')
                B(805, 265, 170, 170, (0, 242, 255), '', image = 'GAMEUPGRADES/game_upgrades_crit_damage.png')

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        closing()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            openshop = False
                            running = False
                    if BBACK.is_clicked(event):
                        openshop = False
                        running = False
                    if BTEAM.is_clicked(event):
                        slide = 'Team'
                        running = False
                    if BHEROS.is_clicked(event):
                        slide = 'Heros'
                        running = False
                    if BWEAPONS.is_clicked(event):
                        slide = 'Weapons'
                        running = False
                pygame.display.update()
                clock.tick(30)

    global TEAMLASTOPEN
    TEAMLASTOPEN = slide

def shop(slide):
    openshop = True
    while openshop:
        running = True
        button_dict = {}
        XVALUEFORBUTTON = [325/6, (325/6)*2 + 135, (325/6)*3 + (135)*2, (325/6)*4 + (135)*3, (325/6)*5 + (135)*4]
        YVALUEFORBUTTON = [210]*5 + [220 + 135]*5
        if slide == 'Heros':
            while running:
                basicheading('Shop')
                pygame.draw.rect(screen, (0, 211, 222), pygame.Rect(50, 100, 300, 500 / 5))

                BBACK = B(25, 25, 150, 50, (200, 20, 20), 'Back')
                B(100, 125, 200, 50, (0, 211, 222), 'Heros', 75,(0, 211, 222))
                BWEAPONS = B(400, 125, 200, 50, (0, 242, 255), 'Weapons')
                BUPGRADES = B(700, 125, 200, 50, (0, 242, 255), 'Upgrades')

                buttonslist = ['BPLAYER', 'BALPIN', 'BGAR', 'BMARKSON', 'BSISTER', 'BTORPEDO', 'BMINER', 'BRAZOR', 'BVIVI', 'BCLYPEUS']
                heroslist = [PLAYER, ALPIN, GAR, MARKSON, SISTER, TORPEDO, MINER, RAZOR, VIVI, CLYPEUS]
                for button, hero, x, y in zip(buttonslist, heroslist, itertools.cycle(XVALUEFORBUTTON), YVALUEFORBUTTON):
                    button_dict[button] = B(x, y, 135, 135, (0, 211, 222), 'Recruited', 35, image = hero.inventory('shop'))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        closing()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            openshop = False
                            running = False
                    if BBACK.is_clicked(event):
                        openshop = False
                        running = False
                    if BWEAPONS.is_clicked(event):
                        slide = 'Weapons'
                        running = False
                    if BUPGRADES.is_clicked(event):
                        slide = 'Upgrades'
                        running = False
                    for button, hero in zip(button_dict, heroslist):
                        B2(button_dict[button], selectionbox, event, hero, 'hero', 'buy', 'Recruited')
                pygame.display.update()
                clock.tick(30)
        if slide == 'Weapons':
            while running:
                basicheading('Shop')
                pygame.draw.rect(screen, (0, 211, 222), pygame.Rect(350, 100, 300, 500 / 5))

                BBACK = B(25, 25, 150, 50, (200, 20, 20), 'Back')
                BHEROS = B(100, 125, 200, 50, (0, 242, 255), 'Heros')
                B(400, 125, 200, 50, (0, 211, 222), 'Weapons', 75,(0, 211, 222))
                BUPGRADES = B(700, 125, 200, 50, (0, 242, 255), 'Upgrades')

                buttonslist = ['BBOW', 'BDUALBLADE', 'BCHAINKUNAI', 'BSPEAR', 'BMACE', 'BHAMMER', 'BNUNCHUCKS', 'BPICKAXE', 'BCLUB', 'BHEAL']
                weaponslist = [BOWANDARROW, DUALBALDE, CHAINKUNAI, SPEAR, MACE, HAMMER, NUNCHUCKS, PICKAXE, CLUB, HEAL]
                for button, weapon, x, y in zip(buttonslist, weaponslist, itertools.cycle(XVALUEFORBUTTON), YVALUEFORBUTTON):
                    button_dict[button] = B(x, y, 135, 135, (0, 211, 222), 'Sold Out', 35, image = weapon.inventory('shop'))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        closing()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            openshop = False
                            running = False
                    if BBACK.is_clicked(event):
                        openshop = False
                        running = False
                    if BHEROS.is_clicked(event):
                        slide = 'Heros'
                        running = False
                    if BUPGRADES.is_clicked(event):
                        slide = 'Upgrades'
                        running = False
                    for button, weapon in zip(button_dict, weaponslist):
                        B2(button_dict[button], selectionbox, event, weapon, 'weapon', 'buy', 'Sold Out')
                pygame.display.update()
                clock.tick(30)
        if slide == 'Upgrades':
            while running:
                basicheading('Shop')
                pygame.draw.rect(screen, (0, 211, 222), pygame.Rect(650, 100, 300, 500 / 5))

                BBACK = B(25, 25, 150, 50, (200, 20, 20), 'Back')
                BHEROS = B(100, 125, 200, 50, (0, 242, 255), 'Heros')
                BWEAPONS = B(400, 125, 200, 50, (0, 242, 255), 'Weapons')
                B(700, 125, 200, 50, (0, 211, 222), 'Upgrades', 75,(0, 211, 222))

                B(25, 265, 170, 170, (0, 242, 255), '', image = 'GAMEUPGRADES/game_upgrades_attack.png')
                B(220, 265, 170, 170, (0, 242, 255), '', image = 'GAMEUPGRADES/game_upgrades_defense.png')
                B(415, 265, 170, 170, (0, 242, 255), '', image = 'GAMEUPGRADES/game_upgrades_health.png')
                B(610, 265, 170, 170, (0, 242, 255), '', image = 'GAMEUPGRADES/game_upgrades_crit_rate.png')
                B(805, 265, 170, 170, (0, 242, 255), '', image = 'GAMEUPGRADES/game_upgrades_crit_damage.png')

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        closing()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            openshop = False
                            running = False
                    if BBACK.is_clicked(event):
                        openshop = False
                        running = False
                    if BHEROS.is_clicked(event):
                        slide = 'Heros'
                        running = False
                    if BWEAPONS.is_clicked(event):
                        slide = 'Weapons'
                        running = False
                pygame.display.update()
                clock.tick(30)
    global SHOPLASTOPEN
    SHOPLASTOPEN = slide

def selectionbox(item, type, use, message):
    print(item.bought)
    print(use)
    global GOLD
    running = True
    while running:
        key = ''
        DATALIST = [item.cost, item.type, item.damage, item.defense, item.health, item.critrate, item.critdamage, item.speed]

        if type == 'hero':
            statslist = ['Cost = ', 'Rarity = ', 'Damage Bonus = ', 'Base Defense = ', 'Base Health = ', 'Crit Rate Bonus = ', 'Base Crit Damage = ', 'Speed = ']
        else:
            statslist = ['Cost = ', 'Type = ', 'Base Damage = ', 'Defense Bonus = ', 'Health Bonus = ', 'Base Crit Rate = ', 'Crit Damage Bonus = ', 'Weight = ']

        if use == 'buy':
            question = ['Do you wish to buy: ', '?']
            if item.bought == None:
                key = 'shop'
        else:
            question = ['Add ', ' to your team?']
            statslist.remove('Cost = ')
            DATALIST.remove(item.cost)
            if item.bought != None:
                key = 'team'

        if key == 'shop' or key == 'team':

            B(275, 25, 450, 450, (0, 211, 222), '', 75, (0, 211, 222))
            B(275, 25, 450, 50, (0, 211, 222), question[0] + str(item.name) + question[1], 30, (0, 211, 222))
            B(300, 100, 250, 250, (0, 0, 0), '', 0, (0, 0, 0), image = item.icon)

            YVALUEFORSTATS = 0
            for stat, statdata in zip(statslist, DATALIST):
                B(575, 100 + (YVALUEFORSTATS*(250/8)), 125, 250 / 8, (0, 0, 0), stat + str(statdata), 20, invisible='on')
                YVALUEFORSTATS += 1

            BCANCEL = B(275 + 50/3, 400, 200, 50, (200, 20, 20), 'Cancel')
            BACCEPT = B(475 + 100/3, 400, 200, 50, (20, 200, 20), 'Accept')

        else:
            B(275, 25, 450, 450, (0, 242, 255), message, 75, (0, 242, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                closing()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if B(0, 0, 1000, 25, (0, 242, 255), '', invisible = 'on').is_clicked(event)\
                or B(0, 475, 1000, 25, (0, 242, 255), '', invisible = 'on').is_clicked(event)\
                or B(0, 25, 275, 450, (0, 242, 255), '', invisible = 'on').is_clicked(event)\
                or B(725, 25, 275, 450, (0, 242, 255), '', invisible = 'on').is_clicked(event):
                running = False
            if key == 'shop' or key == 'team':
                if BCANCEL.is_clicked(event):
                    running = False
                if BACCEPT.is_clicked(event):
                    if use == 'buy':
                        if GOLD >= item.cost:
                            GOLD = GOLD - item.cost
                            item.bought = 'yes'
                            running = False
                        else:
                            print('not enough gold')
                    else:
                        loadoutbox(item, type)
                        running = False
        pygame.display.update()
        clock.tick(30)

def loadoutbox(item, type):
    running = True
    while running:

        button_dict = {}
        if type == 'hero':
            actioncolorhero = (255, 255, 0)
            actioncolorweapon = (0, 242, 255)
        else:
            actioncolorhero = (0, 242, 255)
            actioncolorweapon = (255, 255, 0)
        B(25, 25, 950, 450, (0, 211, 222), '', hovercolor = (0, 211, 222))
        B(25, 25, 950, 25 + (325 - 850/3), (0, 211, 222), 'Pick the slot', hovercolor = (0, 211, 222))
        BCANCEL = B(400, 400, 200, 50, (200, 20, 20), 'Cancel')

        '''Location markers ↓↓↓, B12 = "Button" team "1" weapons slot "2"'''

        # B(50, 50 + (325 - 850/3), 850/3, 850/3, (0, 0, 0), '')
        # B(75 + (850/3), 50 + (325 - 850/3), 850/3, 850/3, (0, 0, 0), '')
        # B(100 + (850/3) * 2, 50 + (325 - 850/3), 850/3, 850/3, (0, 0, 0), '')

        buttonslist = ['B10', 'B11', 'B12', 'B13', 'B20', 'B21', 'B22', 'B23', 'B30', 'B31', 'B32', 'B33']
        XVALUEFORBUTTONTEAM = [50, 75 + (850/3), 100 + (850/3)*2]
        XVALUEFORBUTTONWEAPONS = [0, 850/3/3 + 3.75, 2*(850/3/3) + 7.5]

        onteamimages = [None, None, None, None, None, None, None, None, None, None, None, None]
        for weapon, hero in zip(fullweaponslist, fullheroslist):
            if weapon.onteam != None:
                onteamimages.pop(weapon.teamcode)
                onteamimages.insert(weapon.teamcode, weapon.icon)
            if hero.onteam != None:
                onteamimages.pop(hero.teamcode)
                onteamimages.insert(hero.teamcode, hero.icon)

        buttonmark = 0
        for teamslot in XVALUEFORBUTTONTEAM:
            button_dict[buttonslist[buttonmark]] = B(teamslot, 50 + (325 - 850/3), 2*(850/3/3) - 3.75, 2*(850/3/3) - 3.75, (0, 242, 255), 'Hero', hovercolor = actioncolorhero, image = onteamimages[buttonmark])
            buttonmark += 1
            for weaponslot in XVALUEFORBUTTONWEAPONS:
                button_dict[buttonslist[buttonmark]] = B(teamslot + weaponslot, 50 + (325 - 850/3) + 850/3 - 850/3/3 + 7.5, 850/3/3 - 7.5, 850/3/3 - 7.5, (0, 242, 255), 'Weapon', 20, actioncolorweapon, image = onteamimages[buttonmark])
                buttonmark += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                closing()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if B(0, 0, 1000, 25, (0, 242, 255), '', invisible = 'on').is_clicked(event)\
                or B(0, 475, 1000, 25, (0, 242, 255), '', invisible = 'on').is_clicked(event)\
                or B(0, 25, 25, 450, (0, 242, 255), '', invisible = 'on').is_clicked(event)\
                or B(975, 25, 25, 450, (0, 242, 255), '', invisible = 'on').is_clicked(event)\
                or BCANCEL.is_clicked(event):
                    running = False

            for button, index in zip(button_dict, range(0, 12)):
                if button_dict[button].is_clicked(event):
                    item.putinloadout(button, index)

        pygame.display.update()
        clock.tick(30)

def monsters():
    running = True
    while running:
        basicheading('Monsters')

        BBACK = B(25, 25, 150, 50, (200, 20, 20), 'Back')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                closing()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if BBACK.is_clicked(event):
                running = False
        pygame.display.update()
        clock.tick(30)

'''Extra stuff for testing the game'''

def c():
    running = True
    while running:
        basicheading('Credits')

        BBACK = B(25, 25, 150, 50, (200, 20, 20), 'Back')
        BTESTSCREEN = B(400, 500/2 + 150, 200, 50, (0, 242, 255), 'Testscreen')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                closing()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if BBACK.is_clicked(event):
                running = False
            B2(BTESTSCREEN, testscreen, event)
        pygame.display.update()
        clock.tick(30)

def testscreen():
    running = True
    while running:
        basicheading('Testscreen')

        BBACK = B(25, 25, 150, 50, (200, 20, 20), 'Back')
        BGIVEGOLD = B(100, 500 / 2 + 50, 200, 50, (0, 242, 255), 'Add Gold')
        BGIVEXP = B(400, 500 / 2 + 50, 200, 50, (0, 242, 255), 'Add XP')
        BTAKEGOLD = B(100, 500 / 2 + 150, 200, 50, (0, 242, 255), 'Minus Gold')
        BTAKEXP = B(400, 500 / 2 + 150, 200, 50, (0, 242, 255), 'Minus XP')
        BTEST = B(700, 500 / 2 + 50, 200, 50, (0, 242, 255), 'TEST BUTTON')
        BGRID = B(700, 500 / 2 + 150, 200, 50, (0, 242, 255), 'Grid')

        global gridscreen
        global GOLD
        global XP

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                closing()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if BBACK.is_clicked(event):
                running = False
            if BGIVEGOLD.is_clicked(event):
                GOLD = GOLD + 100
                print('Gold added, now at ' + str(GOLD))
            if BGIVEXP.is_clicked(event):
                XP = XP + 500
                print('XP added, now at ' + str(XP))
            if BTAKEGOLD.is_clicked(event):
                GOLD = GOLD - 100
                print('Gold subtracted, now at ' + str(GOLD))
            if BTAKEXP.is_clicked(event):
                XP = XP - 100
                print('XP subtracted, now at ' + str(XP))
            B2(BTEST, selectionbox, event, BOWANDARROW, 'test', 'testing again', 'testing once again')
            if BGRID.is_clicked(event):
                if gridscreen == 'off':
                    gridscreen = 'on'
                else:
                    gridscreen = 'off'
                makegrid()
        pygame.display.update()
        clock.tick(30)

def makegrid():
    if gridscreen == 'on':
        XVALUEFORLINE = 0
        YVALUEFORLINE = 0
        for x in range(21):
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(XVALUEFORLINE, 0, 1, 500))
            XVALUEFORLINE += 50
        for y in range(11):
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, YVALUEFORLINE, 1000, 1))
            YVALUEFORLINE += 50
    else:
        pass

'''Weapons for player, place holder stats'''

class Weapon():
    def __init__(self, name, type, cost, basedamage, defensebonus, healthbonus, basecritrate, critdamagebonus, speedreduction, icon, bought = None, onteam = None, requiredlevel = 0):
        self.name = name
        self.type = type
        self.cost = cost
        self.damage = basedamage
        self.defense = defensebonus
        self.health = healthbonus
        self.critrate = basecritrate
        self.critdamage = critdamagebonus
        self.speed = speedreduction
        self.icon = icon
        self.bought = bought
        self.onteam = onteam
        self.requiredlevel = requiredlevel
        self.teamcode = None

    def inventory(self, location):
        if self.requiredlevel != 0:
            if self.requiredlevel <= currentlevel:
                self.bought = 'yes'
        if location == 'shop':
            if self.bought != None:
                return None
            else:
                return self.icon
        else:
            if self.bought != None:
                return self.icon
            else:
                return None

    def putinloadout(self, place, placeindex):
        if place[-1] == '0':
            print('zero')
        else:
            for weapon in fullweaponslist:
                if weapon.onteam == place:
                    weapon.onteam = None
                    weapon.teamcode = None
            self.onteam = place
            self.teamcode = placeindex
            print(self.onteam, placeindex)

SWORD = Weapon('Sword', 'Damage', 50, 250, 150, 100, 50, 25, 15, 'GAMEWEAPONS/game_sword_icon.png', requiredlevel = 1)
BOWANDARROW = Weapon('Bow and Arrows', 'Damage', 0, 250, 150, 100, 50, 25, 15, 'GAMEWEAPONS/game_bow_icon.png')
DUALBALDE = Weapon('Dual Blades', 'Damage', 0, 250, 150, 100, 50, 25, 15, 'GAMEWEAPONS/game_dualblade_icon.png')
CHAINKUNAI = Weapon('Chained Kunai', 'Damage', 0, 250, 150, 100, 50, 25, 15, 'GAMEWEAPONS/game_chainkunai_icon.png')
SPEAR = Weapon('Spear', 'Damage', 0, 250, 150, 100, 50, 25, 15, 'GAMEWEAPONS/game_spear_icon.png')
AX = Weapon('Ax', 'Damage', 50, 250, 150, 100, 50, 25, 15, 'GAMEWEAPONS/game_ax_icon.png', requiredlevel = 9)
MACE = Weapon('Mace', 'Breaker', 50, 250, 150, 100, 50, 25, 15, 'GAMEWEAPONS/game_mace_icon.png')
HAMMER = Weapon('Hammer', 'Breaker', 50, 250, 150, 100, 50, 25, 15, 'GAMEWEAPONS/game_hammer_icon.png')
NUNCHUCKS = Weapon('Nunchucks', 'Breaker', 50, 250, 150, 100, 50, 25, 15, 'GAMEWEAPONS/game_nunchucks_icon.png')
PICKAXE = Weapon('Pickaxe', 'Breaker', 50, 250, 150, 100, 50, 25, 15, 'GAMEWEAPONS/game_pickaxe_icon.png')
MAGIC = Weapon('Magic', 'Breaker', 50, 250, 150, 100, 50, 25, 15, 'GAMEWEAPONS/game_magic_icon.png', requiredlevel = 7)
CLUB = Weapon('Club', 'Stack', 50, 250, 150, 100, 50, 25, 15, 'GAMEWEAPONS/game_club_icon.png')
BLOWGUN = Weapon('Blowgun', 'Stack', 50, 250, 150, 100, 50, 25, 15, 'GAMEWEAPONS/game_blowgun_icon.png', requiredlevel = 3)
SCYTHE = Weapon('Scythe', 'Stack', 50, 250, 150, 100, 50, 25, 15, 'GAMEWEAPONS/game_scythe_icon.png', requiredlevel = 5)
HEAL = Weapon('Heal', 'Heal', 50, 250, 150, 100, 50, 25, 15, 'GAMEWEAPONS/game_heal_icon.png')

'''Player and enemies, place holder stats'''

class Character():
    def __init__(self, name, rarity, cost, basedamage, basedefense, basehealth, critratebonus, basecritdamage, speed, icon, profile, bought = None, onteam = None, requiredlevel = 0):
        self.name = name
        self.type = rarity
        self.cost = cost
        self.damage = basedamage
        self.defense = basedefense
        self.health = basehealth
        self.critrate = critratebonus
        self.critdamage = basecritdamage
        self.speed = speed
        self.icon = icon
        self.profile = profile
        self.bought = bought
        self.onteam = onteam
        self.requiredlevel = requiredlevel
        self.teamcode = None

    def inventory(self, location):
        if self.requiredlevel != 0:
            if self.requiredlevel <= currentlevel:
                self.bought = 'yes'
        if location == 'shop':
            if self.bought != None:
                return None
            else:
                return self.icon
        else:
            if self.bought != None:
                return self.icon
            else:
                return None

    def putinloadout(self, place, placeindex):
        if place[-1] != '0':
            print('zero')
        else:
            for hero in fullheroslist:
                if hero.onteam == place:
                    hero.onteam = None
                    hero.teamcode = None
            self.onteam = place
            self.teamcode = placeindex
            print(self.onteam, placeindex)

PLAYER = Character('Player', 'Common', 0, 250, 150, 100, 50, 25, 15, 'GAMEHEROICONS/game_player_icon.png', None)
ALPIN = Character('Alpin', 'Common', 0, 250, 150, 100, 50, 25, 15, 'GAMEHEROICONS/game_alpin_icon.png', None)
GAR = Character('Gar', 'Common', 0, 250, 150, 100, 50, 25, 15, 'GAMEHEROICONS/game_gar_icon.png', None)
MARKSON = Character('Markson', 'Common', 0, 250, 150, 100, 50, 25, 15, 'GAMEHEROICONS/game_markson_icon.png', None)
SWAMP = Character('Swamp', 'Rare', 50, 250, 150, 100, 50, 25, 15, 'GAMEHEROICONS/game_swamp_icon.png', None, requiredlevel = 2)
SISTER = Character('Sister', 'Rare', 50, 250, 150, 100, 50, 25, 15, 'GAMEHEROICONS/game_sister_icon.png', None)
TORPEDO = Character('Torpedo', 'Rare', 50, 250, 150, 100, 50, 25, 15, 'GAMEHEROICONS/game_torpedo_icon.png', None)
REAPER = Character('Reaper', 'Rare', 50, 250, 150, 100, 50, 25, 15, 'GAMEHEROICONS/game_reaper_icon.png', None, requiredlevel = 4)
MINER = Character('Miner', 'Rare', 50, 250, 150, 100, 50, 25, 15, 'GAMEHEROICONS/game_miner_icon.png', None)
RAZOR = Character('Razor', 'Rare', 50, 250, 150, 100, 50, 25, 15, 'GAMEHEROICONS/game_razor_icon.png', None)
PHANTASM = Character('Phantasm', 'Rare', 50, 250, 150, 100, 50, 25, 15, 'GAMEHEROICONS/game_phantasm_icon.png',None, requiredlevel = 6)
STALKER = Character('Stalker', 'Rare', 50, 250, 150, 100, 50, 25, 15, 'GAMEHEROICONS/game_stalker_icon.png', None, requiredlevel = 8)
VIVI = Character('Vivi', 'Epic', 50, 250, 150, 100, 50, 25, 15, 'GAMEHEROICONS/game_vivi_icon.png', None)
CLYPEUS = Character('Clypeus', 'Epic', 50, 250, 150, 100, 50, 25, 15, 'GAMEHEROICONS/game_clypeus_icon.png', None)
EXECUTIONER = Character('Executioner', 'Epic', 50, 250, 150, 100, 50, 25, 15, 'GAMEHEROICONS/game_executioner_icon.png', None, requiredlevel = 10)

def requirements(item):
    if item.requiredlevel == 0:
        return 'In Shop'
    else:
        return 'Level ' + str(item.requiredlevel)

fullweaponslist = [SWORD, BOWANDARROW, DUALBALDE, CHAINKUNAI, SPEAR, AX, MACE, HAMMER, NUNCHUCKS, PICKAXE, MAGIC, CLUB, BLOWGUN, SCYTHE, HEAL]
fullheroslist = [PLAYER, ALPIN, GAR, MARKSON, SWAMP, SISTER, TORPEDO, REAPER, MINER, RAZOR, PHANTASM, STALKER, VIVI, CLYPEUS, EXECUTIONER]

'''code testing'''

# x = ['buffalo', 'hellp', 'me', 'please']
# y = [1, 2, 3, 4]
# for zzz, num in zip(x, y):
#     exec("%s = %d" % (zzz, num))
#
# print(buffalo)
# print(hellp)
# print(me)
# print(please)

# my_dict = {}
# x = ['hello', 'world', 'hope', 'your', 'well']
# y = [1, 2, 3]
# for var, num in zip(x, itertools.cycle(y)):
#     my_dict[var] = num
#
# print(list(my_dict.keys())[2])
#
# print(my_dict['hello'])
#
# print(my_dict)

# def m(x, y):
#     print(x+y)
#
# def bbb(func, *args):
#     func(*args)
#
# bbb(m, 3, 4)

# herotest = ['B30', None, 'B20']
# onteamzzz = []
# for h in herotest:
#     if h != None:
#         onteamzzz.append(h)
#     else:
#         onteamzzz.append(None)
#
# print(onteamzzz)
#
# for num in range(0, 5):
#     print(num)

menu()

