
from odoo import fields, models, api, _

class AccountJournal(models.Model):

    _inherit = "account.journal"

    l10n_py_dnit_pto_exp = fields.Integer('Punto de Expedicion', default = 1)
