from odoo import models, fields, api, _

class ResCompany(models.Model):
    _name = "res.company"
    _inherit = "res.company"


    a_c_name = fields.Char('A/C Name')
    bank = fields.Char('Bank')
    account_number = fields.Char('Account Number')
    iban = fields.Char('IBAN')
    swift_code = fields.Char('SWIFT Code')