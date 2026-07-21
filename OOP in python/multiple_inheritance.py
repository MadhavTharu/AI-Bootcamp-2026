class Father:
    def money(self):
        print("Father has money")

class Mother:
    def love(self):
        print("Mother has love")

class child(Father,Mother):
    pass

c= child()
c.money()
c.love()
