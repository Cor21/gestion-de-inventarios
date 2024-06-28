# importaciones
from odoo.tests.common import TransactionCase
from odoo.exceptions import UserError

# clase que es para realizar test del módulo


class TestInventory(TransactionCase):

    # Este método se ejecuta antes de cada prueba para configurar el entorno de prueba
    def setUp(self):
        super().setUp()
        self.Product = self.env['product']
        self.StockIn = self.env['stock.in']
        self.StockOut = self.env['stock.out']

    def test_product_creation_with_invalid_cost_price(self):
        # Caso de prueba para crear un producto con un precio de costo inválido
        # (menor o igual a 0), se espera que lance un error de usuario.
        with self.assertRaises(UserError, msg="Debe indicarse un precio de costo mayor a 0."):
            self.Product.create({
                'name': 'Monitor 24 pulgadas',
                'cost_price': 0,
            })

    def test_inventory_moves(self):
        # Caso de prueba para validar los movimientos de inventario
        # afectan la cantidad en stock y el costo de inventario.
        product_vals = {
            'name': 'Monitor 24 pulgadas',
            'cost_price': 2,
        }
        product = self.Product.create(product_vals)

        # Crear movimiento de entrada
        stock_in_vals = {
            'product_id': product.id,
            'quantity': 5,
        }
        stock_in = self.StockIn.create(stock_in_vals)

        # Crear movimiento de salida
        stock_out_vals = {
            'product_id': product.id,
            'quantity': 2,
        }
        stock_out = self.StockOut.create(stock_out_vals)

        # Verificar la cantidad en stock y el costo de inventario después de los movimientos
        product.refresh()  # Actualizar el producto para obtener los valores actualizados
        self.assertEqual(product.quantity_on_hand, 3, "Cálculo incorrecto de la cantidad en stock")