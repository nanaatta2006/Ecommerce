# 🛍️ Interactive Smart E-Commerce System

A terminal-based e-commerce app in **129 lines of Python** — no dependencies required.

---

## 🚀 How to Run

```bash
python ecommerce.py
```

Requires Python 3.10+. No installs needed.

---

## 📋 Menu Options

```
[1] View Products   [2] Add to Cart
[3] View Cart       [4] Checkout   [5] Exit
```

- Products are split into **Physical** (📦) and **Digital** (💾)
- Add items by entering their ID number
- Checkout automatically applies discounts per product type
- All bad input (letters, invalid IDs, out-of-stock) is caught gracefully

---

## ⚙️ OOP Requirements

### 1 — Abstract Blueprint
`Product(ABC)` is the base class. It cannot be instantiated directly and forces every subclass to implement `apply_discount()` and `display_info()` via `@abstractmethod`.

### 2 — Inheritance
| Class | Extra attributes |
|-------|-----------------|
| `PhysicalProduct` | `weight`, `ship_cost` |
| `DigitalProduct` | `link`, `size` |

Both call `super().__init__()` to reuse shared logic.

### 3 — Encapsulation
`price` and `stock` are private (`self.__price`, `self.__stock`) and only accessible through `@property` setters that reject negative values and wrong types.

```python
product.price = -50  # raises ValueError
```

### 4 — Polymorphism
`ShoppingCart.checkout()` calls `p.apply_discount()` on every item — same call, different behaviour:

| Type | Rule |
|------|------|
| Physical | 10% off + shipping fee added |
| Digital | 20% off, no shipping |

---

## 👤 Author

Abdelrhman Khaled Atta
