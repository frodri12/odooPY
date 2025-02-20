from odoo import models, fields

class L10nPyCity(models.Model):

    _name = "l10n_py_city"
    _description = "Paraguay - Cities"

    code = fields.Integer()
    name = fields.Char()

    country_id = fields.Many2one("res.country")
    district_id = fields.Many2one("l10n_py_district")
