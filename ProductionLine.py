import ProductionOrder


class ProductionLine: 
    def __init__(self, name): 
        self.name = name
        self.orders = []

    def add_order(self, order:ProductionOrder): 
        self.orders.append(order)

    def get_production_line_name(self): 
        return(self.name)

    def get_orders(self): 
        return self.orders