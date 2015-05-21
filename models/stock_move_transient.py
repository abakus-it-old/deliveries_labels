from openerp.osv import fields, osv

class stock_move_transient(osv.osv_memory):
    _name = "stock.move.transient"
    _description = "Scrap Moves"

    _columns = {
        'product_id': fields.many2one('product.product', 'Product'),
        'product_qty': fields.float('Quantity'),
        'date': fields.datetime('Date'),
        'picking_id': fields.many2one('stock.picking', 'Reference'),
    }

    def print_labels_from_stock_move_with_custom_qty(self, cr, uid, stock_move_id, qty, context=None):
        stock_move_obj = self.pool.get('stock.move')
        stock_move_transient_obj = self.pool.get('stock.move.transient')
        
        stock_move = stock_move_obj.browse(cr, uid, int(stock_move_id))
        stock_move_transient = stock_move_transient_obj.create(cr, uid, {   'picking_id': stock_move.picking_id.id,
                                                                            'date': stock_move.date,
                                                                            'product_id': stock_move.product_id.id,
                                                                            'product_qty': int(qty),
                                                                        })
        
        return self.pool['report'].get_action(cr, uid, stock_move_transient, 'deliveries_labels.report_deliverieslabels_stock_move_transient', context=context)