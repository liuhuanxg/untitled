class Person():
    def __init__(self,name,attack_power,hp):
        self.name=name
        self.attack_power=attack_power
        self.hp=hp
    def attack(self,obj):
        obj.hp-=self.attack_power
    def __str__(self):
        return '我叫{},我还有{}滴血，我的攻击力是{}'.format(self.name,self.hp,self.attack_power)
class NPC():
    def __init__(self,name,attack_power,hp):
        self.name=name
        self.attack_power=attack_power
        self.hp=hp
    def attack(self,obj):
        obj.hp-=self.attack_power
    def __str__(self):
        return '枭雄{},我还有{}滴血，我的攻击力是{}'.format(self.name,self.hp,self.attack_power)
r=Person('诸葛亮',30,100)
c=NPC('曹操',25,150)
r.attack(c)
c.attack(r)
print(c)
print(r)