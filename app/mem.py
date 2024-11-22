class Owner:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

class Restaurant:
    def __init__(self, name, address, owner):
        self.name = name
        self.address = address
        self.owner = owner
        self.tables = []
        self.departments = []

class Table:
    def __init__(self, table_number, seats):
        self.table_number = table_number
        self.seats = seats
        self.status = "available"  # Can be "available", "occupied", "reserved"

class Department:
    def __init__(self, name):
        self.name = name
        self.dishes = []

class Dish:
    def __init__(self, name, price, department):
        self.name = name
        self.price = price
        self.department = department
