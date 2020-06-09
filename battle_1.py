class Monster:
    def __init__(self,init_hp):
      if (init_hp > 0):
          self.hp = init_hp
      else:
          print('体力は0以上')
          self.hp = 1

goblin=Monster(50)
wizardsnake = Monster(100)

print('ゴブリンの体力'+str(goblin.hp))
