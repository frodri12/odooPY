#
from odoo import api, fields, models, tools, SUPERUSER_ID, _

class Users(models.Model):

    _inherit = 'res.users'

    @api.model
    def default_get(self,fields_list):
        #res = super(ResPartner, self).default_get(fields)
        res = super().default_get(fields_list)
        res.update({'lang':self.env.lang})
        return res
