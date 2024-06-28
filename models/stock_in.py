
# importaciones
from odoo import models, api

# es una clase que hereda models.model, lo que indica que se almacena en la bd
class StockIn(models.Model):
    # nombre tecnico
    _name = 'stock.in'
    # indica que este medulo hereda del modulo inventory.move
    _inherit = 'inventory.move'
    _description = 'Stock In'

    # metodo que hereda de el modulo inventory.mode, que permite saber la cantidad de productos que entran al inventario
    def get_quantity(self):
        return self.quantity
