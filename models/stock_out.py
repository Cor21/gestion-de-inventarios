# importaciones
from odoo import models

# es una clase que hereda models.model, lo que indica que se almacena en la bd
class StockOut(models.Model):
    # nombre tecnico
    _name = 'stock.out'
    # indica que este medulo hereda del modulo inventory.move
    _inherit = 'inventory.move'
    _description = 'Stock Out'

    # # metodo que hereda de el modulo inventory.mode, que permite saber la cantidad de productos que salen del inventario
    def get_quantity(self):
        return -self.quantity

