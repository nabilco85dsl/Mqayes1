""" Initialize Res Users """

from dateutil.relativedelta import relativedelta

from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError, Warning


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    arabic_name = fields.Char(string='Arabic Name')

class ResPartner(models.Model):
    _inherit = 'res.partner'
    arabic_name = fields.Char(string='Arabic Name')

class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    arabic_name = fields.Char(string='Arabic Name')

