class live:
    def eat(self):
        print("正在吃东西")
class Dog(live):
    def eat(self):
        print("猫在吃东西")
class Cat(live):
    def eat(self):
        print("猫在吃东西")
class Pig(live):
    def eat(self):
        print("猪在吃东西")
class master:
    def eat1(self,pet):
        print("主人在喂宠物")
        pet.eat()
master1=master()
master1.eat1(Dog())