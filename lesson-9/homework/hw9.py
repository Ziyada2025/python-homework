1.class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return 3.14159 * self.radius ** 2
    
    def calculate_perimeter(self):
        return 2 * 3.14159 * self.radius

# Create a circle object
my_circle = Circle(5)

# Calculate and display results
print("Circle with radius:", my_circle.radius)
print("Area:", my_circle.calculate_area())
print("Perimeter:", my_circle.calculate_perimeter()) 
2.from datetime import datetime

class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth
    
    def calculate_age(self):
        today = datetime.now()
        birth_date = datetime.strptime(self.date_of_birth, "%Y-%m-%d")
        age = today.year - birth_date.year
        
        # Check if birthday hasn't occurred yet this year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
        
        return age

# Create a person object
person1 = Person("John Doe", "USA", "1990-05-15")

# Display person details and age
print("Name:", person1.name)
print("Country:", person1.country)
print("Date of Birth:", person1.date_of_birth)
print("Age:", person1.calculate_age(), "years old") 
3.class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b 
4.class Shape:
    def calculate_area(self):
        pass
    
    def calculate_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return 3.14159 * self.radius ** 2
    
    def calculate_perimeter(self):
        return 2 * 3.14159 * self.radius

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def calculate_area(self):
        # Using Heron's formula
        s = (self.side1 + self.side2 + self.side3) / 2
        return (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5
    
    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def calculate_area(self):
        return self.side ** 2
    
    def calculate_perimeter(self):
        return 4 * self.side

# Create objects and calculate
circle = Circle(5)
triangle = Triangle(3, 4, 5)
square = Square(6)

print("Circle - Radius: 5")
print("  Area:", circle.calculate_area())
print("  Perimeter:", circle.calculate_perimeter())
print()

print("Triangle - Sides: 3, 4, 5")
print("  Area:", triangle.calculate_area())
print("  Perimeter:", triangle.calculate_perimeter())
print()

print("Square - Side: 6")
print("  Area:", square.calculate_area())
print("  Perimeter:", square.calculate_perimeter()) 
5.class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root is None:
            self.root = {'value': value, 'left': None, 'right': None}
        else:
            self._insert(value, self.root)
    
    def _insert(self, value, node):
        if value < node['value']:
            if node['left'] is None:
                node['left'] = {'value': value, 'left': None, 'right': None}
            else:
                self._insert(value, node['left'])
        else:
            if node['right'] is None:
                node['right'] = {'value': value, 'left': None, 'right': None}
            else:
                self._insert(value, node['right'])
    
    def search(self, value):
        return self._search(value, self.root)
    
    def _search(self, value, node):
        if node is None:
            return False
        if value == node['value']:
            return True
        elif value < node['value']:
            return self._search(value, node['left'])
        else:
            return self._search(value, node['right'])
    
    def show_sorted(self):
        result = []
        self._inorder(self.root, result)
        return result
    
    def _inorder(self, node, result):
        if node:
            self._inorder(node['left'], result)
            result.append(node['value'])
            self._inorder(node['right'], result)

# Simple usage
bst = BinarySearchTree()

# Add numbers
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)

# Check if numbers exist
print("40 in tree?", bst.search(40))  # True
print("90 in tree?", bst.search(90))  # False

# Show all numbers in order
print("Sorted numbers:", bst.show_sorted()) 
6.class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack is empty"
    
    def is_empty(self):
        return len(self.items) == 0

# Usage
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print("Popped:", s.pop())  # 30
print("Popped:", s.pop())  # 20 
7.class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def delete(self, data):
        current = self.head
        if current and current.data == data:
            self.head = current.next
            return
        
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next
        
        if current:
            prev.next = current.next
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Usage
ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.display()  # 30 -> 20 -> 10 -> None
ll.delete(20)
ll.display()  # 30 -> 10 -> None 
8.class ShoppingCart:
    def __init__(self):
        self.items = {}
    
    def add_item(self, item, price, quantity=1):
        if item in self.items:
            self.items[item]['quantity'] += quantity
        else:
            self.items[item] = {'price': price, 'quantity': quantity}
    
    def remove_item(self, item, quantity=1):
        if item in self.items:
            self.items[item]['quantity'] -= quantity
            if self.items[item]['quantity'] <= 0:
                del self.items[item]
    
    def total_price(self):
        total = 0
        for item, details in self.items.items():
            total += details['price'] * details['quantity']
        return total

# Usage
cart = ShoppingCart()
cart.add_item("Apple", 1.50, 3)
cart.add_item("Banana", 0.75, 5)
cart.add_item("Milk", 3.00, 1)
print("Total:", cart.total_price())  # 1.5*3 + 0.75*5 + 3.0*1
cart.remove_item("Apple", 1)
print("After removal:", cart.total_price()) 
9.class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack is empty"
    
    def display(self):
        print("Stack:", self.items)
    
    def is_empty(self):
        return len(self.items) == 0

# Usage
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()  # Stack: [10, 20, 30]
print("Popped:", s.pop())
s.display()  # Stack: [10, 20] 
10.class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return "Queue is empty"
    
    def is_empty(self):
        return len(self.items) == 0

# Usage
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print("Dequeued:", q.dequeue())  # 10
print("Dequeued:", q.dequeue())  # 20 
11.class Bank:
    def __init__(self):
        self.accounts = {}
    
    def create_account(self, account_number, initial_balance=0):
        if account_number not in self.accounts:
            self.accounts[account_number] = initial_balance
            return f"Account {account_number} created with ${initial_balance}"
        return "Account already exists"
    
    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number] += amount
            return f"Deposited ${amount}. New balance: ${self.accounts[account_number]}"
        return "Account not found"
    
    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number] >= amount:
                self.accounts[account_number] -= amount
                return f"Withdrew ${amount}. New balance: ${self.accounts[account_number]}"
            return "Insufficient funds"
        return "Account not found"
    
    def check_balance(self, account_number):
        if account_number in self.accounts:
            return f"Balance: ${self.accounts[account_number]}"
        return "Account not found"

# Usage
bank = Bank()
print(bank.create_account("12345", 1000))
print(bank.deposit("12345", 500))
print(bank.withdraw("12345", 200))
print(bank.check_balance("12345"))
