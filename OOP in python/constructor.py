class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model= model

    def show(self):
        print(self.brand,self.model)

c1=car("Toyota","Corolla")
c1.show()
