# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models, tools, SUPERUSER_ID, _, Command
import logging

_logger = logging.getLogger(__name__)

ADDRESS_FIELDS = (
    'street', 'l10n_py_streetnmbr', 'street2', 
    'zip', 'city', 'state_id', 'l10n_py_district_id', 
    'l10n_py_city_id', 'country_id')

class ResPartner(models.Model):

    _inherit = 'res.partner'

    l10n_py_streetnmbr = fields.Char("NumberHouse")
    l10n_py_district_id = fields.Many2one("l10n_py_district")
    l10n_py_city_id = fields.Many2one("l10n_py_city")

    l10n_py_set_responsibility_type_id = fields.Many2one(
        'l10n_py.set.responsibility.type', string='SET Responsibility Type', index='btree_not_null', help='Defined by SET to'
        ' identify the type of responsibilities that a person or a legal entity could have and that impacts in the'
        ' type of operations and requirements they need.')

    @api.model
    def default_get(self,fields_list):
        #res = super(ResPartner, self).default_get(fields)
        res = super().default_get(fields_list)
        res.update(
            {'country_id':self.env['res.country'].search([('code', '=', 'PY')], limit=1).id}
        )
        return res

    @api.onchange('country_id','l10n_py_city_id')
    def _onChange_City(self):
        if self.country_id.code == 'PY' and self.l10n_py_city_id.country_id.code == 'PY' :
            self.write({'city': self.l10n_py_city_id.name,})

