
from odoo import fields, models, api, _

class AccountJournal(models.Model):

    _inherit = "account.journal"

    l10n_py_dnit_pto_exp = fields.Integer('Punto de Expedicion', default = 1)

    @api.onchange('l10n_py_dnit_pto_exp', 'type')
    def _onchange_set_short_name(self):
        """ Will define the AFIP POS Address field domain taking into account the company configured in the journal
        The short code of the journal only admit 5 characters, so depending on the size of the pos_number (also max 5)
        we add or not a prefix to identify sales journal.
        """
        if self.type == 'sale' and self.l10n_py_dnit_pto_exp:
            self.code = "%03i" % self.l10n_py_dnit_pto_exp
