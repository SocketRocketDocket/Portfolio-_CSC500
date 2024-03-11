# Class for items
class ItemToPurchase:
    def __init__(self, item_name='none', item_price=0, item_quantity=0, item_description='No description'):
        self.item_name = item_name
        self.item_price = float(item_price)
        self.item_quantity = int(item_quantity)
        self.item_description = item_description
# Print attributes
    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}'.center(32))
# Class for user's cart
class ShoppingCart:
    def __init__(self, customer_name='none', current_date='January 1, 2020'):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []
# Add item function
    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)
        print(f'{ItemToPurchase.item_name} has been added to the cart.'.center(32))
# Remove item function
    def remove_item(self, item_name):
        found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                found = True
                print(f'{item_name} has been removed from the cart.'.center(32))
                break
        if not found:
            print('Item not found in cart. Nothing removed.'.center(32))
# Change item quantity function
    def change_item_quantity(self):
        item_name = input('Enter the item name to change quantity: '.center(32)).strip()
        found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                new_quantity = int(input('Enter the new quantity: '.center(32)))
                item.item_quantity = new_quantity
                print(f'Quantity for {item_name} has been updated to {new_quantity}.'.center(32))
                found = True
                break
        if not found:
            print('Item not found in cart. Quantity not changed.'.center(32))
# Total cost function
    def get_cost_of_cart(self):
        return sum(item.item_price * item.item_quantity for item in self.cart_items)
# Cart output function
    def print_total(self):
        print('\n      OUTPUT SHOPPING CART'.center(32))
        if not self.cart_items:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}".center(32))
            print('SHOPPING CART IS EMPTY'.center(32))
        else:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}".center(32))
            print('Number of Items: {}'.format(sum(item.item_quantity for item in self.cart_items)).center(32))
            total_cost = 0
            for item in self.cart_items:
                total_cost += item.item_price * item.item_quantity
                item.print_item_cost()
            print(f'Total: ${total_cost}'.center(32))
# Cart descriptions function
    def print_descriptions(self):
        print('\nOUTPUT ITEM DESCRIPTIONS'.center(32))
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}".center(32))
        print('Item Descriptions:'.center(32))
        for item in self.cart_items:
            print(f'{item.item_name}: {item.item_description}'.center(32))
# Menu function
def print_menu(shoppingCart):
    menu_options = {
        'a': 'Add item to cart',
        'r': 'Remove item from cart',
        'c': 'Change item quantity',
        'i': "Output items' descriptions",
        'o': 'Output shopping cart',
        'q': 'Quit'
    }
# User input item function
    def add_item_to_cart():
        item_name = input('Enter the item name: '.center(32))
        item_price = float(input('Enter the item price: '.center(32)))
        item_quantity = int(input('Enter the item quantity: '.center(32)))
        item_description = input('Enter the item description: '.center(32))
        new_item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
        shoppingCart.add_item(new_item)
# User input remove function
    def remove_item_from_cart():
        item_name = input('Enter the item name to remove: '.center(32))
        shoppingCart.remove_item(item_name)
# User incput quantity change function
    def change_item_quantity():
        shoppingCart.change_item_quantity()
   
    while True:
        print('\n' + 'MENU'.center(32))
        for key, value in menu_options.items():
            print(f'{key} - {value}'.center(32))
        choice = input('Choose an option: '.center(32))
        
        if choice == 'a':
            add_item_to_cart()
        elif choice == 'r':
            remove_item_from_cart()
        elif choice == 'c':
            change_item_quantity()
        elif choice == 'i':
            shoppingCart.print_descriptions()
        elif choice == 'o':
            shoppingCart.print_total()
        elif choice == 'q':
            print('Quit'.center(32))
            break
        else:
            print('Invalid option. Please try again.'.center(32))
# Main program
def main():
    customer_name = input("Enter customer's name: ")
    current_date = input('Enter date: ') 
    shopping_cart = ShoppingCart(customer_name, current_date)
    print_menu(shopping_cart)

if __name__ == '__main__':
    main()
