
# Sales = Sal
# Inventory = Inv
class Operaciones ():
    def __init__(self, Inventory, Sale):
        self.Inv = Inventory
        self.Sal = Sale

    def residuo (self):
        return int(self.Inv['quantity']) - int(self.Sal['quantity'])

    def subtotal (self):
        total = int(self.Sal['quantity']) * float(self.Inv['price'])
        descuento = (total * float(self.Sal['discount']))/100
        return total - descuento

    def total (self):
        iva = (self.subtotal() * float(self.Inv['tax']))/100
        return self.subtotal() + iva

    def res (self):
        resultado = []
        resultado.append(self.residuo)
        resultado.append(self.subtotal)
        resultado.append(self.total)
        return resultado