from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ProjectProject(models.Model):
    _inherit = "project.project"


    def write(self, vals):

        if 'stage_id' in vals.keys() and vals['stage_id'] == 3:
            for elem in self.task_ids:
                # if ('انهاء' not in elem.stage_id.name) or ('إنهاء' not in elem.stage_id.name) or ('انتهاء' not in elem.stage_id.name) or ('إنتهاء' not in elem.stage_id.name) or ('الالغاء' not in elem.stage_id.name) or ('الإلغاء' not in elem.stage_id.name) or ('منتهي' not in elem.stage_id.name):
                if elem.stage_id.sequence not in (9, 10):
                    raise ValidationError("يوجد مهام لم يتم انهائها أو الغائها")

        return super(ProjectProject, self).write(vals)