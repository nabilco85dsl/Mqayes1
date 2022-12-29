from odoo import models, fields, api

class ResCompanyInherit(models.Model):
    _inherit = 'res.company'

    arabic_name = fields.Char(string="إسم الشركة")

    arabic_street = fields.Char()
    arabic_street2 = fields.Char()
    arabic_city = fields.Char()
    bo_box = fields.Char(string="PO.Box")



class ResBankInherit(models.Model):
    _inherit = 'res.bank'

    arabic_name = fields.Char(string="Arabic Name")




