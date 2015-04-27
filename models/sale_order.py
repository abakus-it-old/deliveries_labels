from openerp import models,api

class sale_delivery_labels(models.Model):
    _inherit = ['sale.order']

    def print_labels(self, cr, uid, ids, context=None):
        #report name: sale.report_deliverieslabels
        return self.pool['report'].get_action(cr, uid, ids, 'deliveries_labels.report_deliverieslabels_sale', context=context)