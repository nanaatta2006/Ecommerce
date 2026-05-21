# 🛍️ Interactive Smart E-Commerce System

A terminal-based e-commerce app in **83 lines of Python** — no dependencies required.

---

## 🚀 How to Run

```bash
python main.py
```

Requires Python 3.x+. No installs needed.

---

## 📋 Menu Options

```
====================================
     ✨ SMART E-COMMERCE HUB ✨
====================================
 [1] 📜 View Available Products
 [2] 🛒 Add Product to Cart
 [3] 👀 View Current Cart
 [4] 💳 Proceed to Checkout
 [5] ❌ Exit Application
====================================
```

- Products are dynamically indexed as simple sequential IDs (**1, 2, 3...**) for quick and easy input.
- Displays split items using elegant terminal alignments for **Physical** (📦) and **Digital** (💻).
- Checkout automatically applies distinct algorithmic discounts per product type.
- All faulty inputs (letters, out-of-bounds numbers, out-of-stock actions) are handled gracefully without crashing.

---

## ⚙️ OOP Requirements

### 1 — Abstract Blueprint
`Product(ABC)` serves as the core base structure. It strictly prevents direct instantiation and forces every subclass to implement `apply_discount()` and `display_info(idx)` via `@abstractmethod`.

### 2 — Inheritance
| Class | Extra Attributes | Specialization Rule |
|-------|------------------|---------------------|
| `PhysicalProduct` | `weight` | Handles real-world shipping weights in kg |
| `DigitalProduct` | `file_size` | Manages file download sizes in MB |

Both classes seamlessly utilize `super().__init__()` to inherit and reuse shared metadata logic.

### 3 — Encapsulation
The catalog's highly sensitive fields (`price` and `stock`) are safely protected as private properties (`self.__price`, `self.__stock`). External modifications are strictly routed through custom `@property` setters containing validation rules that instantly reject negative logical inputs.

```python
product.price = -20  # raises ValueError("Negative price")
```

### 4 — Polymorphism
`ShoppingCart.checkout()` loops over all active elements and triggers `item.apply_discount()`. The loop remains entirely free from complex conditional checking, yet achieves unique behaviors based on object mutation:

| Product Type | Concrete Dynamic Rule |
|--------------|----------------------|
| **Physical** | Deducts 10% off the base price + charges a $2.0 shipping rate per kg |
| **Digital** | Automatically executes a flat 20% off deduction with zero delivery fees |

---

## 👤 Author

**[Your Name]** — [Student ID]
