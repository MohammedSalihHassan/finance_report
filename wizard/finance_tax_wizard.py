from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

from datetime import datetime, timedelta

class FinanceTaxWizard(models.TransientModel):

    _name = "finance.tax.wizard"
    _description = "Taxes report"


    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)
    move_type = fields.Selection([
        ('in_invoice','Vendor Bill'),
        ('out_invoice','Customer Invoice'),
        ('in_refund', 'Vendor Credit Note'),
        ('out_refund', 'Customer Credit Note')
        ])

    @api.constrains('start_date', 'end_date')
    def _check_date(self):
        if self.start_date > self.end_date:
            raise UserError('Constraint Error: The end date < start date ! ')

    def report_print(self):
        data ={
            'form_data':self.read()[0],
        }
        return self.env.ref("finance_report.action_report_finance_tax"
            ).with_context(landscap=True).report_action(self, data=data)
