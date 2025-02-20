
from odoo import models, fields

class L10nPyDistrict(models.Model):

    _name = "l10n_py_district"
    _description = "Paraguay - Districts"

    code = fields.Integer()
    name = fields.Char()

    country_id = fields.Many2one("res.country")
    state_id = fields.Many2one("res.country.state")
