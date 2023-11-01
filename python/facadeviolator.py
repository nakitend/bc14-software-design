
class Investor:
    def invest(self):
        print("Investor: Investing......")

class Vendor:
    def give(self):
        print("Vendor: Giving the materials")

class Builder:
    def build(self):
        print("Builder: Building.....")

# BuildingFacade class is removed

if __name__ == '__main__':
    investor = Investor()
    vendor = Vendor()
    builder = Builder()

    for i in range(30):
        investor.invest()  # Directly call methods on Investor

    for i in range(40):
        vendor.give()      # Directly call methods on Vendor

    for i in range(200):
        builder.build()    # Directly call methods on Builder
