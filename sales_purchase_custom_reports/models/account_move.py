from odoo import models, fields, api
from num2words import num2words

class AccountMoveInherit(models.Model):
    _inherit = 'account.move'

    total_amount_word = fields.Char(string="Total Amount", compute='get_total_in_words')
    total_amount_arabic_word = fields.Char(string="Arabic Amount", compute='compute_amount_arabic_word')

    @api.depends('amount_total')
    def get_total_in_words(self):
        for rec in self:
            rec.total_amount_word = str(rec.currency_id.amount_to_text(rec.amount_total)) + str(' ')

    @api.depends('amount_total', 'invoice_line_ids')
    def compute_amount_arabic_word(self):
        self.total_amount_arabic_word = ''
        amount = round(self.amount_total, 4)
        text = self.currency_id.amount_to_text(amount)
        integer = int(amount)
        decimal = round((amount - integer), 2) * 100
        riyal = num2words(integer, lang='ar')
        halala = num2words(decimal, lang='ar')
        text_ar = riyal
        text_ar += " " + str(self.currency_id.currency_unit_arabic)
        if decimal:
            text_ar += ' و'
            text_ar += halala
            text_ar += " " + str(self.currency_id.currency_subunit_arabic)

        if 3000 <= self.amount_total < 11000 and "ألف" in text_ar:
            text_ar_value = text_ar.replace("ألف", " ألاف ")
            for rec in self:
                rec.total_amount_arabic_word = text_ar_value
        else:
            for rec in self:
                rec.total_amount_arabic_word = text_ar

    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        res = super(AccountMoveInherit, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar,
                                                              submenu=submenu)
        remove_report_id = self.env.ref('sales_purchase_custom_reports.account_move_custom_report').id
        if view_type == 'form' and self.env.context.get('default_move_type') != 'out_invoice':
            if remove_report_id and toolbar and res['toolbar'] and res['toolbar'].get('print'):
                remove_report_record = [rec for rec in res['toolbar'].get('print') if rec.get('id') == remove_report_id]
                if remove_report_record and remove_report_record[0]:
                    res['toolbar'].get('print').remove(remove_report_record[0])
        return res


class ResPartnerInherits(models.Model):
    _inherit = 'res.partner'

    arabic_name = fields.Char("Arabic Name")
    arabic_street = fields.Char()
    arabic_street2 = fields.Char()
    arabic_city = fields.Char()

class ResCurrencyInherit(models.Model):
    _inherit = 'res.currency'

    currency_unit_arabic = fields.Char(string="Arabic Currency Unit")
    currency_subunit_arabic = fields.Char(string="Arabic Currency Subunit")
