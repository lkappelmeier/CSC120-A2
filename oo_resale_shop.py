class ResaleShop:
    # What attributes will it need?
    # The ResaleShop class will need an inventory attribute. 
    # How will you set up your constructor?
    # We can set up the inventory as an empty list that we can append. We also have to include self
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.item_id = 0
        self.inventory = {}

    # What methods will you need?
    # We need to be able to buy, sell, and refurbish the computer, and also update the price. 
    def buy_computer(self, computer):
        self.item_id += 1
        self.inventory[self.item_id] = computer
        return self.item_id
    
    def update_price(self, new_price:int, item_id:int):
        if item_id in self.inventory: # finding the item
            self.inventory[item_id]["price"] = new_price
        else:
            print("Item", item_id, "not found. Cannot update price.")
    
    def sell_computer(self, item_id:int):
        if item_id in self.inventory:
            del self.inventory[item_id] # deleting the computer from the inventory
            print("Item", item_id, "sold!")
        else:
            print("Item",item_id, "not found. Please select another item to sell.")

    def print_inventory(self):
        if self.inventory:
            # for each item
            for item_id in self.inventory:
                #print its details
                print(f'Item ID: {item_id} : {self.inventory[item_id]}')
        else:
            print("No inventory to display.")

    def refurbish(self, item_id:int):
        if item_id in self.inventory:
            computer = self.inventory[item_id] # locate the computer
            if int(computer["year_made"]) < 2000:
                computer["price"] = 0 # too old to sell, donation only
            elif int(computer["year_made"]) < 2012:
                computer["price"] = 250 # heavily discounted for being over 10 years old
            elif int(computer["year_made"]) < 2018:
                computer["price"] = 550 # discounted for slightly less recent, 4-10 years, computer
            else:
                computer["price"] = 1000 # last 4 or 5 years

            if self.new_os is not None: 
                computer["operating_system"] = self.new_os #updating operating system information
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")
def main():
    shop = ResaleShop()
    shop.buy_computer({"description":"2019 MacBook Pro", "processor_type":"Intel", "hard_drive_capacity":256, "memory":16, "operating_system":"High Sienna", "year_made":2019, "price":1000})
    shop.update_price(2000, 1)
    shop.print_inventory()

main()
        