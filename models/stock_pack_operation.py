from openerp import models,api
 
class stock_pack_operation_delivery_labels(models.Model):
    _inherit = ['stock.pack.operation']

    def print_label(self, cr, uid, ids, context=None):
        return self.pool['report'].get_action(cr, uid, ids, 'deliveries_labels.report_deliverieslabels_stock_pack_operation', context=context)