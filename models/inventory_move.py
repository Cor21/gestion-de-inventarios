# models/inventory_move.py

# Importaciones
from odoo import models, fields


# Aquí se define una clase llamada `InventoryMove` que hereda de `models.AbstractModel`.
# Esto indica que es un modelo abstracto, lo que significa que no se almacenará
# directamente en la base de datos, sino que está destinado a ser heredado por otros modelos.

class InventoryMove(models.AbstractModel):
    # atributos del modelo

    # nombre tecnico del modelo
    _name = 'inventory.move'
    _description = 'Inventory Move'

    #  product_id es de tipo Many2one que crea una relación de muchos a uno con el modelo product.
    # Representa el producto involucrado en el movimiento de inventario.
    product_id = fields.Many2one('product', string='Producto', required=True)
    # quantity es de tipo float y hace referencia a la cantidad de producto que se mueve
    quantity = fields.Float(string='Cantidad', required=True)
    # move_date es de tipo Datetime que hace referencia a la fecha del movimiento del producto
    move_date = fields.Datetime(string='Fecha del movimiento', default=fields.Datetime.now)

    # este metodo debe ser heredado por cualquier modelo que herede el modelo Inventory.Move,
    # Lanza una excepción `NotImplementedError` si no se sobrescribe en los modelos hijos, indicando que se espera que
    # los modelos hijos proporcionen su propia implementación de este método.
    def get_quantity(self):
        raise NotImplementedError('El método get_quantity debe ser implementado por los modelos heredados.')
