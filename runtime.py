class methodoverride1:
    def display(self):
        print("method invoked from base class")
class methodOverride2(methodoverride1):
    def display(self):
        print("method invoked from derived class")
ob=methodOverride2()
ob.display()