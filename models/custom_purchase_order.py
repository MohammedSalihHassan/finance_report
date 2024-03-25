from odoo import models, fields, api, _
from datetime import datetime


class CustoPurchaseOrder(models.Model):

    _name = 'purchase.order'
    _inherit = 'purchase.order'

    vendor_quote_ref = fields.Char('Vendor Quote Ref')
    vendor_quote_date = fields.Date('Vendor Quote Date')
    project = fields.Char('Project')

    payment_method = fields.Char('Payment Method', )
    discount = fields.Float('Discount')
    total_with_discount = fields.Float('Total with discount', compute='_total_discount', readonly=True)

    def _total_discount(self):
        for record in self:
            if record.discount:
                record.total_with_discount = record.amount_untaxed - record.discount
            else:
                record.total_with_discount = record.amount_untaxed

