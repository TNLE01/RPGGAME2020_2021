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

    def draw_text(self, text, font, color, surface, x, y, type = 'center'):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        if type == 'center':
            textrect.center = (x, y)
        elif type == 'midleft':
            textrect.midleft = (x, y)
        elif type == 'midright':
            textrect.midright = (x, y)
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

    def __init__(self, ShopLastOpen, TeamLastOpen, Gold, XP, CurrentLevel, text_display, timer):
        self.ShopLastOpen = ShopLastOpen
        self.TeamLastOpen = TeamLastOpen
        self.Gold = Gold
        self.XP = XP
        self.CurrentLevel = CurrentLevel
        self.ontheteam = None
        self.currentlevel = None
        self.text_displayed = text_display
        self.timer = timer

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

    def text_guild(self):
        if self.timer <= 75:
            Button(0, 490, 1000, 10, (219, 219, 219), self.text_displayed, 15,hovercolor = (219, 219, 219)).draw()

FILE_1 = Profile('Heroes', 'Team', 0, 0, 1, 'Welcome to the Coliseum', 0)
#FILE_2 = Profile()
#FILE_3 = Profile()

def helpful_text(newtext = None, reset = None):
    if newtext != None:
        FILE_1.text_displayed = newtext
    if reset != None:
        FILE_1.timer = 0
    FILE_1.text_guild()
    FILE_1.timer += 1

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

            helpful_text()

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

                BMAP.clicked_action(event, self.map)
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
            button_dict = {}
            BasicWorkings().basicheading('Map')

            BBACK = Button(25, 25, 150, 50, (200, 20, 20), 'Back').draw()

            buttonslist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
            XVFB, YVFB = [1, 0], [112, 0]
            for button in buttonslist:
                button_dict[button] = Button(XVFB[0]*(575/6) + (XVFB[1]*85), YVFB[0], 85, 85, (0, 242, 255), str(button)).draw()
                XVFB[0], XVFB[1], YVFB[1] = (XVFB[0] + 1), (XVFB[1] + 1), (YVFB[1] + 1)
                if YVFB[1] == 5:
                    XVFB, YVFB = [1, 0], [YVFB[0] + 97, 0]

            # XVALUEFORLINE = 0
            # YVALUEFORLINE = 100
            # for x in range(21):
            #     pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(XVALUEFORLINE, 100, 1, 500))
            #     XVALUEFORLINE += 200
            # for y in range(11):
            #     pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, YVALUEFORLINE, 1000, 1))
            #     YVALUEFORLINE += 100

            helpful_text()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    BasicWorkings().closing()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                if BBACK.is_clicked(event):
                    running = False
                for button in button_dict:
                    button_dict[button].clicked_action(event, Popup(PHW, button, 'level', 'Complete previous Level').selectionbox, 50)

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
                    BHEROES = Button(310, 125, 150, 50, (0, 242, 255), 'Heroes', 30).draw()
                    BWEAPONS = Button(540, 125, 150, 50, (0, 242, 255), 'Weapons', 30).draw()
                    BUPGRADES = Button(770, 125, 150, 50, (0, 242, 255), 'Upgrades', 30).draw()

                    buttonslist = ['B10', 'B11', 'B12', 'B13', 'B20', 'B21', 'B22', 'B23', 'B30', 'B31', 'B32', 'B33']
                    XVALUEFORBUTTONTEAM = [47.5, 365, 682.5]
                    XVALUEFORBUTTONWEAPONS = [237.5, 555, 872.5]
                    YVALUEFORBUTTONWEAPONS = [215, 310, 405]

                    FILE_1.ontheteam = ([PHC] + [PHW] * 3) * 3
                    for weapon, hero in zip(fullweaponslist, fullheroeslist):
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

                    helpful_text()

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
                        if BHEROES.is_clicked(event):
                            slide = 'Heroes'
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
            if slide == 'Heroes':
                while running:
                    BasicWorkings().basicheading('Team')
                    pygame.draw.rect(screen, (0, 211, 222), pygame.Rect(270, 100, 230, 500 / 5))

                    BBACK = Button(25, 25, 150, 50, (200, 20, 20), 'Back').draw()
                    BTEAM = Button(80, 125, 150, 50, (0, 242, 255), 'Team', 30).draw()
                    Button(310, 125, 150, 50, (0, 211, 222), 'Heroes', 55, (0, 211, 222)).draw()
                    BWEAPONS = Button(540, 125, 150, 50, (0, 242, 255), 'Weapons', 30).draw()
                    BUPGRADES = Button(770, 125, 150, 50, (0, 242, 255), 'Upgrades', 30).draw()

                    buttonslist = ['BPLAYER', 'BALPIN', 'BGAR', 'BMARKSON', 'BSWAMP', 'BSISTER', 'BTORPEDO', 'BREAPER', 'BMINER', 'BRAZOR', 'BPHANTASM', 'BSTALKER', 'BVIVI', 'BCLYPEUS', 'BEXECUTIONER']
                    for button, hero, x, y in zip(buttonslist, fullheroeslist, itertools.cycle(XVALUEFORBUTTON), YVALUEFORBUTTON):
                        button_dict[button] = Button(x, y, 80, 80, (0, 211, 222), requirements(hero), 25, image = hero.inventory('self')).draw()

                    helpful_text()

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
                        for button, hero in zip(button_dict, fullheroeslist):
                            button_dict[button].clicked_action(event, Popup(hero, 'hero', 'team', requirements(hero)).selectionbox)
                    pygame.display.update()
                    clock.tick(30)
            if slide == 'Weapons':
                while running:
                    BasicWorkings().basicheading('Team')
                    pygame.draw.rect(screen, (0, 211, 222), pygame.Rect(500, 100, 230, 500 / 5))

                    BBACK = Button(25, 25, 150, 50, (200, 20, 20), 'Back').draw()
                    BTEAM = Button(80, 125, 150, 50, (0, 242, 255), 'Team', 30).draw()
                    BHEROES = Button(310, 125, 150, 50, (0, 242, 255), 'Heroes', 30).draw()
                    Button(540, 125, 150, 50, (0, 211, 222), 'Weapons', 55, (0, 211, 222)).draw()
                    BUPGRADES = Button(770, 125, 150, 50, (0, 242, 255), 'Upgrades', 30).draw()

                    buttonslist = ['BSWORD', 'BBOW', 'BDUALBLADE', 'BCHAINKUNAI', 'BSPEAR', 'BAX', 'BMACE', 'BHAMMER', 'BNUNCHUCKS', 'BPICKAXE', 'BMAGIC', 'BCLUB', 'BBLOWGUN', 'BSCYTHE', 'BHEAL']
                    for button, weapon, x, y in zip(buttonslist, fullweaponslist, itertools.cycle(XVALUEFORBUTTON), YVALUEFORBUTTON):
                        button_dict[button] = Button(x, y, 80, 80, (0, 211, 222), requirements(weapon), 25, image = weapon.inventory('self')).draw()

                    helpful_text()

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
                        if BHEROES.is_clicked(event):
                            slide = 'Heroes'
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
                    BHEROES = Button(310, 125, 150, 50, (0, 242, 255), 'Heroes', 30).draw()
                    BWEAPONS = Button(540, 125, 150, 50, (0, 242, 255), 'Weapons', 30).draw()
                    Button(770, 125, 150, 50, (0, 211, 222), 'Upgrades', 55, (0, 211, 222)).draw()

                    Button(25, 265, 170, 170, (0, 242, 255), '', image = 'GAMEUPGRADES/game_upgrades_attack.png').draw()
                    Button(220, 265, 170, 170, (0, 242, 255), '', image = 'GAMEUPGRADES/game_upgrades_defense.png').draw()
                    Button(415, 265, 170, 170, (0, 242, 255), '', image = 'GAMEUPGRADES/game_upgrades_health.png').draw()
                    Button(610, 265, 170, 170, (0, 242, 255), '', image = 'GAMEUPGRADES/game_upgrades_crit_rate.png').draw()
                    Button(805, 265, 170, 170, (0, 242, 255), '', image = 'GAMEUPGRADES/game_upgrades_crit_damage.png').draw()

                    helpful_text()

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
                        if BHEROES.is_clicked(event):
                            slide = 'Heroes'
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
            if slide == 'Heroes':
                while running:
                    BasicWorkings().basicheading('Shop')
                    pygame.draw.rect(screen, (0, 211, 222), pygame.Rect(50, 100, 300, 500 / 5))

                    BBACK = Button(25, 25, 150, 50, (200, 20, 20), 'Back').draw()
                    Button(100, 125, 200, 50, (0, 211, 222), 'Heroes', 75, (0, 211, 222)).draw()
                    BWEAPONS = Button(400, 125, 200, 50, (0, 242, 255), 'Weapons').draw()
                    BUPGRADES = Button(700, 125, 200, 50, (0, 242, 255), 'Upgrades').draw()

                    buttonslist = ['BPLAYER', 'BALPIN', 'BGAR', 'BMARKSON', 'BSISTER', 'BTORPEDO', 'BMINER', 'BRAZOR', 'BVIVI', 'BCLYPEUS']
                    heroeslist = [PLAYER, ALPIN, GAR, MARKSON, SISTER, TORPEDO, MINER, RAZOR, VIVI, CLYPEUS]
                    for button, hero, x, y in zip(buttonslist, heroeslist, itertools.cycle(XVALUEFORBUTTON), YVALUEFORBUTTON):
                        button_dict[button] = Button(x, y, 135, 135, (0, 211, 222), 'Recruited', 35, image = hero.inventory('shop')).draw()

                    helpful_text()

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
                        for button, hero in zip(button_dict, heroeslist):
                            button_dict[button].clicked_action(event, Popup(hero, 'hero', 'buy', 'Recruited').selectionbox)
                    pygame.display.update()
                    clock.tick(30)
            if slide == 'Weapons':
                while running:
                    BasicWorkings().basicheading('Shop')
                    pygame.draw.rect(screen, (0, 211, 222), pygame.Rect(350, 100, 300, 500 / 5))

                    BBACK = Button(25, 25, 150, 50, (200, 20, 20), 'Back').draw()
                    BHEROES = Button(100, 125, 200, 50, (0, 242, 255), 'Heroes').draw()
                    Button(400, 125, 200, 50, (0, 211, 222), 'Weapons', 75, (0, 211, 222)).draw()
                    BUPGRADES = Button(700, 125, 200, 50, (0, 242, 255), 'Upgrades').draw()

                    buttonslist = ['BBOW', 'BDUALBLADE', 'BCHAINKUNAI', 'BSPEAR', 'BMACE', 'BHAMMER', 'BNUNCHUCKS', 'BPICKAXE', 'BCLUB', 'BHEAL']
                    weaponslist = [BOWANDARROW, DUALBALDE, CHAINKUNAI, SPEAR, MACE, HAMMER, NUNCHUCKS, PICKAXE, CLUB, HEAL]
                    for button, weapon, x, y in zip(buttonslist, weaponslist, itertools.cycle(XVALUEFORBUTTON), YVALUEFORBUTTON):
                        button_dict[button] = Button(x, y, 135, 135, (0, 211, 222), 'Sold Out', 35, image = weapon.inventory('shop')).draw()

                    helpful_text()

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
                        if BHEROES.is_clicked(event):
                            slide = 'Heroes'
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
                    BHEROES = Button(100, 125, 200, 50, (0, 242, 255), 'Heroes').draw()
                    BWEAPONS = Button(400, 125, 200, 50, (0, 242, 255), 'Weapons').draw()
                    Button(700, 125, 200, 50, (0, 211, 222), 'Upgrades', 75, (0, 211, 222)).draw()

                    Button(25, 265, 170, 170, (0, 242, 255), '', image = 'GAMEUPGRADES/game_upgrades_attack.png').draw()
                    Button(220, 265, 170, 170, (0, 242, 255), '', image = 'GAMEUPGRADES/game_upgrades_defense.png').draw()
                    Button(415, 265, 170, 170, (0, 242, 255), '', image = 'GAMEUPGRADES/game_upgrades_health.png').draw()
                    Button(610, 265, 170, 170, (0, 242, 255), '', image = 'GAMEUPGRADES/game_upgrades_crit_rate.png').draw()
                    Button(805, 265, 170, 170, (0, 242, 255), '', image = 'GAMEUPGRADES/game_upgrades_crit_damage.png').draw()

                    helpful_text()

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
                        if BHEROES.is_clicked(event):
                            slide = 'Heroes'
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

            helpful_text()

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

            helpful_text()

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

            helpful_text()

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
            if self.use == 'level':
                key = self.levels()

            if key == True:
                BCANCEL = Button(275 + 50 / 3, 400, 200, 50, (200, 20, 20), 'Cancel').draw()
                BACCEPT = Button(475 + 100 / 3, 400, 200, 50, (20, 200, 20), 'Accept').draw()

            else:
                if self.donothing != None:
                    return
                self.TEXT(size)

            helpful_text()

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
        if self.use == 'level':
            self.levels(action = 'on')

    def buying(self, action = None):
        if self.item.bought == None and action == None:
            Button(275, 25, 450, 450, (0, 211, 222), '', 75, (0, 211, 222)).draw()
            Button(275, 25, 450, 50, (0, 211, 222), 'Do you wish to buy: ' + str(self.item.name) + '?', 30, (0, 211, 222)).draw()
            Button(300, 100, 250, 250, (0, 0, 0), '', 0, (0, 0, 0), image = self.item.icon).draw()
            YVALUEFORSTATS = 0
            for num in range(0, 8):
                Button(575, 100 + (YVALUEFORSTATS * (250 / 8)), 125, 250 / 8, (0, 0, 0),
                       self.item.statslist[num] + str(self.item.DATALIST[num]), 20, invisible = 'on').draw()
                YVALUEFORSTATS += 1
            return True
        if action != None:
            if FILE_1.Gold >= self.item.cost:
                FILE_1.change('gold', -self.item.cost)
                self.item.bought = 'yes'
                helpful_text('Just recuited ' + self.item.name, 0) if self.type == 'hero' else helpful_text('Just bought ' + self.item.name, 0)
            else:
                helpful_text('Not enough gold', 0)

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

            for weapon, hero in zip(fullweaponslist, fullheroeslist):
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

            helpful_text()

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

    def levels(self, action = None):
        if FILE_1.CurrentLevel >= self.type and action == None:
            Button(275, 25, 450, 450, (0, 211, 222), '', 75, (0, 211, 222)).draw()
            Button(275, 25, 450, 50, (0, 211, 222), 'Enter Level ' + str(self.type) + '?', 30, (0, 211, 222)).draw()
            return True
        if action != None:
            hero_indexes, weapon_indexes, heroes_in_team = [0, 4, 8], [1, 2, 3], 3
            for hindex in hero_indexes:
                if FILE_1.ontheteam[hindex] == PHC:
                    heroes_in_team -= 1
                else:
                    hero_with_weapon = [True, True, True]
                    for windex in weapon_indexes:
                        if FILE_1.ontheteam[hindex + windex] == PHW:
                            hero_with_weapon[windex - 1] = False
                    if hero_with_weapon == [False, False, False]:
                        heroes_in_team = 1000

            if heroes_in_team == 0:
                helpful_text('No teammates on team', 0)
            elif heroes_in_team > 3:
                helpful_text("Teammate doesn't have weapon", 0)
            else:
                Combat().start()

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

    def totallist(self):
        alltotal = []
        statfunctions = [self.totaldamage(), self.totaldefense(), self.totalhealth(), self.totalcritrate(), self.totalcritdamage(), self.totalspeed()]
        for stats in statfunctions:
            alltotal.append(stats)
        return alltotal

class Combat:

    def __init__(self):

        self.player1, self.enemy1 = FILE_1.ontheteam[0], FILE_1.currentlevel[0]
        self.item11, self.item12, self.item13 = FILE_1.ontheteam[1], FILE_1.ontheteam[2], FILE_1.ontheteam[3]
        self.enemyitem11, self.enemyitem12, self.enemyitem13 = FILE_1.currentlevel[1], FILE_1.currentlevel[2], FILE_1.currentlevel[3]

        self.player2, self.enemy2 = FILE_1.ontheteam[4], FILE_1.currentlevel[4]
        self.item21, self.item22, self.item23 = FILE_1.ontheteam[5], FILE_1.ontheteam[6], FILE_1.ontheteam[7]
        self.enemyitem21, self.enemyitem22, self.enemyitem23 = FILE_1.currentlevel[5], FILE_1.currentlevel[6], FILE_1.currentlevel[7]

        self.player3, self.enemy3 = FILE_1.ontheteam[8], FILE_1.currentlevel[8]
        self.item31, self.item32, self.item33 = FILE_1.ontheteam[9], FILE_1.ontheteam[10], FILE_1.ontheteam[11]
        self.enemyitem31, self.enemyitem32, self.enemyitem33= FILE_1.currentlevel[9], FILE_1.currentlevel[10], FILE_1.currentlevel[11]

        # damage 0 defense 1 health 2 critrate 3 critdamage 4 speed 5
        self.stats1, self.stats2, self.stats3 = Totalstats(FILE_1.ontheteam, 1).totallist(), Totalstats(FILE_1.ontheteam, 2).totallist(), Totalstats(FILE_1.ontheteam, 3).totallist()
        self.estats1, self.estats2, self.estats3 = Totalstats(FILE_1.currentlevel, 1).totallist(), Totalstats(FILE_1.currentlevel, 2).totallist(), Totalstats(FILE_1.currentlevel, 3).totallist()

        self.playerteam, self.enemyteam = [1, self.player1, self.item11, self.item12, self.item13, self.stats1, 'p1'], [1, self.enemy1, self.enemyitem11, self.enemyitem12, self.enemyitem13, self.estats1, 'e1']

        self.round, self.recentmessage = 1, ['Enemy ' + self.enemyteam[1].name + ' stands in your way', '', '', '', '']

        self.playerstatus, self.enemystatus, self.playerlistdata, self.enemylistdata = ['a'] * 3, ['a'] * 3, ['p1', 'p2', 'p3'], ['e1', 'e2', 'e3']

        self.player_effects, self.enemy_effects = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]] # [[0]*5]*3

        self.damagedeal, self.attack_style = 0, ''

    def start(self):

        if self.player1 == PHC:
            self.playerstatus[0] = 'd'
            self.playerlistdata.remove('p1')

        if self.enemy1 == PHC:
            self.enemystatus[0] = 'd'
            self.enemylistdata.remove('e1')

        if self.player2 == PHC:
            self.playerstatus[1] = 'd'
            self.playerlistdata.remove('p2')

        if self.enemy2 == PHC:
            self.enemystatus[1] = 'd'
            self.enemylistdata.remove('e2')

        if self.player3 == PHC:
            self.playerstatus[2] = 'd'
            self.playerlistdata.remove('p3')

        if self.enemy3 == PHC:
            self.enemystatus[2] = 'd'
            self.enemylistdata.remove('e3')

        self.combatwindow()

    def s(self, new):

        if new == 'p1':
            self.playerteam = [1, self.player1, self.item11, self.item12, self.item13, self.stats1, 'p1']
        elif new == 'p2':
            self.playerteam = [2, self.player2, self.item21, self.item22, self.item23, self.stats2, 'p2']
        elif new == 'p3':
            self.playerteam = [3, self.player3, self.item31, self.item32, self.item33, self.stats3, 'p3']
        elif new == 'e1':
            self.enemyteam = [1, self.enemy1, self.enemyitem11, self.enemyitem12, self.enemyitem13, self.estats1, 'e1']
        elif new == 'e2':
            self.enemyteam = [2, self.enemy2, self.enemyitem21, self.enemyitem22, self.enemyitem23, self.estats2, 'e2']
        elif new == 'e3':
            self.enemyteam = [3, self.enemy3, self.enemyitem31, self.enemyitem32, self.enemyitem33, self.estats3, 'e3']

        elif new == 'rp':
            if self.playerstatus != ['d'] * 3:
                self.s(random.choice(self.playerlistdata))
            else:
                pass
        elif new == 're':
            if self.enemystatus != ['d'] * 3:
                self.s(random.choice(self.enemylistdata))
            else:
                pass

    def combatwindow(self):
        running = True
        while running:
            BasicWorkings().basicheading('', size = 30)
            Button(0, 470, 1000, 30, (0, 211, 222), '', 75, (0, 211, 222)).draw()
            Button(450, 50, 100, 50, (0, 211, 222), 'Round ' + str(self.round), invisible = 'on').draw()

            # Button(499, 0, 2, 500, (255, 0, 0), '', 75, (255, 0, 0)).draw()
            # global gridscreen
            # gridscreen = 'on'

            if self.playerstatus[self.playerteam[0] - 1] == 'd':
                self.s('rp')
            elif self.enemystatus[self.enemyteam[0] - 1] == 'd':
                self.s('re')

            '''player side'''

            Button(100, 100, 300, 300, (0, 211, 222), '', 75, (0, 211, 222), image = self.playerteam[1].icon).draw()  # player
            self.healthbar(FILE_1.ontheteam, 'player')

            bplayer1 = Button(10, 110, 80, 80, (0, 211, 222), '', 75, image = self.player1.icon).draw() if self.playerstatus[0] == 'a' else Button(10, 110, 80, 80, (217, 15, 39), '', 75, (217, 15, 39), image = self.player1.icon).draw() # team 1
            bplayer2 = Button(10, 210, 80, 80, (0, 211, 222), '', 75, image = self.player2.icon).draw() if self.playerstatus[1] == 'a' else Button(10, 210, 80, 80, (217, 15, 39), '', 75, (217, 15, 39), image = self.player2.icon).draw() # team 2
            bplayer3 = Button(10, 310, 80, 80, (0, 211, 222), '', 75, image = self.player3.icon).draw() if self.playerstatus[2] == 'a' else Button(10, 310, 80, 80, (217, 15, 39), '', 75, (217, 15, 39), image = self.player3.icon).draw() # team 3

            bplayeritem1 = Button(110, 410, 80, 80, (0, 211, 222), '', 75, image = self.playerteam[2].icon).draw() if self.playerteam[2] != PHW else Button(0, 0, 0, 0, (0, 0, 0), '', invisible = 'on') # weapon 1
            bplayeritem2 = Button(210, 410, 80, 80, (0, 211, 222), '', 75, image = self.playerteam[3].icon).draw() if self.playerteam[3] != PHW else Button(0, 0, 0, 0, (0, 0, 0), '', invisible = 'on') # weapon 2
            bplayeritem3 = Button(310, 410, 80, 80, (0, 211, 222), '', 75, image = self.playerteam[4].icon).draw() if self.playerteam[4] != PHW else Button(0, 0, 0, 0, (0, 0, 0), '', invisible = 'on') # weapon 3

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

            benemy1 = Button(910, 110, 80, 80, (0, 211, 222), '', 75, (0, 211, 222), image = self.enemy1.icon).draw() if self.enemystatus[0] == 'a' else Button(910, 110, 80, 80, (217, 15, 39), '', 75, (217, 15, 39), image = self.enemy1.icon).draw() # team 1
            benemy2 = Button(910, 210, 80, 80, (0, 211, 222), '', 75, (0, 211, 222), image = self.enemy2.icon).draw() if self.enemystatus[1] == 'a' else Button(910, 210, 80, 80, (217, 15, 39), '', 75, (217, 15, 39), image = self.enemy2.icon).draw() # team 2
            benemy3 = Button(910, 310, 80, 80, (0, 211, 222), '', 75, (0, 211, 222), image = self.enemy3.icon).draw() if self.enemystatus[2] == 'a' else Button(910, 310, 80, 80, (217, 15, 39), '', 75, (217, 15, 39), image = self.enemy3.icon).draw() # team 3

            # benemyitem1 = Button(610, 410, 80, 80, (0, 211, 222), '', 75, (0, 211, 222), image = self.enemyteam[2].icon).draw()  # weapon 1
            # benemyitem2 = Button(710, 410, 80, 80, (0, 211, 222), '', 75, (0, 211, 222), image = self.enemyteam[3].icon).draw()  # weapon 2
            # benemyitem3 = Button(810, 410, 80, 80, (0, 211, 222), '', 75, (0, 211, 222), image = self.enemyteam[4].icon).draw()  # weapon 3

            if self.enemyteam[0] == 1:
                Button(900, 140, 10, 20, (0, 211, 222), '', 75, (0, 211, 222)).draw()
            if self.enemyteam[0] == 2:
                Button(900, 240, 10, 20, (0, 211, 222), '', 75, (0, 211, 222)).draw()
            if self.enemyteam[0] == 3:
                Button(900, 340, 10, 20, (0, 211, 222), '', 75, (0, 211, 222)).draw()

            self.affects()

            self.textwindow()

            # BBACK = Button(25, 25, 150, 50, (200, 20, 20), 'Back').draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    BasicWorkings().closing()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

                if self.playerteam[0] == 1:
                    if bplayer2.is_clicked(event) and self.playerstatus[1] == 'a':
                        self.s('p2')
                    if bplayer3.is_clicked(event) and self.playerstatus[2] == 'a':
                        self.s('p3')
                if self.playerteam[0] == 2:
                    if bplayer1.is_clicked(event) and self.playerstatus[0] == 'a':
                        self.s('p1')
                    if bplayer3.is_clicked(event) and self.playerstatus[2] == 'a':
                        self.s('p3')
                if self.playerteam[0] == 3:
                    if bplayer1.is_clicked(event) and self.playerstatus[0] == 'a':
                        self.s('p1')
                    if bplayer2.is_clicked(event) and self.playerstatus[1] == 'a':
                        self.s('p2')

                enemy_weapon_choice = random.randint(2, 4) if self.enemyteam[4] != PHW else random.randint(2, 3) if self.enemyteam[3] != PHW else random.randint(2, 2)

                if self.playerteam[2] != PHW:
                    bplayeritem1.clicked_action(event, self.speedfactor, 'toenemy', 2, enemy_weapon_choice)
                if self.playerteam[3] != PHW:
                    bplayeritem2.clicked_action(event, self.speedfactor, 'toenemy', 3, enemy_weapon_choice)
                if self.playerteam[4] != PHW:
                    bplayeritem3.clicked_action(event, self.speedfactor, 'toenemy', 4, enemy_weapon_choice)

                if self.playerstatus == ['d'] * 3:
                    running = False
                    helpful_text('You lose', 0)
                elif self.enemystatus == ['d'] * 3:
                    running = False
                    helpful_text('You win', 0)

                # if BBACK.is_clicked(event):
                #     running = False

            pygame.display.update()
            clock.tick(30)

    def healthbar(self, team, side):
        # a = "neg" if b < 0 else "pos" if b > 0 else "zero"
        whos_hp = [self.playerteam, 100] if side == 'player' else [self.enemyteam, 600]
        current_health = whos_hp[0][5][2]
        BAR = 300*(current_health/Totalstats(team, whos_hp[0][0]).totalhealth())
        current_color = 0 if BAR > 250 else 1 if BAR > 200 else 2 if BAR > 150 else 3 if BAR > 100 else 4 if BAR > 50 else 5
        health_color = [(0, 255, 0), (100, 255, 0), (200, 255, 0), (255, 200, 0), (255, 100, 0), (255, 0, 0)]

        Button(whos_hp[1], 50, 300, 30, (200, 200, 200), '', 20, (200, 200, 200)).draw() # health
        Button(whos_hp[1], 50, BAR, 30, health_color[current_color], '', 20, health_color[current_color]).draw()
        Button(whos_hp[1], 50, 300, 30, (200, 200, 200), 'Health ' + str(int(current_health)) + '/' + str(Totalstats(team, whos_hp[0][0]).totalhealth()), 20, (200, 200, 200), invisible = 'on').draw()

    def speedfactor(self, who, weapon, enemy_weapon, forced = None):

        if forced == None:

            self.s('re')
            Button(600, 100, 300, 300, (0, 211, 222), '', 75, (0, 211, 222), image = self.enemyteam[1].icon).draw()  # player
            self.healthbar(FILE_1.currentlevel, 'enemy')

            self.assign_abilities('before', [self.playerteam, 'Player'], [self.enemyteam, 'Enemy'], weapon)
            self.assign_abilities('before', [self.enemyteam, 'Enemy'], [self.playerteam, 'Player'], enemy_weapon)

            self.affects()

        if self.playerteam[5][5] > self.enemyteam[5][5] or forced == 'playerfirst':
            self.textloop('Player goes first')
            self.dealdamage(who, weapon)

            if self.enemystatus[(self.enemyteam[0] - 1)] == 'd':
                self.textloop('can not attack enemy is dead')
            else:

                self.dealdamage('toplayer', enemy_weapon)

            self.round += 1

        elif self.playerteam[5][5] < self.enemyteam[5][5] or forced == 'enemyfirst':
            self.textloop('Enemy goes first')
            self.dealdamage('toplayer', enemy_weapon)

            if self.playerstatus[(self.playerteam[0] - 1)] == 'd':
                self.textloop('can not attack player is dead')
            else:

                self.dealdamage(who, weapon)

            self.round += 1

        #if speed is the same do a coin flip'''

        else:
            self.textloop('Player and Enemy has the same speed, a coin will be flipped')
            coin = 0
            for side in range(1):
                coin = random.randint(1, 2)
            if coin == 1:
                self.speedfactor(who, weapon, enemy_weapon, 'playerfirst')
            elif coin == 2:
                self.speedfactor(who, weapon, enemy_weapon, 'enemyfirst')

    def dealdamage(self, who, weapon):

        if who == 'toenemy':
            attacker, defender, status, listdata, effects = [self.playerteam, 'Player'], [self.enemyteam, 'Enemy'], self.enemystatus, self.enemylistdata, [self.player_effects, self.enemy_effects]
        elif who == 'toplayer':
            attacker, defender, status, listdata, effects = [self.enemyteam, 'Enemy'], [self.playerteam, 'Player'], self.playerstatus, self.playerlistdata, [self.enemy_effects, self.player_effects]

        self.attack_style = attacker[1] + ' deal '

        for x in range(1):
            if random.randint(1, 100) <= defender[0][5][5]:
                self.textloop(defender[1] + "'s " + defender[0][1].name + ' dodge the attack')
            else:

                total_attack = attacker[0][5][0]*1.075 if attacker[0][weapon].type == 'Damage' else attacker[0][5][0]
                total_defense = defender[0][5][1]*.75 if attacker[0][weapon].type == 'Breaker' else defender[0][5][1]

                ####Abilities(attacker[0], defender[0], total_attack, total_defense, effects[0], effects[1], weapon).damage_cal()

                self.damagedeal = ((total_attack**2)/(total_attack + total_defense)) * attacker[0][weapon].power

                self.assign_abilities('attack', attacker, defender, weapon, total_attack, total_defense)

                extradamage = 0
                for x in range(1):
                    if random.randint(1, 100) <= attacker[0][5][3]:
                        self.damagedeal *= (1 + (attacker[0][5][4] * 0.01))
                        extradamage = 1
                # defender[0][5][2] -= int(damagedeal)
                self.smoothhpdrop(self.damagedeal / 100, who)
                damagetext = self.attack_style + str(int(self.damagedeal)) + ' damage' if extradamage == 0 else 'Critical hit, ' + self.attack_style + str(int(self.damagedeal)) + ' damage!'

                self.assign_abilities('after', attacker, defender, weapon, total_attack, total_defense)

                self.affects()

                self.textloop(damagetext)
                if defender[0][5][2] <= 0:
                    status[(defender[0][0] - 1)] = 'd'
                    listdata.remove(defender[0][6])
                    self.textloop(defender[1] + "'s " + defender[0][1].name + ' died')

    def smoothhpdrop(self, damagedeal, who):
        theteam = FILE_1.currentlevel if who == 'toenemy' else FILE_1.ontheteam
        healthbar = 'enemy' if who == 'toenemy' else 'player'
        side = self.enemyteam if who == 'toenemy' else self.playerteam
        damagetimer = 0
        while damagetimer < 100:

            side[5][2] -= damagedeal
            damagetimer += 1

            self.healthbar(theteam, healthbar)

            if side[5][2] <= 0:
                break

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    BasicWorkings().closing()

            pygame.display.update()
            clock.tick(30)

    def affects(self):

        Button(400, 100, 200, 300, (255, 255, 255), '', 75, (255, 255, 255)).draw()

        for affect, x_num in zip(self.player_effects[self.playerteam[0] - 1], range(0, 5)):
            if affect == 0:
                pass
            else:
                Button(430, 130 + (50*x_num), 40, 40, (0, 211, 222), '', 75, (0, 211, 222), image = affect).draw()

        # Button(430, 130, 40, 40, (0, 211, 222), '', 75, (0, 211, 222)).draw()  # affect 1
        # Button(430, 180, 40, 40, (0, 211, 222), '', 75, (0, 211, 222)).draw()  # affect 2
        # Button(430, 230, 40, 40, (0, 211, 222), '', 75, (0, 211, 222)).draw()  # affect 3
        # Button(430, 280, 40, 40, (0, 211, 222), '', 75, (0, 211, 222)).draw()  # affect 4
        # Button(430, 330, 40, 40, (0, 211, 222), '', 75, (0, 211, 222)).draw()  # affect 5

        for affect, x_num in zip(self.enemy_effects[self.enemyteam[0] - 1], range(0, 5)):
            if affect == 0:
                pass
            else:
                Button(530, 130 + (50*x_num), 40, 40, (0, 211, 222), '', 75, (0, 211, 222), image = affect).draw()

        # Button(530, 130, 40, 40, (0, 211, 222), '', 75, (0, 211, 222)).draw()  # affect 1
        # Button(530, 180, 40, 40, (0, 211, 222), '', 75, (0, 211, 222)).draw()  # affect 2
        # Button(530, 230, 40, 40, (0, 211, 222), '', 75, (0, 211, 222)).draw()  # affect 3
        # Button(530, 280, 40, 40, (0, 211, 222), '', 75, (0, 211, 222)).draw()  # affect 4
        # Button(530, 330, 40, 40, (0, 211, 222), '', 75, (0, 211, 222)).draw()  # affect 5

    def assign_abilities(self, phrase, attacker_side, defender_side, current_weapon, attacking_power = 0, defending_power = 0):

        team = [FILE_1.ontheteam, FILE_1.currentlevel] if attacker_side[1] == 'Player' else [FILE_1.currentlevel, FILE_1.ontheteam]
        team_status = self.playerstatus if attacker_side[1] == 'Player' else self.enemystatus

        if phrase == 'before':

            if attacker_side[0][1] == ALPIN and defender_side[0][5][2] > (Totalstats(team[1], defender_side[0][0]).totalhealth()*0.5): # ALPIN
                self.affects_symbols(ALPIN.icon, defender_side[0])



                self.textloop(defender_side[0][1].name + ' has been slowed')


            if attacker_side[0][1] == SISTER: # SISTER
                self.affects_symbols(attacker_side[0][1].icon, attacker_side[0])

            if attacker_side[0][1] == TORPEDO: # TORPEDO
                self.affects_symbols(attacker_side[0][1].icon, attacker_side[0])

            if attacker_side[0][1] == REAPER: # REAPER
                self.affects_symbols(attacker_side[0][1].icon, attacker_side[0])

            if attacker_side[0][1] == MINER: # MINER
                self.affects_symbols(attacker_side[0][1].icon, attacker_side[0])

            if attacker_side[0][1] == PHANTASM: # PHANTASM
                for status in team_status:
                    if status == 'd':
                        self.affects_symbols(attacker_side[0][1].icon, attacker_side[0])
                        break

            if self.round >= 5 and attacker_side[0][1] == STALKER: # STALKER
                self.affects_symbols(attacker_side[0][1].icon, attacker_side[0])

            if attacker_side[0][1] == EXECUTIONER: # EXECUTIONER
                self.affects_symbols(attacker_side[0][1].icon, attacker_side[0])

        elif phrase == 'attack':

            if attacker_side[0][current_weapon].type == 'Stack':
                self.affects_symbols(attacker_side[0][current_weapon].icon, defender_side[0])
                self.attack_style = attacker_side[1] + ' poisoned ' + defender_side[1] + ' with '

            if attacker_side[0][current_weapon].type == 'Damage' and attacker_side[0][1] == RAZOR: # RAZOR
                self.affects_symbols(attacker_side[0][1].icon, defender_side[0])

        elif phrase == 'after':

            if attacker_side[0][1] == PLAYER and defender_side[0][5][2] <= 0:  # PLAYER
                self.affects_symbols(PLAYER.icon, attacker_side[0])

            if defender_side[0][5][2] <= (Totalstats(team[1], defender_side[0][0]).totalhealth()*0.5): # ALPIN
                self.affects_symbols(ALPIN.icon, defender_side[0], 'remove')

            if defender_side[0][1] == GAR and defender_side[0][5][2] <= (Totalstats(team[1], defender_side[0][0]).totalhealth()*0.3): # GAR
                self.affects_symbols(defender_side[0][1].icon, defender_side[0])

            if defender_side[0][1] == SWAMP:
                self.affects_symbols(SWAMP.icon, attacker_side[0])

            if defender_side[0][1] == CLYPEUS and defender_side[0][5][2] <= (Totalstats(team[1], defender_side[0][0]).totalhealth()*0.4): # CLYPEUS
                self.affects_symbols(defender_side[0][1].icon, defender_side[0])

            if defender_side[0][1] == VIVI and defender_side[0][5][2] <= (Totalstats(team[1], defender_side[0][0]).totalhealth()*0.4): # VIVI
                self.affects_symbols(defender_side[0][1].icon, defender_side[0])

        elif phrase == 'death':
            pass

    def affects_symbols(self, add, side, to_do = 'add'):

        current = False
        current_counter = 0
        team = [self.playerteam, self.player_effects] if side == self.playerteam else [self.enemyteam, self.enemy_effects]

        if to_do == 'add':
            for affect in team[1][team[0][0] - 1]:
                if affect == add:
                    current = True
            if current == False:
                for affect in team[1][team[0][0] - 1]:
                    if affect == 0:
                        current_counter += 1
                if current_counter == 0:
                    del team[1][team[0][0] - 1][-1]
                    team[1][team[0][0] - 1].insert(0, add)
                else:
                    team[1][team[0][0] - 1].insert(-current_counter, add)

        elif to_do == 'remove':
            for affect in team[1][team[0][0] - 1]:
                if affect == add:
                    team[1][team[0][0] - 1].remove(add)

    def textloop(self, newmessage):
        del self.recentmessage[-1]
        self.recentmessage.insert(0, newmessage)
        self.textwindow()

    def textwindow(self):
        Button(550, 400, 400, 100, (0, 211, 222), '', 75, (0, 211, 222)).draw()  # player

        # Button(555, 405, 390, 90, (255, 255, 255), message, 25, (255, 255, 255)).draw()

        for num in range(0, 5):
            Button(555, 405 + (18 * num), 390, 18, (255, 255, 255), self.recentmessage[num], 20, (255, 255, 255)).draw()

        # BasicWorkings().draw_text(message + message, BasicWorkings().fontstuff(20), (50, 100, 150), screen, 555, 405 + (18/2), 'midleft')

'''Abilities'''

class Abilities:

    def __init__(self, attacker_side, defender_side, attacking_power, defending_power, attacker_effects, defender_effects, current_weapon):
        self.attacker_side = attacker_side
        self.defender_side = defender_side
        self.attacking_power = attacking_power
        self.defending_power = defending_power
        self.attacker_effects = attacker_effects
        self.defender_effects = defender_effects
        self.current_weapon = current_weapon

    def damage_cal(self):

        if PLAYER.icon in self.attacker_effects:
            print('bob')
        # if
        # if
        # if
        # if
        # if
        # if
        # if
        # if
        # if
        # if
        # if
        # if
        # if
        # if

    def for_honor(self): # PLAYER # Killing an enemy will boost attack
        pass

    def freeze(self): # ALPIN # reduce the speed of enemies when they are above 50% health
        pass

    def rage(self): # GAR # Gain attack boost below 30% health
        pass

    def incraese_scope(self): # MARKSON # Enemies marked by Markson will take increase damage
        pass

    def poisonous(self): # SWAMP # Attacking Swamp will cause poison effect
        pass

    def blessing(self): # SISTER # Heal after each attack
        pass

    def quick_attack(self): # TORPEDO # More power to attack if Torpedo has higher speed
        pass

    def soul_reap(self): # REAPER # Gain health when enemy dies
        pass

    def explosives(self): # MINER # Damages enemy upon death
        pass

    def bleed(self): # RAZOR # Weapons with damage type will cause bleeding
        pass

    def nightmare(self): # PHANTASM # Boost attack if team has dead teammates
        pass

    def weak_spots(self): # STALKER # Enemies after round five will have their defenses lowered
        pass

    def seduction(self): # VIVI # Increase crit when below 40% health
        pass

    def defense_boost(self): # CLYPEUS # Gain shield below 40% health
        pass

    def instant_death(self): # EXECUTIONER # Low chance to instantly kill enemies
        pass

'''Weapons for player, place holder stats'''

class Weapon:

    def __init__(self, name, type, cost, basedamage, defensebonus, healthbonus, basecritrate, critdamagebonus, speedreduction, takeupspace, power, icon, bought = None, onteam = None, requiredlevel = 0):
        self.name = name
        self.type = type
        self.cost = cost
        self.damage = basedamage
        self.defense = defensebonus
        self.health = healthbonus
        self.critrate = basecritrate
        self.critdamage = critdamagebonus
        self.speed = -speedreduction
        self.space = takeupspace
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

SWORD = Weapon('Sword', 'Damage', 50, 250, 150, 100, 5, 10, 15, 1,.20, 'GAMEWEAPONS/game_sword_icon.png', requiredlevel = 1)
BOWANDARROW = Weapon('Bow and Arrows', 'Damage', 0, 250, 150, 100, 5, 10, 15, 1, .20, 'GAMEWEAPONS/game_bow_icon.png')
DUALBALDE = Weapon('Dual Blades', 'Damage', 0, 250, 150, 100, 5, 10, 15, 1, .20, 'GAMEWEAPONS/game_dualblade_icon.png')
CHAINKUNAI = Weapon('Chained Kunai', 'Damage', 0, 250, 150, 100, 5, 10, 15, 1, .20, 'GAMEWEAPONS/game_chainkunai_icon.png')
SPEAR = Weapon('Spear', 'Damage', 0, 250, 150, 100, 5, 10, 15, 1, .20, 'GAMEWEAPONS/game_spear_icon.png')
AX = Weapon('Ax', 'Damage', 50, 250, 150, 100, 5, 10, 15, 1, .20, 'GAMEWEAPONS/game_ax_icon.png', requiredlevel = 9)
MACE = Weapon('Mace', 'Breaker', 50, 250, 150, 100, 5, 10, 15, 1, .20, 'GAMEWEAPONS/game_mace_icon.png')
HAMMER = Weapon('Hammer', 'Breaker', 50, 250, 150, 100, 5, 10, 15, 1, .20, 'GAMEWEAPONS/game_hammer_icon.png')
NUNCHUCKS = Weapon('Nunchucks', 'Breaker', 50, 250, 150, 100, 5, 10, 15, 1, .20, 'GAMEWEAPONS/game_nunchucks_icon.png')
PICKAXE = Weapon('Pickaxe', 'Breaker', 50, 250, 150, 100, 5, 10, 15, 1, .20, 'GAMEWEAPONS/game_pickaxe_icon.png')
MAGIC = Weapon('Magic', 'Breaker', 50, 250, 150, 100, 5, 10, 15, 1, .20, 'GAMEWEAPONS/game_magic_icon.png', requiredlevel = 7)
CLUB = Weapon('Club', 'Stack', 50, 250, 150, 100, 5, 10, 15, 1, .20, 'GAMEWEAPONS/game_club_icon.png')
BLOWGUN = Weapon('Blowgun', 'Stack', 50, 250, 150, 100, 5, 10, 15, 1, .20, 'GAMEWEAPONS/game_blowgun_icon.png', requiredlevel = 3)
SCYTHE = Weapon('Scythe', 'Stack', 50, 250, 150, 100, 5, 10, 15, 1, .20, 'GAMEWEAPONS/game_scythe_icon.png', requiredlevel = 5)
HEAL = Weapon('Heal', 'Heal', 50, 250, 150, 100, 5, 10, 15, 1, .20, 'GAMEWEAPONS/game_heal_icon.png')

'''Player and enemies, place holder stats'''

class Character:

    def __init__(self, name, rarity, cost, basedamage, basedefense, basehealth, critratebonus, basecritdamage, speed, availablespace, icon, profile, bought = None, onteam = None, requiredlevel = 0):
        self.name = name
        self.type = rarity
        self.cost = cost
        self.damage = basedamage
        self.defense = basedefense
        self.health = basehealth
        self.critrate = critratebonus
        self.critdamage = basecritdamage
        self.speed = speed
        self.space = availablespace
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
            for hero in fullheroeslist:
                if hero.onteam == place:
                    hero.onteam = None
                    hero.teamcode = None
            self.onteam = place
            self.teamcode = placeindex
            print(self.onteam, placeindex)

PLAYER = Character('Player', 'Common', 0, 250, 1500, 1000, 5, 10, 15, 3, 'GAMEHEROICONS/game_player_icon.png', None)
ALPIN = Character('Alpin', 'Common', 0, 250, 150, 100, 5, 10, 15, 3, 'GAMEHEROICONS/game_alpin_icon.png', None)
GAR = Character('Gar', 'Common', 0, 250, 150, 100, 5, 10, 15, 3, 'GAMEHEROICONS/game_gar_icon.png', None)
MARKSON = Character('Markson', 'Common', 0, 250, 150, 100, 5, 10, 15, 3, 'GAMEHEROICONS/game_markson_icon.png', None)
SWAMP = Character('Swamp', 'Rare', 50, 250, 150, 100, 5, 10, 15, 3, 'GAMEHEROICONS/game_swamp_icon.png', None, requiredlevel = 2)
SISTER = Character('Sister', 'Rare', 50, 250, 150, 100, 5, 10, 15, 3, 'GAMEHEROICONS/game_sister_icon.png', None)
TORPEDO = Character('Torpedo', 'Rare', 50, 250, 150, 100, 5, 10, 15, 3, 'GAMEHEROICONS/game_torpedo_icon.png', None)
REAPER = Character('Reaper', 'Rare', 50, 250, 150, 100, 5, 10, 15, 3, 'GAMEHEROICONS/game_reaper_icon.png', None, requiredlevel = 4)
MINER = Character('Miner', 'Rare', 50, 250, 150, 100, 5, 10, 15, 3, 'GAMEHEROICONS/game_miner_icon.png', None)
RAZOR = Character('Razor', 'Rare', 50, 250, 150, 100, 5, 10, 15, 3, 'GAMEHEROICONS/game_razor_icon.png', None)
PHANTASM = Character('Phantasm', 'Rare', 50, 250, 150, 100, 5, 10, 15, 3, 'GAMEHEROICONS/game_phantasm_icon.png',None, requiredlevel = 6)
STALKER = Character('Stalker', 'Rare', 50, 250, 150, 100, 5, 10, 15, 3, 'GAMEHEROICONS/game_stalker_icon.png', None, requiredlevel = 8)
VIVI = Character('Vivi', 'Epic', 50, 250, 150, 100, 5, 10, 15, 3, 'GAMEHEROICONS/game_vivi_icon.png', None)
CLYPEUS = Character('Clypeus', 'Epic', 50, 250, 150, 700, 5, 10, 15, 3, 'GAMEHEROICONS/game_clypeus_icon.png', None)
EXECUTIONER = Character('Executioner', 'Epic', 50, 250, 150, 100, 5, 10, 15, 3, 'GAMEHEROICONS/game_executioner_icon.png', None, requiredlevel = 10)

def requirements(item):
    if item.requiredlevel == 0:
        return 'In Shop'
    else:
        return 'Level ' + str(item.requiredlevel)

fullweaponslist = [SWORD, BOWANDARROW, DUALBALDE, CHAINKUNAI, SPEAR, AX, MACE, HAMMER, NUNCHUCKS, PICKAXE, MAGIC, CLUB, BLOWGUN, SCYTHE, HEAL]
fullheroeslist = [PLAYER, ALPIN, GAR, MARKSON, SWAMP, SISTER, TORPEDO, REAPER, MINER, RAZOR, PHANTASM, STALKER, VIVI, CLYPEUS, EXECUTIONER]

'''PLace Holders for Weapons and Characters'''

PHW = Weapon('', '', 0, 0, 0, 0, 0, 0, 0, 0, 0, None)
PHC = Character('', '', 0, 0, 0, 0, 0, 0, 0, 0, None, None)


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
FILE_1.currentlevel = (ALPIN, CLUB, BLOWGUN, SCYTHE, SWAMP, SPEAR, PICKAXE, HEAL, CLYPEUS, MAGIC, SWORD, AX)
FILE_1.ontheteam = (CLYPEUS, SWORD, PICKAXE, SCYTHE, PLAYER, SPEAR, BLOWGUN, HEAL, ALPIN, MAGIC, CLUB, AX)
# menu()

# print(Combat().player1.damage)
#
# totalpower = Totalstats(FILE_1.ontheteam, 1).totallist()
# print(totalpower)
#
# print(Combat().stats1)
# print(Combat().stats2)
# print(Combat().stats3)
#
# deff = 900
#
# print((1000) * (((deff)/(deff + 100))))
#
# print((1000**2)/(1000 + deff))

# print(((1000**2)/(1000 + 600))*.2)
# print(((1000**2)/(1000 + 300))*.2)
# print(((1000**2)/(1000 + 560))*.2)
# print(((1075**2)/(1075 + 700))*.2)

if __name__ == '__main__':
    MainRun()
