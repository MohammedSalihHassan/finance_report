from odoo import models, api

class FinanceTaxReport(models.AbstractModel):
    _name = 'report.finance_report.root_account_move_line_template'


    @api.model
    def _get_report_values(self, docids, data=None):
        domain = [('move_id.state','=', 'posted'),('product_id','!=', False)]
        start_date = data.get('form_data').get('start_date')
        if start_date:
            domain += [('date', '>', start_date)]
        end_date = data.get('form_data').get('end_date')
        if start_date:
            domain += [('date', '<', end_date)]
        move_type = data.get('form_data').get('move_type')
        if move_type == 'in_invoice':
            domain += [('move_id.move_type', '=', 'in_invoice')]
        if move_type == 'out_invoice':
            domain += [('move_id.move_type', '=', 'out_invoice')]
        if move_type == 'in_refund':
            domain += [('move_id.move_type', '=', 'in_refund')]
        if move_type == 'out_refund':
            domain += [('move_id.move_type', '=', 'out_refund')]
        if move_type == False:
            domain += []
        docs = self.env['account.move.line'].search(domain)
        return {
            'docs': docs
        }


class GeneralLedgerReport(models.AbstractModel):
    _name = 'report.finance_report.root_general_ledger_report_template'

    @api.model
    def _get_report_values(self, docids, data=None):
        domain = [('move_id.state','=', 'posted')]
        start_date = data.get('form_data').get('start_date')
        if start_date:
            domain += [('date', '>', start_date)]
        end_date = data.get('form_data').get('end_date')
        if start_date:
            domain += [('date', '<', end_date)]
        account_id = data.get('form_data').get('account_id')
        if account_id:
            domain += [('account_id', '=', account_id[0])]
        docs = self.env['account.move.line'].search(domain)
        return {
            'docs': docs,
            'start_date': start_date,
            'end_date': end_date,
            'account_id': account_id[1]
        }
