from odoo import models, fields, api, _
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    is_booking = fields.Boolean(default=True)
    teams_id = fields.Many2one('service.team', string=_('Team'))
    team_leader = fields.Many2one('res.users', string=_('Team Leader'))
    team_members = fields.Many2many('res.users', string=_('Team Members'))
    booking_start = fields.Datetime('Booking Start')
    booking_end = fields.Datetime('Booking End')
    working_count = fields.Integer(compute='_compute_working_order')
    
    
    @api.depends('working_count')
    def _compute_working_order(self):
        for rec in self:
            wo_ids = self.env['work.order'].search([('booking_order_ref', '=', self.id)])
            if wo_ids:
                rec.working_count = len(wo_ids)
            else:
                rec.working_count = 0
    
    def open_working_order(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Work Order',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'work.order',
            'domain': [('booking_order_ref', '=', self.id)],
            'context': dict(self.env.context),
        }

    
    @api.onchange('teams_id')
    def _onchange_team_id(self):
        if self.teams_id:
            self.team_leader = self.teams_id.team_leader
            self.team_members = self.teams_id.team_members
        else:
            self.team_leader = False
            self.team_members = [(5, 0, 0)]
            
            
    def button_check(self):
        for rec in self:
            overlapping_work_orders = self.env['work.order'].search([
                ('state', '!=', 'cancelled'),  # Tidak dalam status cancelled
                ('teams_id', '=', rec.teams_id.id),  # Team yang sama
                ('planned_start', '<=', rec.booking_end),
                ('planned_end', '>=', rec.booking_start),
                ('planned_start', '<=', rec.booking_start),
            ])
            
            if overlapping_work_orders:
                raise UserError(_('Team already has work order during that period on %s') % overlapping_work_orders.name)
            else:
                raise UserError('Team is Available for booking')
        
    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        
        for rec in self:
            overlapping_work_orders = self.env['work.order'].search([
                ('state', '!=', 'cancelled'),  # Tidak dalam status cancelled
                ('teams_id', '=', rec.teams_id.id),  # Team yang sama
                ('planned_start', '<=', rec.booking_end),
                ('planned_end', '>=', rec.booking_start),
                ('planned_start', '<=', rec.booking_start),
            ])
            
            if overlapping_work_orders:
                raise UserError(_('Team already has work order during that period on %s') % overlapping_work_orders.name)
            else:
                wo_obj = self.env['work.order'].create({
                    'name': self.env['ir.sequence'].sudo().next_by_code('work.order.sequence'),
                    'teams_id': self.teams_id.id,
                    'state': 'pending',
                    'team_leader': self.team_leader.id,
                    'team_members': [(6, 0, self.team_members.ids)],
                    'planned_start': self.booking_start,
                    'planned_end': self.booking_end,
                    'date_start': self.booking_start,
                    'date_end': self.booking_end,
                    'booking_order_ref': self.id
                    
                })
        
        return res
    