
from odoo import models, api, fields, _
from odoo.exceptions import UserError

class L10nLatamDocumentType(models.Model):

    _inherit = 'l10n_latam.document.type'

    def _format_document_number(self, document_number):
        """ Make validation of Import Dispatch Number
          * making validations on the document_number. If it is wrong it should raise an exception
          * format the document_number against a pattern and return it
        """
        self.ensure_one()
        if self.country_id.code != "PY":
            return super()._format_document_number(document_number)

        if not document_number:
            return False

        if not self.code:
            return document_number

        # Invoice Number Validator (For Eg: 123-123-1234)
        failed = False
        args = document_number.split('-')
        if len(args) != 3:
            failed = True
        else:
            exp, pos, number = args
            if len(exp) > 3 or not exp.isdigit():
                failed = True
            elif len(pos) > 3 or not pos.isdigit():
                failed = True
            elif len(number) > 7 or not number.isdigit():
                failed = True
            document_number = '{:>03s}-{:>03s}-{:>07s}'.format(exp, pos, number)
        if failed:
            raise UserError(
                _(
                    "%(value)s is not a valid value for %(field)s.\nThe document number must be entered with a dash (-) and a maximum of 5 characters for the first part and 8 for the second. The following are examples of valid numbers:\n* 1-1\n* 0001-00000001\n* 00001-00000001",
                    value=document_number,
                    field=self.name,
                ),
            )

        return document_number
