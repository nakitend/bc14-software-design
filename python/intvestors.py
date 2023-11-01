# Define the Visitor class
class Visitor:
    def visit(self):
        print("Visiting the project site")

class Investor:
    def invest(self):
        print("Investing......")

class Vendor:
    def give(self):
        print("Giving the materials")

class Builder:
    def build(self):
        print("Building.....")

class BuildingFacade:
    def __init__(self):
        self.investor = Investor()
        self.vendor = Vendor()
        self.builder = Builder()

    def build_project(self):
        for i in range(30):
            self.investor.invest()

        for i in range(40):
            self.vendor.give()

        for i in range(200):
            self.builder.build()

if __name__ == '__main__':
    facade = BuildingFacade()
    facade.build_project()

class Facade:
    def __init__(self):
        self.building_facade = BuildingFacade()
        self.visitor = Visitor()  # Create an instance of the Visitor class

    def start_project(self):
        self.building_facade.build_project()
        for i in range(100):
            self.visitor.visit()  # Use the Visitor instance to visit the project site

if __name__ == '__main__':
    facade = Facade()
    facade.start_project()
