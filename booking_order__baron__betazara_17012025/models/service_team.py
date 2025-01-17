# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class ServiceTeam(models.Model):
    _name = 'service.team'

    name = fields.Char(required=True, string=_('Team Name'))
    team_leader = fields.Many2one('res.users', required=True)
    team_members = fields.Many2many('res.users')