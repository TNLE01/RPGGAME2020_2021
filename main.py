import pygame, sys, itertools, random

pygame.init()

clock = pygame.time.Clock()

'''Stuff for pygame window'''

screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption('Coliseum')
icon = pygame.image.load('GAMEICON.png')
pygame.display.set_icon(icon)
gridscreen = 'off'

'''Stuff for text / Images'''

class BasicWorkings:

    def closing(self):
        pygame.quit()
        sys.exit()

    def loadimages(self, w, x, y, z, image):
        screen.blit(pygame.transform.scale(pygame.image.load(image), (int(y) - 10, int(z) - 10)), (int(w) + 5, int(x) + 5))

    def draw_text(self, text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.center = (x, y)
        surface.blit(textobj, textrect)

    def fontstuff(self, size):
        return pygame.font.SysFont(None, size)

    def makegrid(self):
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

    def basicheading(self, title, headingcolor = (0, 211, 222), screencolor = (255, 255, 255), size = 500/5):
        screen.fill(screencolor)
        pygame.draw.rect(screen, headingcolor, pygame.Rect(0, 0, 1000, size))
        BasicWorkings().draw_text(title, BasicWorkings().fontstuff(100), (0, 0, 0), screen, 500, 50)
        BasicWorkings().draw_text('$: ' + str(FILE_1.Gold), BasicWorkings().fontstuff(25), (0, 0, 0), screen, 900, 15)
        FILE_1.XPBAR()
        BasicWorkings().makegrid()

'''Stuff to make buttons work / exiting game'''

class Button(object):

    def __init__(self, w, x, y, z, color, text, fontsize = 50, hovercolor = (255, 255, 0), image = None, invisible = None):
        self.text = text
        self.fontsize = fontsize
        self.w = w
        self.x = x
        self.y = y
        self.z = z
        self.color = color
        self.hovercolor = hovercolor
        self.image = image
        self.invisible = invisible
        self.rect = pygame.Rect((0,0), (y, z))
        self.rect.topleft = (w, x)

    def draw(self):
        b = pygame.Rect(self.w, self.x, self.y, self.z)
        mouse = pygame.mouse.get_pos()
        if self.invisible != None:
            BasicWorkings().draw_text(self.text, BasicWorkings().fontstuff(self.fontsize), (50, 100, 150), screen, (self.w + (self.y / 2)), (self.x + (self.z / 2)))
        else:
            if self.w + self.y > mouse[0] > self.w and self.x + self.z > mouse[1] > self.x:
                pygame.draw.rect(screen, self.hovercolor, b)
            else:
                pass
                pygame.draw.rect(screen, self.color, b)
            BasicWorkings().draw_text(self.text, BasicWorkings().fontstuff(self.fontsize), (50, 100, 150), screen, (self.w + (self.y / 2)), (self.x + (self.z / 2)))
        if self.image != None:
            BasicWorkings().loadimages(self.w, self.x, self.y, self.z, self.image)
        return Button(self.w, self.x, self.y, self.z, self.color, self.text, self.fontsize, self.hovercolor)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                return self.rect.collidepoint(event.pos)

    def clicked_action(self, event, action, *actioncommand):
        if self.is_clicked(event):
            if actioncommand != None:
                action(*actioncommand)
            else:
                action()

'''Player stats'''

class Profile:

    def __init__(self, ShopLastOpen, TeamLastOpen, Gold, XP, CurrentLevel):
        self.ShopLastOpen = ShopLastOpen
        self.TeamLastOpen = TeamLastOpen
        self.Gold = Gold
        self.XP = XP
        self.CurrentLevel = CurrentLevel
        self.ontheteam = None
        self.currentlevel = None

    def change(self, what, value):
        if what == 'XP':
            self.XP += value
        else:
            self.Gold += value

    def XPBAR(self):
        XPTOBAR = (self.CurrentLevel * 100) / 200
        Button(650, 5, 200, 20, (200, 200, 200), 'Level ' + str(self.CurrentLevel), 20, (200, 200, 200)).draw()
        Button(650, 5, self.XP / XPTOBAR, 20, (55, 200, 55), '', 20, (55, 200, 55)).draw()
        if self.XP >= self.CurrentLevel * 100:
            self.XP = self.XP - self.CurrentLevel * 100
            self.CurrentLevel = self.CurrentLevel + 1
        BasicWorkings().draw_text('Level ' + str(self.CurrentLevel), BasicWorkings().fontstuff(20), (50, 100, 150), screen, (650 + (200 / 2)), (5 + (20 / 2)))

FILE_1 = Profile('Heros', 'Team', 0, 0, 1)
#FILE_2 = Profile()
#FILE_3 = Profile()

'''Main game loop'''

class MainRun:

    def __init__(self):
        self.dw = 1000
        self.dh = 500
        self.main()

    def main(self):

        while True:
            BasicWorkings().basicheading('', size=250)
            BasicWorkings().draw_text('Coliseum', BasicWorkings().fontstuff(300), (0, 0, 0), screen, 500, 125)

            BMAP = Button(100, 500 / 2 + 50, 200, 50, (0, 242, 255), 'Map').draw()
            BTEAM = Button(400, 500 / 2 + 50, 200, 50, (0, 242, 255), 'Team').draw()
            BSHOP = Button(700, 500 / 2 + 50, 200, 50, (0, 242, 255), 'Shop').draw()
            BMONSTERS = Button(100, 500 / 2 + 150, 200, 50, (0, 242, 255), 'Monsters').draw()
            BCREDITS = Button(400, 500 / 2 + 150, 200, 50, (0, 242, 255), 'Credits').draw()
            BEXIT = Button(700, 500 / 2 + 150, 200, 50, (0, 242, 255), 'Exit').draw()

            '''test code in a loop'''
            #img_path = os.path.join("Game Stuff - Python", "game_ax_icon.png")
            #image = pygame.image.load(img_path).convert()
            #pygame.image.load('Game Stuff - Python/game_ax_icon.png').convert()
            #BasicWorkings().loadimages(105, 305, 190, 40, 'Game Stuff - Python/game_ax_icon.png')
            #cropped_image = pygame.transform.chop(pygame.image.load(ALPIN.icon), (150, 100, 200, 200))
            #cropped_image22 = pygame.image.load(ALPIN.icon).subsurface(((2375/26), 0, (4125/13), 500))
            #BasicWorkings().loadimages(100, 100, 300, 100, ALPIN.icon)
            #screen.blit(pygame.transform.scale(pygame.image.load(SWAMP.icon), (int(300) - 10, int(100) - 10)), (int(100) + 5, int(100) + 5))
            #screen.blit(pygame.transform.scale(pygame.image.load(ALPIN.icon).subsurface(((2375/26), 0, (4125/13), 500)), (200, 100)), (500, 200))
            #screen.blit(cropped_image22, (600,100))

            #Event Tasking
            #Add all your event tasking things here
            BasicWorkings().makegrid()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    BasicWorkings().closing()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        BasicWorkings().closing()

                BMAP.clicked_action(event, Combat().combatwindow) #self.map)
                BTEAM.clicked_action(event, self.team, FILE_1.TeamLastOpen)
                BSHOP.clicked_action(event, self.shop, FILE_1.ShopLastOpen)
                BMONSTERS.clicked_action(event, self.monsters)
                BCREDITS.clicked_action(event, self.c)
                BEXIT.clicked_action(event, BasicWorkings().closing)

            pygame.display.flip()
            clock.tick(30)
            #Add things like player updates here
            #Also things like score updates or drawing additional items
            # Remember things on top get done first so they will update in the order yours is set at

            # Remember to update your clock and display at the end
            pygame.display.update()
            clock.tick(30)

        # If you need to reset variables here
        # This includes things like score resets

    def map(self):
        running = True
        while running:
            BasicWorkings().basicheading('Map')

            BBACK = Button(25, 25, 150, 50, (200, 20, 20), 'Back').draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    BasicWorkings().closing()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                if BBACK.is_clicked(event):
                    running = False

            pygame.display.update()
            clock.tick(30)

    def team(self, slide):
        openshop = True
        while openshop:
            running = True
            button_dict = {}
            XVALUEFORBUTTON = [100, 280, 460, 640, 820]
            YVALUEFORBUTTON = [215] * 5 + [310] * 5 + [405] * 5
            if slide == 'Team':
                while running:
                    BasicWorkings().basicheading('Team')
                    pygame.draw.rect(screen, (0, 211, 222), pygame.Rect(40, 100, 230, 500 / 5))

                    BBACK = Button(25, 25, 150, 50, (200, 20, 20), 'Back').draw()
                    Button(80, 125, 150, 50, (0, 211, 222), 'Team', 55, (0, 211, 222)).draw()
                    BHEROS = Button(310, 125, 150, 50, (0, 242, 255), 'Heros', 30).draw()
                    BWEAPONS = Button(540, 125, 150, 50, (0, 242, 255), 'Weapons', 30).draw()
                    BUPGRADES = Button(770, 125, 150, 50, (0, 242, 255), 'Upgrades', 30).draw()

                    buttonslist = ['B10', 'B11', 'B12', 'B13', 'B20', 'B21', 'B22', 'B23', 'B30', 'B31', 'B32', 'B33']
                    XVALUEFORBUTTONTEAM = [47.5, 365, 682.5]
                    XVALUEFORBUTTONWEAPONS = [237.5, 555, 872.5]
                    YVALUEFORBUTTONWEAPONS = [215, 310, 405]

                    FILE_1.ontheteam = ([PHC] + [PHW] * 3) * 3
                    for weapon, hero in zip(fullweaponslist, fullheroslist):
                        if weapon.onteam != None:
                            FILE_1.ontheteam.pop(weapon.teamcode)
                            FILE_1.ontheteam.insert(weapon.teamcode, weapon)
                        if hero.onteam != None:
                            FILE_1.ontheteam.pop(hero.teamcode)
                            FILE_1.ontheteam.insert(hero.teamcode, hero)

                    buttonmark = 0
                    for teamslot, Xweaponslot in zip(XVALUEFORBUTTONTEAM, XVALUEFORBUTTONWEAPONS):
                        button_dict[buttonslist[buttonmark]] = Button(teamslot, 215, 175, 270, (0, 211, 222), '').draw()
                        characteronteam(teamslot + 5, 220, FILE_1.ontheteam[buttonmark].icon)
                        buttonmark += 1
                        for Yweaponslot in YVALUEFORBUTTONWEAPONS:
                            button_dict[buttonslist[buttonmark]] = Button(Xweaponslot, Yweaponslot, 80, 80, (0, 211, 222), '', image = FILE_1.ontheteam[buttonmark].icon).draw()
                            buttonmark += 1

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            BasicWorkings().closing()
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
                            button_dict[button].clicked_action(event, Popup(FILE_1.ontheteam[index], 'all', 'remove', donothing = 'on').selectionbox)

                    pygame.display.update()
                    clock.tick(30)
            if slide == 'Heros':
                while running:
                    BasicWorkings().basicheading('Team')
                    pygame.draw.rect(screen, (0, 211, 222), pygame.Rect(270, 100, 230, 500 / 5))

                    BBACK = Button(25, 25, 150, 50, (200, 20, 20), 'Back').draw()
                    BTEAM = Button(80, 125, 150, 50, (0, 242, 255), 'Team', 30).draw()
                    Button(310, 125, 150, 50, (0, 211, 222), 'Heros', 55, (0, 211, 222)).draw()
                    BWEAPONS = Button(540, 125, 150, 50, (0, 242, 255), 'Weapons', 30).draw()
                    BUPGRADES = Button(770, 125, 150, 50, (0, 242, 255), 'Upgrades', 30).draw()

                    buttonslist = ['BPLAYER', 'BALPIN', 'BGAR', 'BMARKSON', 'BSWAMP', 'BSISTER', 'BTORPEDO', 'BREAPER', 'BMINER', 'BRAZOR', 'BPHANTASM', 'BSTALKER', 'BVIVI', 'BCLYPEUS', 'BEXECUTIONER']
                    for button, hero, x, y in zip(buttonslist, fullheroslist, itertools.cycle(XVALUEFORBUTTON), YVALUEFORBUTTON):
                        button_dict[button] = Button(x, y, 80, 80, (0, 211, 222), requirements(hero), 25, image = hero.inventory('self')).draw()

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            BasicWorkings().closing()
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
                            button_dict[button].clicked_action(event, Popup(hero, 'hero', 'team', requirements(hero)).selectionbox)
                    pygame.display.update()
                    clock.tick(30)
            if slide == 'Weapons':
                while running:
                    BasicWorkings().basicheading('Team')
                    pygame.draw.rect(screen, (0, 211, 222), pygame.Rect(500, 100, 230, 500 / 5))

                    BBACK = Button(25, 25, 150, 50, (200, 20, 20), 'Back').draw()
                    BTEAM = Button(80, 125, 150, 50, (0, 242, 255), 'Team', 30).draw()
                    BHEROS = Button(310, 125, 150, 50, (0, 242, 255), 'Heros', 30).draw()
                    Button(540, 125, 150, 50, (0, 211, 222), 'Weapons', 55, (0, 211, 222)).draw()
                    BUPGRADES = Button(770, 125, 150, 50, (0, 242, 255), 'Upgrades', 30).draw()

                    buttonslist = ['BSWORD', 'BBOW', 'BDUALBLADE', 'BCHAINKUNAI', 'BSPEAR', 'BAX', 'BMACE', 'BHAMMER', 'BNUNCHUCKS', 'BPICKAXE', 'BMAGIC', 'BCLUB', 'BBLOWGUN', 'BSCYTHE', 'BHEAL']
                    for button, weapon, x, y in zip(buttonslist, fullweaponslist, itertools.cycle(XVALUEFORBUTTON), YVALUEFORBUTTON):
                        button_dict[button] = Button(x, y, 80, 80, (0, 211, 222), requirements(weapon), 25, image = weapon.inventory('self')).draw()

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            BasicWorkings().closing()
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
                            button_dict[button].clicked_action(event, Popup(weapon, 'weapon', 'team', requirements(weapon)).selectionbox)
                    pygame.display.update()
                    clock.tick(30)
            if slide == 'Upgrades':
                while running:
                    BasicWorkings().basicheading('Team')
                    pygame.draw.rect(screen, (0, 211, 222), pygame.Rect(730, 100, 230, 500 / 5))

                    BBACK = Button(25, 25, 150, 50, (200, 20, 20), 'Back').draw()
                    BTEAM = Button(80, 125, 150, 50, (0, 242, 255), 'Team', 30).draw()
                    BHEROS = Button(310, 125, 150, 50, (0, 242, 255), 'Heros', 30).draw()
                    BWEAPONS = Button(540, 125, 150, 50, (0, 242, 255), 'Weapons', 30).draw()
                    Button(770, 125, 150, 50, (0, 211, 222), 'Upgrades', 55, (0, 211, 222)).draw()

                    Button(25, 265, 170, 170, (0, 242, 255), '', image = 'GAMEUPGRADES/game_upgrades_attack.png').draw()
                    Button(220, 265, 170, 170, (0, 242, 255), '', image = 'GAMEUPGRADES/game_upgrades_defense.png').draw()
                    Button(415, 265, 170, 170, (0, 242, 255), '', image = 'GAMEUPGRADES/game_upgrades_health.png').draw()
                    Button(610, 265, 170, 170, (0, 242, 255), '', image = 'GAMEUPGRADES/game_upgrades_crit_rate.png').draw()
                    Button(805, 265, 170, 170, (0, 242, 255), '', image = 'GAMEUPGRADES/game_upgrades_crit_damage.png').draw()

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            BasicWorkings().closing()
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

        FILE_1.TeamLastOpen = slide

    def shop(self, slide):
        openshop = True
        while openshop:
            running = True
            button_dict = {}
            XVALUEFORBUTTON = [325 / 6, (325 / 6) * 2 + 135, (325 / 6) * 3 + (135) * 2, (325 / 6) * 4 + (135) * 3, (325 / 6) * 5 + (135) * 4]
            YVALUEFORBUTTON = [210] * 5 + [220 + 135] * 5
            if slide == 'Heros':
                while running:
                    BasicWorkings().basicheading('Shop')
                    pygame.draw.rect(screen, (0, 211, 222), pygame.Rect(50, 100, 300, 500 / 5))

                    BBACK = Button(25, 25, 150, 50, (200, 20, 20), 'Back').draw()
                    Button(100, 125, 200, 50, (0, 211, 222), 'Heros', 75, (0, 211, 222)).draw()
                    BWEAPONS = Button(400, 125, 200, 50, (0, 242, 255), 'Weapons').draw()
                    BUPGRADES = Button(700, 125, 200, 50, (0, 242, 255), 'Upgrades').draw()

                    buttonslist = ['BPLAYER', 'BALPIN', 'BGAR', 'BMARKSON', 'BSISTER', 'BTORPEDO', 'BMINER', 'BRAZOR', 'BVIVI', 'BCLYPEUS']
                    heroslist = [PLAYER, ALPIN, GAR, MARKSON, SISTER, TORPEDO, MINER, RAZOR, VIVI, CLYPEUS]
                    for button, hero, x, y in zip(buttonslist, heroslist, itertools.cycle(XVALUEFORBUTTON), YVALUEFORBUTTON):
                        button_dict[button] = Button(x, y, 135, 135, (0, 211, 222), 'Recruited', 35, image = hero.inventory('shop')).draw()

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            BasicWorkings().closing()
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
                            button_dict[button].clicked_action(event, Popup(hero, 'hero', 'buy', 'Recruited').selectionbox)
                    pygame.display.update()
                    clock.tick(30)
            if slide == 'Weapons':
                while running:
                    BasicWorkings().basicheading('Shop')
                    pygame.draw.rect(screen, (0, 211, 222), pygame.Rect(350, 100, 300, 500 / 5))

                    BBACK = Button(25, 25, 150, 50, (200, 20, 20), 'Back').draw()
                    BHEROS = Button(100, 125, 200, 50, (0, 242, 255), 'Heros').draw()
                    Button(400, 125, 200, 50, (0, 211, 222), 'Weapons', 75, (0, 211, 222)).draw()
                    BUPGRADES = Button(700, 125, 200, 50, (0, 242, 255), 'Upgrades').draw()

                    buttonslist = ['BBOW', 'BDUALBLADE', 'BCHAINKUNAI', 'BSPEAR', 'BMACE', 'BHAMMER', 'BNUNCHUCKS', 'BPICKAXE', 'BCLUB', 'BHEAL']
                    weaponslist = [BOWANDARROW, DUALBALDE, CHAINKUNAI, SPEAR, MACE, HAMMER, NUNCHUCKS, PICKAXE, CLUB, HEAL]
                    for button, weapon, x, y in zip(buttonslist, weaponslist, itertools.cycle(XVALUEFORBUTTON), YVALUEFORBUTTON):
                        button_dict[button] = Button(x, y, 135, 135, (0, 211, 222), 'Sold Out', 35, image = weapon.inventory('shop')).draw()

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            BasicWorkings().closing()
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
                            button_dict[button].clicked_action(event, Popup(weapon, 'weapon', 'buy', 'Sold Out').selectionbox)
                    pygame.display.update()
                    clock.tick(30)
            if slide == 'Upgrades':
                while running:
                    BasicWorkings().basicheading('Shop')
                    pygame.draw.rect(screen, (0, 211, 222), pygame.Rect(650, 100, 300, 500 / 5))

                    BBACK = Button(25, 25, 150, 50, (200, 20, 20), 'Back').draw()
                    BHEROS = Button(100, 125, 200, 50, (0, 242, 255), 'Heros').draw()
                    BWEAPONS = Button(400, 125, 200, 50, (0, 242, 255), 'Weapons').draw()
                    Button(700, 125, 200, 50, (0, 211, 222), 'Upgrades', 75, (0, 211, 222)).draw()

                    Button(25, 265, 170, 170, (0, 242, 255), '', image = 'GAMEUPGRADES/game_upgrades_attack.png').draw()
                    Button(220, 265, 170, 170, (0, 242, 255), '', image = 'GAMEUPGRADES/game_upgrades_defense.png').draw()
                    Button(415, 265, 170, 170, (0, 242, 255), '', image = 'GAMEUPGRADES/game_upgrades_health.png').draw()
                    Button(610, 265, 170, 170, (0, 242, 255), '', image = 'GAMEUPGRADES/game_upgrades_crit_rate.png').draw()
                    Button(805, 265, 170, 170, (0, 242, 255), '', image = 'GAMEUPGRADES/game_upgrades_crit_damage.png').draw()

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            BasicWorkings().closing()
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

        FILE_1.ShopLastOpen = slide

    def monsters(self):
        running = True
        while running:
            BasicWorkings().basicheading('Monsters')

            BBACK = Button(25, 25, 150, 50, (200, 20, 20), 'Back').draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    BasicWorkings().closing()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                if BBACK.is_clicked(event):
                    running = False
            pygame.display.update()
            clock.tick(30)

    '''Extra stuff for testing the game'''

    def c(self):
        running = True
        while running:
            BasicWorkings().basicheading('Credits')

            BBACK = Button(25, 25, 150, 50, (200, 20, 20), 'Back').draw()
            BTESTSCREEN = Button(400, 500 / 2 + 150, 200, 50, (0, 242, 255), 'Testscreen').draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    BasicWorkings().closing()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                if BBACK.is_clicked(event):
                    running = False
                BTESTSCREEN.clicked_action(event, self.testscreen)
            pygame.display.update()
            clock.tick(30)

    def testscreen(self):
        running = True
        while running:
            BasicWorkings().basicheading('Testscreen')

            BBACK = Button(25, 25, 150, 50, (200, 20, 20), 'Back').draw()
            BGIVEGOLD = Button(100, 500 / 2 + 50, 200, 50, (0, 242, 255), 'Add Gold').draw()
            BGIVEXP = Button(400, 500 / 2 + 50, 200, 50, (0, 242, 255), 'Add XP').draw()
            BTAKEGOLD = Button(100, 500 / 2 + 150, 200, 50, (0, 242, 255), 'Minus Gold').draw()
            BTAKEXP = Button(400, 500 / 2 + 150, 200, 50, (0, 242, 255), 'Minus XP').draw()
            BTEST = Button(700, 500 / 2 + 50, 200, 50, (0, 242, 255), 'TEST BUTTON').draw()
            BGRID = Button(700, 500 / 2 + 150, 200, 50, (0, 242, 255), 'Grid').draw()

            global gridscreen

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    BasicWorkings().closing()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                if BBACK.is_clicked(event):
                    running = False
                if BGIVEGOLD.is_clicked(event):
                    FILE_1.change('gold', 100)
                    print('Gold added, now at ' + str(FILE_1.Gold))
                if BGIVEXP.is_clicked(event):
                    FILE_1.change('XP', 500)
                    print('XP added, now at ' + str(FILE_1.XP))
                if BTAKEGOLD.is_clicked(event):
                    FILE_1.change('gold', -100)
                    print('Gold subtracted, now at ' + str(FILE_1.Gold))
                if BTAKEXP.is_clicked(event):
                    FILE_1.change('XP', -100)
                    print('XP subtracted, now at ' + str(FILE_1.XP))
                BTEST.clicked_action(event, Popup(BOWANDARROW, 'test', 'testing again', 'testing once again').selectionbox)
                if BGRID.is_clicked(event):
                    if gridscreen == 'off':
                        gridscreen = 'on'
                    else:
                        gridscreen = 'off'
                    BasicWorkings().makegrid()
            pygame.display.update()
            clock.tick(30)

def characteronteam(x, y, image = None):
    if image != None:
        screen.blit(pygame.transform.scale(pygame.image.load(image).subsurface(((2375 / 26), 0, (4125 / 13), 500)), (165, 260)), (x, y))

class Popup:

    def __init__(self, item, type, use, message = None, donothing = None):
        self.item = item
        self.type = type
        self.message = message
        self.use = use
        self.donothing = donothing

    def TEXT(self, size):
        Button(275, 25, 450, 450, (0, 242, 255), self.message, size, (0, 242, 255)).draw()

    def selectionbox(self, size = 75):
        running = True
        while running:
            if self.use == 'buy':
                key = self.buying()
            if self.use == 'team':
                key = self.addtoloadout()
            if self.use == 'remove':
                key = self.removefromteam()

            if key == True:
                BCANCEL = Button(275 + 50 / 3, 400, 200, 50, (200, 20, 20), 'Cancel').draw()
                BACCEPT = Button(475 + 100 / 3, 400, 200, 50, (20, 200, 20), 'Accept').draw()

            else:
                if self.donothing != None:
                    return
                self.TEXT(size)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    BasicWorkings().closing()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                if Button(0, 0, 1000, 25, (0, 242, 255), '', invisible='on').is_clicked(event) \
                        or Button(0, 475, 1000, 25, (0, 242, 255), '', invisible='on').is_clicked(event) \
                        or Button(0, 25, 275, 450, (0, 242, 255), '', invisible='on').is_clicked(event) \
                        or Button(725, 25, 275, 450, (0, 242, 255), '', invisible='on').is_clicked(event):
                    running = False
                if key == True:
                    if BCANCEL.is_clicked(event):
                        running = False
                    if BACCEPT.is_clicked(event):
                        self.ACTION()
                        running = False

            pygame.display.update()
            clock.tick(30)

    def ACTION(self):
        if self.use == 'buy':
            self.buying(action = 'on')
        if self.use == 'team':
            self.addtoloadout(action = 'on')
        if self.use == 'remove':
            self.removefromteam(action = 'on')

    def buying(self, action = None):
        if self.item.bought == None and action == None:
            Button(275, 25, 450, 450, (0, 211, 222), '', 75, (0, 211, 222)).draw()
            Button(275, 25, 450, 50, (0, 211, 222), 'Do you wish to buy: ' + str(self.item.name) + '?', 30, (0, 211, 222)).draw()
            Button(300, 100, 250, 250, (0, 0, 0), '', 0, (0, 0, 0), image = self.item.icon).draw()
            YVALUEFORSTATS = 0
            for num in range(0, 8):
                Button(575, 100 + (YVALUEFORSTATS * (250 / 8)), 125, 250 / 8, (0, 0, 0),
                       self.item.statslist[num] + str(self.item.DATALIST[num]), 20, invisible='on').draw()
                YVALUEFORSTATS += 1
            return True
        if action != None:
            if FILE_1.Gold >= self.item.cost:
                FILE_1.change('gold', -self.item.cost)
                self.item.bought = 'yes'
            else:
                print('not enough gold')

    def addtoloadout(self, action = None):
        if self.item.bought != None and action == None:
            Button(275, 25, 450, 450, (0, 211, 222), '', 75, (0, 211, 222)).draw()
            Button(275, 25, 450, 50, (0, 211, 222), 'Add ' + str(self.item.name) + ' to your team?', 30, (0, 211, 222)).draw()
            Button(300, 100, 250, 250, (0, 0, 0), '', 0, (0, 0, 0), image = self.item.icon).draw()
            YVALUEFORSTATS = 0
            for num in range(1, 8):
                Button(575, 100 + (YVALUEFORSTATS * (250 / 8)), 125, 250 / 8, (0, 0, 0), self.item.statslist[num] + str(self.item.DATALIST[num]), 20, invisible = 'on').draw()
                YVALUEFORSTATS += 1
            return True
        if action != None:
            self.loadoutbox()

    def loadoutbox(self):
        running = True
        while running:

            button_dict = {}
            if self.type == 'hero':
                actioncolorhero = (255, 255, 0)
                actioncolorweapon = (0, 242, 255)
            else:
                actioncolorhero = (0, 242, 255)
                actioncolorweapon = (255, 255, 0)
            Button(25, 25, 950, 450, (0, 211, 222), '', hovercolor = (0, 211, 222)).draw()
            Button(25, 25, 950, 25 + (325 - 850 / 3), (0, 211, 222), 'Pick the slot', invisible = 'on').draw()
            BCANCEL = Button(400, 400, 200, 50, (200, 20, 20), 'Cancel').draw()

            '''Location markers ↓↓↓, B12 = "Button" team "1" weapons slot "2"'''

            # Button(50, 50 + (325 - 850/3), 850/3, 850/3, (0, 0, 0), '').draw()
            # Button(75 + (850/3), 50 + (325 - 850/3), 850/3, 850/3, (0, 0, 0), '').draw()
            # Button(100 + (850/3) * 2, 50 + (325 - 850/3), 850/3, 850/3, (0, 0, 0), '').draw()

            buttonslist = ['B10', 'B11', 'B12', 'B13', 'B20', 'B21', 'B22', 'B23', 'B30', 'B31', 'B32', 'B33']
            XVALUEFORBUTTONTEAM = [50, 75 + (850 / 3), 100 + (850 / 3) * 2]
            XVALUEFORBUTTONWEAPONS = [0, 850 / 3 / 3 + 3.75, 2 * (850 / 3 / 3) + 7.5]
            statslist = ['Speed = ', 'Crit Damage = ', 'Crit Rate = ', 'Health = ', 'Defense = ', 'Damage = ']

            FILE_1.ontheteam = ([PHC] + [PHW] * 3) * 3

            for weapon, hero in zip(fullweaponslist, fullheroslist):
                if weapon.onteam != None:
                    FILE_1.ontheteam.pop(weapon.teamcode)
                    FILE_1.ontheteam.insert(weapon.teamcode, weapon)
                if hero.onteam != None:
                    FILE_1.ontheteam.pop(hero.teamcode)
                    FILE_1.ontheteam.insert(hero.teamcode, hero)

            buttonmark = 0
            totalcounter = 0
            totalstat = 0
            for teamslot in XVALUEFORBUTTONTEAM:
                button_dict[buttonslist[buttonmark]] = Button(teamslot, 50 + (325 - 850 / 3), 2 * (850 / 3 / 3) - 3.75, 2 * (850 / 3 / 3) - 3.75, (0, 242, 255), 'Hero', hovercolor = actioncolorhero, image = FILE_1.ontheteam[buttonmark].icon).draw()
                buttonmark += 1
                totalcounter += 4
                for weaponslot in XVALUEFORBUTTONWEAPONS:
                    button_dict[buttonslist[buttonmark]] = Button(teamslot + weaponslot, 50 + (325 - 850 / 3) + 850 / 3 - 850 / 3 / 3 + 7.5, 850 / 3 / 3 - 7.5, 850 / 3 / 3 - 7.5, (0, 242, 255), 'Weapon', 20, actioncolorweapon, image = FILE_1.ontheteam[buttonmark].icon).draw()
                    buttonmark += 1
                    statindex = 7
                    for num, stats in zip(range(1, 7), statslist):
                        for total in range(totalcounter - 4, totalcounter):
                            totalstat += FILE_1.ontheteam[total].DATALIST[statindex]
                        Button(teamslot + 2 * (850 / 3 / 3) + 7.5, (50 + (325 - 850 / 3) + 850 / 3 - 850 / 3 / 3) - (2 * (850 / 3 / 3)) * (num / 6), 850 / 3 / 3 - 7.5, (2 * (850 / 3 / 3) - 3.75) / 6, (0, 242, 255), stats + str(totalstat), 15, invisible='on').draw()
                        statindex -= 1
                        totalstat = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    BasicWorkings().closing()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                if Button(0, 0, 1000, 25, (0, 242, 255), '', invisible='on').is_clicked(event) \
                        or Button(0, 475, 1000, 25, (0, 242, 255), '', invisible='on').is_clicked(event) \
                        or Button(0, 25, 25, 450, (0, 242, 255), '', invisible='on').is_clicked(event) \
                        or Button(975, 25, 25, 450, (0, 242, 255), '', invisible='on').is_clicked(event) \
                        or BCANCEL.is_clicked(event):
                    running = False

                for button, index in zip(button_dict, range(0, 12)):
                    if button_dict[button].is_clicked(event):
                        self.item.putinloadout(button, index)
            pygame.display.update()
            clock.tick(30)

    def removefromteam(self, action = None):
        if self.item.bought != None and action == None:
            Button(275, 25, 450, 450, (0, 211, 222), '', 75, (0, 211, 222)).draw()
            Button(275, 25, 450, 50, (0, 211, 222), 'Remove ' + str(self.item.name) + ' from your team?', 30, (0, 211, 222)).draw()
            Button(300, 100, 250, 250, (0, 0, 0), '', 0, (0, 0, 0), image = self.item.icon).draw()
            YVALUEFORSTATS = 0
            for num in range(1, 8):
                Button(575, 100 + (YVALUEFORSTATS * (250 / 8)), 125, 250 / 8, (0, 0, 0), self.item.statslist[num] + str(self.item.DATALIST[num]), 20, invisible = 'on').draw()
                YVALUEFORSTATS += 1
            return True
        if action != None:
            if self.item in FILE_1.ontheteam:
                self.item.onteam = None

class Totalstats:

    def __init__(self, teamlist, team):
        self.teamlist = teamlist
        self.team = team
        if self.team == 1:
            self.adding = [0, 1, 2, 3]
        elif self.team == 2:
            self.adding = [4, 5, 6, 7]
        elif self.team == 3:
            self.adding = [8, 9, 10, 11]

    def totaldamage(self):
        totalattack = 0
        for stats in self.adding:
            totalattack += self.teamlist[stats].damage
        return totalattack

    def totaldefense(self):
        totalprotection = 0
        for stats in self.adding:
            totalprotection += self.teamlist[stats].defense
        return totalprotection

    def totalhealth(self):
        totalhp = 0
        for stats in self.adding:
            totalhp += self.teamlist[stats].health
        return totalhp

    def totalcritrate(self):
        totalrate = 0
        for stats in self.adding:
            totalrate += self.teamlist[stats].critrate
        return totalrate

    def totalcritdamage(self):
        totalextra = 0
        for stats in self.adding:
            totalextra += self.teamlist[stats].critdamage
        return totalextra

    def totalspeed(self):
        quickness = 0
        for stats in self.adding:
            quickness += self.teamlist[stats].speed
        return quickness

    def totallsit(self):
        alltotal = []
        statfunctions = [self.totaldamage(), self.totaldefense(), self.totalhealth(), self.totalcritrate(), self.totalcritdamage(), self.totalspeed()]
        for stats in statfunctions:
            alltotal.append(stats)
        return alltotal

class Combat:

    def __init__(self):

        self.player1 = FILE_1.ontheteam[0]
        self.item11 = FILE_1.ontheteam[1]
        self.item12 = FILE_1.ontheteam[2]
        self.item13 = FILE_1.ontheteam[3]
        self.player2 = FILE_1.ontheteam[4]
        self.item21 = FILE_1.ontheteam[5]
        self.item22 = FILE_1.ontheteam[6]
        self.item23 = FILE_1.ontheteam[7]
        self.player3 = FILE_1.ontheteam[8]
        self.item31 = FILE_1.ontheteam[9]
        self.item32 = FILE_1.ontheteam[10]
        self.item33 = FILE_1.ontheteam[11]

        self.enemy1 = FILE_1.currentlevel[0]
        self.enemyitem11 = FILE_1.currentlevel[1]
        self.enemyitem12 = FILE_1.currentlevel[2]
        self.enemyitem13 = FILE_1.currentlevel[3]
        self.enemy2 = FILE_1.currentlevel[4]
        self.enemyitem21 = FILE_1.currentlevel[5]
        self.enemyitem22 = FILE_1.currentlevel[6]
        self.enemyitem23 = FILE_1.currentlevel[7]
        self.enemy3 = FILE_1.currentlevel[8]
        self.enemyitem31 = FILE_1.currentlevel[9]
        self.enemyitem32 = FILE_1.currentlevel[10]
        self.enemyitem33 = FILE_1.currentlevel[11]
        # damage 0 defense 1 health 2 critrate 3 critdamage 4 speed 5
        self.stats1, self.stats2, self.stats3 = Totalstats(FILE_1.ontheteam, 1).totallsit(), Totalstats(FILE_1.ontheteam, 2).totallsit(), Totalstats(FILE_1.ontheteam, 3).totallsit()
        self.estats1, self.estats2, self.estats3 = Totalstats(FILE_1.currentlevel, 1).totallsit(), Totalstats(FILE_1.currentlevel, 2).totallsit(), Totalstats(FILE_1.currentlevel, 3).totallsit()

        self.playerteam, self.enemyteam = [1, self.player1, self.item11, self.item12, self.item13, self.stats1], [1, self.enemy1, self.enemyitem11, self.enemyitem12, self.enemyitem13, self.estats1]

    def s(self, new):
        if new == 'p1':
            self.playerteam = [1, self.player1, self.item11, self.item12, self.item13, self.stats1]
        elif new == 'p2':
            self.playerteam = [2, self.player2, self.item21, self.item22, self.item23, self.stats2]
        elif new == 'p3':
            self.playerteam = [3, self.player3, self.item31, self.item32, self.item33, self.stats3]
        elif new == 'e1':
            self.enemyteam = [1, self.enemy1, self.enemyitem11, self.enemyitem12, self.enemyitem13, self.estats1]
        elif new == 'e2':
            self.enemyteam = [2, self.enemy2, self.enemyitem21, self.enemyitem22, self.enemyitem23, self.estats2]
        elif new == 'e3':
            self.enemyteam = [3, self.enemy3, self.enemyitem31, self.enemyitem32, self.enemyitem33, self.estats3]

    def combatwindow(self):
        running = True
        while running:
            BasicWorkings().basicheading('', size=30)
            Button(0, 470, 1000, 30, (0, 211, 222), '', 75, (0, 211, 222)).draw()

            # Button(499, 0, 2, 500, (255, 0, 0), '', 75, (255, 0, 0)).draw()
            global gridscreen
            gridscreen = 'on'

            '''player side'''

            Button(100, 100, 300, 300, (0, 211, 222), '', 75, (0, 211, 222), image = self.playerteam[1].icon).draw()  # player
            self.healthbar(FILE_1.ontheteam, 'player')
            bplayer1 = Button(10, 110, 80, 80, (0, 211, 222), '', 75, image = self.player1.icon).draw()  # team 1
            bplayer2 = Button(10, 210, 80, 80, (0, 211, 222), '', 75, image = self.player2.icon).draw()  # team 2
            bplayer3 = Button(10, 310, 80, 80, (0, 211, 222), '', 75, image = self.player3.icon).draw()  # team 3
            bplayeritem1 = Button(110, 410, 80, 80, (0, 211, 222), '', 75, image = self.playerteam[2].icon).draw()  # weapon 1
            bplayeritem2 = Button(210, 410, 80, 80, (0, 211, 222), '', 75, image = self.playerteam[3].icon).draw()  # weapon 2
            bplayeritem3 = Button(310, 410, 80, 80, (0, 211, 222), '', 75, image = self.playerteam[4].icon).draw()  # weapon 3

            if self.playerteam[0] == 1:
                Button(90, 140, 10, 20, (0, 211, 222), '', 75, (0, 211, 222)).draw()
                bplayer1 = Button(10, 110, 80, 80, (0, 211, 222), '', 75, (0, 211, 222), image = self.player1.icon).draw()  # team 1
            if self.playerteam[0] == 2:
                Button(90, 240, 10, 20, (0, 211, 222), '', 75, (0, 211, 222)).draw()
                bplayer2 = Button(10, 210, 80, 80, (0, 211, 222), '', 75, (0, 211, 222), image = self.player2.icon).draw()  # team 2
            if self.playerteam[0] == 3:
                Button(90, 340, 10, 20, (0, 211, 222), '', 75, (0, 211, 222)).draw()
                bplayer3 = Button(10, 310, 80, 80, (0, 211, 222), '', 75, (0, 211, 222), image = self.player3.icon).draw()  # team 3

            '''enemy side'''

            Button(600, 100, 300, 300, (0, 211, 222), '', 75, (0, 211, 222), image = self.enemyteam[1].icon).draw()  # player
            self.healthbar(FILE_1.currentlevel, 'enemy')
            benemy1 = Button(910, 110, 80, 80, (0, 211, 222), '', 75, (0, 211, 222), image = self.enemy1.icon).draw()  # team 1
            benemy2 = Button(910, 210, 80, 80, (0, 211, 222), '', 75, (0, 211, 222), image = self.enemy2.icon).draw()  # team 2
            benemy3 = Button(910, 310, 80, 80, (0, 211, 222), '', 75, (0, 211, 222), image = self.enemy3.icon).draw()  # team 3
            benemyitem1 = Button(610, 410, 80, 80, (0, 211, 222), '', 75, (0, 211, 222), image = self.enemyteam[2].icon).draw()  # weapon 1
            benemyitem2 = Button(710, 410, 80, 80, (0, 211, 222), '', 75, (0, 211, 222), image = self.enemyteam[3].icon).draw()  # weapon 2
            benemyitem3 = Button(810, 410, 80, 80, (0, 211, 222), '', 75, (0, 211, 222), image = self.enemyteam[4].icon).draw()  # weapon 3


            if self.enemyteam[0] == 1:
                Button(900, 140, 10, 20, (0, 211, 222), '', 75, (0, 211, 222)).draw()
            if self.enemyteam[0] == 2:
                Button(900, 240, 10, 20, (0, 211, 222), '', 75, (0, 211, 222)).draw()
            if self.enemyteam[0] == 3:
                Button(900, 340, 10, 20, (0, 211, 222), '', 75, (0, 211, 222)).draw()

            '''Mapping out Buttons'''

            Button(430, 130, 40, 40, (0, 211, 222), '', 75, (0, 211, 222)).draw()  # affect 1
            Button(430, 180, 40, 40, (0, 211, 222), '', 75, (0, 211, 222)).draw()  # affect 2
            Button(430, 230, 40, 40, (0, 211, 222), '', 75, (0, 211, 222)).draw()  # affect 3
            Button(430, 280, 40, 40, (0, 211, 222), '', 75, (0, 211, 222)).draw()  # affect 4
            Button(430, 330, 40, 40, (0, 211, 222), '', 75, (0, 211, 222)).draw()  # affect 5

            Button(530, 130, 40, 40, (0, 211, 222), '', 75, (0, 211, 222)).draw()  # affect 1
            Button(530, 180, 40, 40, (0, 211, 222), '', 75, (0, 211, 222)).draw()  # affect 2
            Button(530, 230, 40, 40, (0, 211, 222), '', 75, (0, 211, 222)).draw()  # affect 3
            Button(530, 280, 40, 40, (0, 211, 222), '', 75, (0, 211, 222)).draw()  # affect 4
            Button(530, 330, 40, 40, (0, 211, 222), '', 75, (0, 211, 222)).draw()  # affect 5

            # BBACK = Button(25, 25, 150, 50, (200, 20, 20), 'Back').draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    BasicWorkings().closing()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

                if self.playerteam[0] == 1:
                    if bplayer2.is_clicked(event):
                        self.s('p2')
                    if bplayer3.is_clicked(event):
                        self.s('p3')
                if self.playerteam[0] == 2:
                    if bplayer1.is_clicked(event):
                        self.s('p1')
                    if bplayer3.is_clicked(event):
                        self.s('p3')
                if self.playerteam[0] == 3:
                    if bplayer1.is_clicked(event):
                        self.s('p1')
                    if bplayer2.is_clicked(event):
                        self.s('p2')

                bplayeritem1.clicked_action(event, self.dealdamage, 'toenemy', 2)
                bplayeritem2.clicked_action(event, self.dealdamage, 'toenemy', 3)
                bplayeritem3.clicked_action(event, self.dealdamage, 'toenemy', 4)

                        # if BBACK.is_clicked(event):
                #     running = False

            pygame.display.update()
            clock.tick(30)

    def healthbar(self, team, side):
        if side == 'player':
            currenthealth = self.playerteam[5][2]
            Button(100, 50, 300, 30, (200, 200, 200), '', 20, (200, 200, 200)).draw() # health
            Button(100, 50, 300*(currenthealth/Totalstats(team, self.playerteam[0]).totalhealth()), 30, (100, 255, 0), '', 20, (100, 255, 0)).draw()
            Button(100, 50, 300, 30, (200, 200, 200), 'Health ' + str(currenthealth) + '/' + str(Totalstats(team, self.playerteam[0]).totalhealth()), 20, (200, 200, 200), invisible = 'on').draw()
        elif side == 'enemy':
            currenthealth = self.enemyteam[5][2]
            Button(600, 50, 300, 30, (200, 200, 200), '', 20, (200, 200, 200)).draw()  # health
            Button(600, 50, 300 * (currenthealth/Totalstats(team, self.enemyteam[0]).totalhealth()), 30, (100, 255, 0), '', 20, (100, 255, 0)).draw()
            Button(600, 50, 300, 30, (200, 200, 200), 'Health ' + str(currenthealth) + '/' + str(Totalstats(team, self.enemyteam[0]).totalhealth()), 20, (200, 200, 200), invisible='on').draw()

    def dealdamage(self, who, weapon):
        if who == 'toenemy':
            damagedeal = self.playerteam[5][0] * self.playerteam[weapon].power
            for x in range(1):
                t = random.randint(1, 101)
                print(t)
                if t <= self.playerteam[5][3]:
                    damagedeal *= (1+self.playerteam[5][4])
            self.enemyteam[5][2] -= int(damagedeal)

        elif who == 'toplayer':
            damagedeal = self.enemyteam[5][0] * self.enemyteam[weapon].power
            for x in range(1):
                if random.randint(1, 101) <= self.enemyteam[5][3]:
                    damagedeal *= (1+self.enemyteam[5][4])
            self.playerteam[5][2] -= int(damagedeal)

'''Weapons for player, place holder stats'''

class Weapon:

    def __init__(self, name, type, cost, basedamage, defensebonus, healthbonus, basecritrate, critdamagebonus, speedreduction, power, icon, bought = None, onteam = None, requiredlevel = 0):
        self.name = name
        self.type = type
        self.cost = cost
        self.damage = basedamage
        self.defense = defensebonus
        self.health = healthbonus
        self.critrate = basecritrate
        self.critdamage = critdamagebonus
        self.speed = -speedreduction
        self.power = power
        self.icon = icon
        self.bought = bought
        self.onteam = onteam
        self.requiredlevel = requiredlevel
        self.teamcode = None
        self.statslist = ['Cost = ', 'Type = ', 'Base Damage = ', 'Defense Bonus = ', 'Health Bonus = ', 'Base Crit Rate = ', 'Crit Damage Bonus = ', 'Weight = ']
        self.DATALIST = [self.cost, self.type, self.damage, self.defense, self.health, self.critrate, self.critdamage, self.speed]

    def inventory(self, location):
        if self.requiredlevel != 0:
            if self.requiredlevel <= FILE_1.CurrentLevel:
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

SWORD = Weapon('Sword', 'Damage', 50, 250, 150, 100, 5, .1, 15, .20, 'GAMEWEAPONS/game_sword_icon.png', requiredlevel = 1)
BOWANDARROW = Weapon('Bow and Arrows', 'Damage', 0, 250, 150, 100, 5, .1, 15, .20, 'GAMEWEAPONS/game_bow_icon.png')
DUALBALDE = Weapon('Dual Blades', 'Damage', 0, 250, 150, 100, 5, .1, 15, .20, 'GAMEWEAPONS/game_dualblade_icon.png')
CHAINKUNAI = Weapon('Chained Kunai', 'Damage', 0, 250, 150, 100, 5, .1, 15, .20, 'GAMEWEAPONS/game_chainkunai_icon.png')
SPEAR = Weapon('Spear', 'Damage', 0, 250, 150, 100, 5, .1, 15, .20, 'GAMEWEAPONS/game_spear_icon.png')
AX = Weapon('Ax', 'Damage', 50, 250, 150, 100, 5, .1, 15, .20, 'GAMEWEAPONS/game_ax_icon.png', requiredlevel = 9)
MACE = Weapon('Mace', 'Breaker', 50, 250, 150, 100, 5, .1, 15, .20, 'GAMEWEAPONS/game_mace_icon.png')
HAMMER = Weapon('Hammer', 'Breaker', 50, 250, 150, 100, 5, .1, 15, .20, 'GAMEWEAPONS/game_hammer_icon.png')
NUNCHUCKS = Weapon('Nunchucks', 'Breaker', 50, 250, 150, 100, 5, .1, 15, .20, 'GAMEWEAPONS/game_nunchucks_icon.png')
PICKAXE = Weapon('Pickaxe', 'Breaker', 50, 250, 150, 100, 5, .1, 15, .20, 'GAMEWEAPONS/game_pickaxe_icon.png')
MAGIC = Weapon('Magic', 'Breaker', 50, 250, 150, 100, 5, .1, 15, .20, 'GAMEWEAPONS/game_magic_icon.png', requiredlevel = 7)
CLUB = Weapon('Club', 'Stack', 50, 250, 150, 100, 5, .1, 15, .20, 'GAMEWEAPONS/game_club_icon.png')
BLOWGUN = Weapon('Blowgun', 'Stack', 50, 250, 150, 100, 5, .1, 15, .20, 'GAMEWEAPONS/game_blowgun_icon.png', requiredlevel = 3)
SCYTHE = Weapon('Scythe', 'Stack', 50, 250, 150, 100, 5, .1, 15, .20, 'GAMEWEAPONS/game_scythe_icon.png', requiredlevel = 5)
HEAL = Weapon('Heal', 'Heal', 50, 250, 150, 100, 5, .1, 15, .20, 'GAMEWEAPONS/game_heal_icon.png')

'''Player and enemies, place holder stats'''

class Character:

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
        self.statslist = ['Cost = ', 'Rarity = ', 'Damage Bonus = ', 'Base Defense = ', 'Base Health = ', 'Crit Rate Bonus = ', 'Base Crit Damage = ', 'Speed = ']
        self.DATALIST = [self.cost, self.type, self.damage, self.defense, self.health, self.critrate, self.critdamage, self.speed]

    def inventory(self, location):
        if self.requiredlevel != 0:
            if self.requiredlevel <= FILE_1.CurrentLevel:
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

PLAYER = Character('Player', 'Common', 0, 250, 150, 100, 5, .1, 15, 'GAMEHEROICONS/game_player_icon.png', None)
ALPIN = Character('Alpin', 'Common', 0, 250, 150, 100, 5, .1, 15, 'GAMEHEROICONS/game_alpin_icon.png', None)
GAR = Character('Gar', 'Common', 0, 250, 150, 100, 5, .1, 15, 'GAMEHEROICONS/game_gar_icon.png', None)
MARKSON = Character('Markson', 'Common', 0, 250, 150, 100, 5, .1, 15, 'GAMEHEROICONS/game_markson_icon.png', None)
SWAMP = Character('Swamp', 'Rare', 50, 250, 150, 10000, 5, .1, 15, 'GAMEHEROICONS/game_swamp_icon.png', None, requiredlevel = 2)
SISTER = Character('Sister', 'Rare', 50, 250, 150, 100, 5, .1, 15, 'GAMEHEROICONS/game_sister_icon.png', None)
TORPEDO = Character('Torpedo', 'Rare', 50, 250, 150, 100, 5, .1, 15, 'GAMEHEROICONS/game_torpedo_icon.png', None)
REAPER = Character('Reaper', 'Rare', 50, 250, 150, 100, 5, .1, 15, 'GAMEHEROICONS/game_reaper_icon.png', None, requiredlevel = 4)
MINER = Character('Miner', 'Rare', 50, 250, 150, 100, 5, .1, 15, 'GAMEHEROICONS/game_miner_icon.png', None)
RAZOR = Character('Razor', 'Rare', 50, 250, 150, 100, 5, .1, 15, 'GAMEHEROICONS/game_razor_icon.png', None)
PHANTASM = Character('Phantasm', 'Rare', 50, 250, 150, 100, 5, .1, 15, 'GAMEHEROICONS/game_phantasm_icon.png',None, requiredlevel = 6)
STALKER = Character('Stalker', 'Rare', 50, 250, 150, 100, 5, .1, 15, 'GAMEHEROICONS/game_stalker_icon.png', None, requiredlevel = 8)
VIVI = Character('Vivi', 'Epic', 50, 250, 150, 100, 5, .1, 15, 'GAMEHEROICONS/game_vivi_icon.png', None)
CLYPEUS = Character('Clypeus', 'Epic', 50, 250, 150, 100, 5, .1, 15, 'GAMEHEROICONS/game_clypeus_icon.png', None)
EXECUTIONER = Character('Executioner', 'Epic', 50, 250, 150, 1, 5, .1, 15, 'GAMEHEROICONS/game_executioner_icon.png', None, requiredlevel = 10)

def requirements(item):
    if item.requiredlevel == 0:
        return 'In Shop'
    else:
        return 'Level ' + str(item.requiredlevel)

fullweaponslist = [SWORD, BOWANDARROW, DUALBALDE, CHAINKUNAI, SPEAR, AX, MACE, HAMMER, NUNCHUCKS, PICKAXE, MAGIC, CLUB, BLOWGUN, SCYTHE, HEAL]
fullheroslist = [PLAYER, ALPIN, GAR, MARKSON, SWAMP, SISTER, TORPEDO, REAPER, MINER, RAZOR, PHANTASM, STALKER, VIVI, CLYPEUS, EXECUTIONER]

'''PLace Holders for Weapons and Characters'''

PHW = Weapon('', '', 0, 0, 0, 0, 0, 0, 0, 0, None)
PHC = Character('', '', 0, 0, 0, 0, 0, 0, 0, None, None)

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

# bobbob = ['q', 'w', 'e', 'r']
# print(bobbob)
# print(bobbob[1])
# print(bobbob)

FILE_1.ontheteam = ([PHC] + [PHW] * 3) * 3
FILE_1.currentlevel = (PLAYER, SWORD, PICKAXE, SPEAR, SWAMP, SCYTHE, BLOWGUN, HEAL, EXECUTIONER, MAGIC, CLUB, AX)
FILE_1.ontheteam = FILE_1.currentlevel
# menu()

print(Combat().player1.damage)

totalpower = Totalstats(FILE_1.ontheteam, 1).totallsit()
print(totalpower)

print(Combat().stats1)
print(Combat().stats2)
print(Combat().stats3)

if __name__ == '__main__':
    MainRun()
