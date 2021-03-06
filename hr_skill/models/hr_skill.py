# Copyright 2013 Savoir-faire Linux
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import api, fields, models


class Skill(models.Model):
    _name = 'hr.skill'
    _parent_store = True
    _order = 'parent_left'

    name = fields.Char(string='Name', required=True, translate=True)
    active = fields.Boolean(string='Active', default=True)
    parent_id = fields.Many2one(comodel_name='hr.skill',
                                string='Parent',
                                ondelete='cascade')
    parent_left = fields.Integer(string='Parent Left', index=True)
    parent_right = fields.Integer(string='Parent Right', index=True)
    child_ids = fields.One2many(comodel_name='hr.skill',
                                inverse_name='parent_id',
                                string='Children')
    employee_ids = fields.Many2many(
        comodel_name='hr.employee',
        relation='skill_employee_rel',
        column1='skill_id',
        column2='employee_id',
        string='Employee(s)')

    @api.multi
    def name_get(self):
        res = []
        for skill in self:
            names = []
            current = skill
            while current:
                names.append(current.name)
                current = current.parent_id
            res.append((skill.id, ' / '.join(reversed(names))))
        return res
