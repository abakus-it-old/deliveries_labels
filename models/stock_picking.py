from openerp import models,api
 
class stock_delivery_labels(models.Model):
    _inherit = ['stock.picking']

    def print_labels(self, cr, uid, ids, context=None):
        #report name: stock.report_deliverieslabels
        return self.pool['report'].get_action(cr, uid, ids, 'deliveries_labels.report_deliverieslabels_stock', context=context)