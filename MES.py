from ProductionLine import ProductionLine


class MES: 
    def __init__(self): 
        self.productionLine = []
        pass

    def add_production_line(self, name): 
        self.productionLine.append(ProductionLine(name))
        pass

    def create_production_order(self, production_line_name, order_number:int),  
        self.get_production_line(production_line_name).add_order(order_number)
        pass
    def produce_units(self, production_line_name, order_number, units): 
        #UNDONE
        pass

    def get_production_lines(self):
        return self.productionLine
        pass 
        
    def get_production_line(self, name)->ProductionLine:
        if name in self.productionLine:
            return self.productionLine(self.productionLine.index(name))
        else:
            return False
