from odoo import models, fields, api, _
import datetime

class WorkOrder(models.Model):
    _name = 'work.order'

    name = fields.Char('WO Number', default='/')
    booking_order_ref = fields.Many2one('sale.order')
    teams_id = fields.Many2one('service.team', string=_('Team'), required=True )
    team_leader = fields.Many2one('res.users', string=_('Team Leader'), required=True )
    team_members = fields.Many2many('res.users')
    planned_start = fields.Datetime(_('Planned Start'), required=True, )
    planned_end = fields.Datetime(_('Planned End'), required=True, )
    date_start = fields.Datetime(_('Date Start'), readonly=True, )
    date_end = fields.Datetime(_('Date End'), readonly=True, )
    state = fields.Selection([
            ('pending', 'Pending'),
            ('in_progress', 'In Progress'),
            ('done', 'Done'),
            ('cancel', 'Cancelled'),
        ], string='Status', default='pending')
    notes = fields.Text('Notes')
    
    def start_work(self):
        for rec in self:
            rec.write({
                'state': 'in_progress',
                'date_start': fields.Datetime.now()
            })
    
    def end_work(self):
        for rec in self:
            rec.write({
                'state': 'done',
                'date_end': fields.Datetime.now()
            })
    
    def reset_work(self):
        for rec in self:
            rec.write({
                'state': 'pending',
                'date_start': False
            })
            
    def cancel_work(self):
        for rec in self:
            rec.write({
                'state': 'cancel',
                'date_start': False,
                'date_end': False,
            })
            return {
                'type': 'ir.actions.act_window',
                'name': 'Reason for Cancellation',
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'work.order.cancel',
                'context': {'default_work_id': rec.id},
                'target': 'new'
            }
            
            
    @api.model
    def create(self, vals):
        if vals.get('name') == '/':
            vals['name'] = self.env['ir.sequence'].sudo().next_by_code('work.order.sequence')
        return super(WorkOrder, self).create(vals)