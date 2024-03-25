from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

from datetime import datetime, timedelta

class GeneralLedgerWizard(models.TransientModel):

    _name = "general.ledger.wizard"
    _description = "General Ledger report"


    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)
    account_id = fields.Many2one('account.account', string="Acount", required=True)


    @api.constrains('start_date', 'end_date')
    def _check_date(self):
        if self.start_date > self.end_date:
            raise UserError('Constraint Error: The end date < start date ! ')

    def report_print(self):
        data ={
            'form_data':self.read()[0],
        }
        return self.env.ref("finance_report.action_report_finance_general_ledger"
            ).report_action(self, data=data)