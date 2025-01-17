from odoo import fields, models, api, _
from odoo.exceptions import UserError

class WorkOrderCancel(models.TransientModel):

    _name = 'work.order.cancel'

    work_id = fields.Many2one('work.order')
    notes = fields.Text('Notes')
    
    def action_confirm(self):
        for rec in self:
            rec.work_id.write({
                'notes': rec.notes
            })
