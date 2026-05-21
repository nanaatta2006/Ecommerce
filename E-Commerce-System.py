from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, name, price, stock):
        self.name, self.price, self.stock = name, price, stock

    @property
    def price(self): return self.__price
    @price.setter
    def price(self, val):
        if val < 0: raise ValueError("Negative price")
        self.__price = val

    @property
    def stock(self): return self.__stock
    @stock.setter
    def stock(self, val):
        if val < 0: raise ValueError("Negative stock")
        self.__stock = val

    @abstractmethod
    def apply_discount(self): pass
    @abstractmethod
    def display_info(self, item_id): pass

class PhysicalProduct(Product):
    def __init__(self, name, price, stock, weight):
        super().__init__(name, price, stock); self.weight = weight
    def apply_discount(self): return (self.price * 0.9) + (self.weight * 2.0)
    def display_info(self, idx):
        return f" [{idx}] 📦 {self.name:<22} | Price: ${self.price:<5.2f} | Stock: {self.stock:<3} | {self.weight}kg"

class DigitalProduct(Product):
    def __init__(self, name, price, stock, file_size):
        super().__init__(name, price, stock); self.file_size = file_size
    def apply_discount(self): return self.price * 0.8
    def display_info(self, idx):
        return f" [{idx}] 💻 {self.name:<22} | Price: ${self.price:<5.2f} | Stock: {self.stock:<3} | {self.file_size}MB"

class ShoppingCart:
    def __init__(self): self.items = []
    def add_product(self, product):
        if product.stock <= 0: return print("\n❌ Out of stock!")
        product.stock -= 1; self.items.append(product)
        print(f"\n🛍️ Added [{product.name}] to cart.")
    def view_cart(self):
        if not self.items: return print("\n🛒 Your cart is empty.")
        print("\n--- 🛒 CURRENT CART ---")
        for i, item in enumerate(self.items, 1): print(f" {i}. {item.name:<22} - ${item.price:.2f}")
    def checkout(self):
        if not self.items: return print("\n❌ Cart is empty.")
        print("\n============ 🧾 RECEIPT ============"); tot = disc = 0
        for item in self.items:
            tot += item.price; dp = item.apply_discount(); disc += dp
            print(f" • {item.name:<22} Final: ${dp:.2f}")
        print(f"------------------------------------\n Original Total: ${tot:.2f}\n 🚀 Grand Total: ${disc:.2f}\n====================================")
        self.items.clear()

def main():
    inv = [
        PhysicalProduct("Mechanical Keyboard", 120.0, 5, 1.2),
        PhysicalProduct("Heavy Duty Desk Mat", 35.0, 10, 0.8),
        DigitalProduct("Python Mastery E-Book", 30.0, 999, 15.0),
        DigitalProduct("Lo-Fi Beats Pack", 15.0, 999, 450.0)
    ]
    cart = ShoppingCart()
    while True:
        print("\n====================================\n     ✨ SMART E-COMMERCE HUB ✨\n====================================\n [1] 📜 View Available Products\n [2] 🛒 Add Product to Cart\n [3] 👀 View Current Cart\n [4] 💳 Proceed to Checkout\n [5] ❌ Exit Application\n====================================")
        choice = input("👉 Select option (1-5): ").strip()
        if choice == "1":
            print("\n--- 📜 AVAILABLE PRODUCTS ---")
            for i, p in enumerate(inv, 1): print(p.display_info(i))
        elif choice == "2":
            idx = input("👉 Enter Product Number (ID): ").strip()
            if idx.isdigit() and 1 <= int(idx) <= len(inv): cart.add_product(inv[int(idx) - 1])
            else: print("\n❌ Invalid ID. Choose a valid product number.")
        elif choice == "3": cart.view_cart()
        elif choice == "4": cart.checkout()
        elif choice == "5": print("\n👋 Goodbye!"); break
        else: print("\n❌ Invalid selection. Try again.")

if __name__ == "__main__":
    main()