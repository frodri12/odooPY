
from odoo import models, fields

class L10nLatamIdentificationType(models.Model):

    _inherit = "l10n_latam.identification.type"

    l10n_py_dnit_code = fields.Char("DNIT Code")