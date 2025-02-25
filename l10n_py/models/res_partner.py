# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models, tools, SUPERUSER_ID, _, Command
import logging
import re

from odoo.exceptions import ValidationError

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
        ' type of operations and requirements they need.',
    )

    l10n_latam_identification_type_id = fields.Many2one('l10n_latam.identification.type',
        string="Identification Type", index='btree_not_null', auto_join=True,
        default=lambda self: self.env.ref('l10n_py.it_ruc', raise_if_not_found=False),
        help="The type of identification")

    @api.model
    def default_get(self,fields_list):
        #res = super(ResPartner, self).default_get(fields)
        res = super().default_get(fields_list)
        res.update(
            {'country_id':self.env['res.country'].search([('code', '=', 'PY')], limit=1).id}
        )
        res.update({'lang':self.env.lang})
        return res

    @api.onchange('country_id','l10n_py_city_id')
    def _onChange_City(self):
        if self.country_id.code == 'PY' and self.l10n_py_city_id.country_id.code == 'PY' :
            self.write({'city': self.l10n_py_city_id.name,})

    @api.constrains('vat', 'l10n_latam_identification_type_id')
    def check_vat(self):
        if self.env.context.get('no_vat_validation'):
            return
        if not self.vat:
            return
        #with_vat = self.filtered(lambda x: x.l10n_latam_identification_type_id.is_vat)
        if self.commercial_partner_id.country_id.code == 'PY' and self.l10n_latam_identification_type_id.name == 'RUC':
            ## Validar
            if re.findall("^[0-9]{5,8}-[0-9]$", self.vat).__len__() == 0:
                raise ValidationError("El formato del RUC es incorrecto [XXXXX-X, XXXXXX-X, XXXXXXX-X o XXXXXXXX-X]")


