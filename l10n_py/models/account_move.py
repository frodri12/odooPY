

from odoo import models, fields, api, _

import logging
_logger = logging.getLogger(__name__)

class AccountMove(models.Model):

    _inherit = 'account.move'

    def _get_formatted_sequence(self, number=0):
        return "%s %03d-%03d-%07d" % (self.l10n_latam_document_type_id.doc_code_prefix,
                                 self.company_id.l10n_py_establecimiento,
                                 self.journal_id.l10n_py_dnit_pto_exp, number)

    def _get_starting_sequence(self):
        """ If use documents then will create a new starting sequence using the document type code prefix and the
        journal document number with a 8 padding number """
        if self.journal_id.l10n_latam_use_documents and self.company_id.account_fiscal_country_id.code == "PY":
            if self.l10n_latam_document_type_id:
                return self._get_formatted_sequence()
        return super()._get_starting_sequence()
