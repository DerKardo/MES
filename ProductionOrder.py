class ProductionOrder: 
    __order_number = 0
    __product_name = ""
    __quantity = 0
    __status = "created"

    def __init__(self, order_number:int, product_name:str, quantity:int):
        self.__order_number = order_number
        self.__product_name = product_name
        self.__quantity = quantity

    def get_order_number(self): 
        return self.__order_number
    
    def start(self): 
        self.__status = "started"
        pass
    def finish(self):
        self.__status = "finished"
        pass
    def produce(self, units): 
        self.start
        self.__quantity += units
        self.finish
        pass
    def get_production_progress(self): 
        return self.__status