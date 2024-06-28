#importaciones
from odoo import models, fields, api
from odoo.exceptions import ValidationError

# es una clase que hereda models.model, lo que indica que se almacena en la bd
class Product(models.Model):

    _name = 'product'
    _description = 'Product'

    # es un campo que almacena el nombre del producto y es de tipo char
    name = fields.Char(string='Nombre del producto', required=True)
    # es un campo que almacena la cantidad del stock, y se calcula mediante el metodo _compute_quantity_on_hand
    quantity_on_hand = fields.Float(string='Cantidad en stock', compute='_compute_quantity_on_hand', store=True)
    # es un campo que almacena el valor total del inventario, se calcula mediante el metodo _compute_inventory_cost
    inventory_cost = fields.Float(string='Costo total del stock', compute='_compute_inventory_cost', store=True)
    # es un campo que almacena el precio de costo, es de tipo float
    cost_price = fields.Float(string='Precio de costo', required=True)
    # es un campo de tipo One2many que crea una relacion de uno a muchos con el modelo stock.in
    # reprensenta el moviento de entrada de los productos
    in_moves_ids = fields.One2many('stock.in', 'product_id', string='Movimientos de entrada')
    # es un campo de tipo One2many que crea una relacion de uno a muchos con el modelo stock.in
    # reprensenta el moviento de salida de los productos
    out_moves_ids = fields.One2many('stock.out', 'product_id', string='Movimientos de salida')

    #es una restricion de sql, que asegura que el nombre del producto sea unico
    _sql_constraints = [
        ('name_unique', 'unique(name)', 'El nombre del producto debe ser único.'),
    ]
    #@api.constrains es un decorador utilizado para definir métodos que implementan restricciones o validaciones a nivel de registro en un model
    @api.constrains('cost_price')
    # es un metodo que se asegura que el precio no sea menor o igual a 0
    def _check_cost_price(self):
        for record in self:
            if record.cost_price <= 0:
                raise ValidationError('El precio de costo debe ser mayor que cero.')

    # @api.depends es un decorador que permite definir los capos calculados depende de otros campos
    @api.depends('in_moves_ids.quantity', 'out_moves_ids.quantity')

    # es un metodo que permite saber la cantidad de stock se calcula sumando la cantidad de entrada y restando la de salida
    def _compute_quantity_on_hand(self):
        for record in self:
            record.quantity_on_hand = sum(record.in_moves_ids.mapped('quantity')) - sum(record.out_moves_ids.mapped('quantity'))

    @api.depends('quantity_on_hand', 'cost_price')
    # es un metodo que permite saber el costo del inventario, multiplicando la cantidad de stock con el precio de costo
    def _compute_inventory_cost(self):
        for record in self:
            record.inventory_cost = record.quantity_on_hand * record.cost_price


"""
  def create(self, vals):
        if vals.get('cost_price', 0) <= 0:
            raise ValidationError('El precio de costo debe ser mayor que cero.')
        return super(Product, self).create(vals)

    def write(self, vals):
        if 'cost_price' in vals and vals['cost_price'] <= 0:
            raise ValidationError('El precio de costo debe ser mayor que cero.')
        return super(Product, self).write(vals)

"""