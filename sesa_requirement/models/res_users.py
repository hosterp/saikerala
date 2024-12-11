from openerp import models, fields

class ResUsers(models.Model):
    _inherit = 'res.users'  # Inherit the res.users model

    district_id = fields.Many2one('event.district', string="District")
