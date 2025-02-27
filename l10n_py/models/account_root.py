
from odoo import api, fields, models

class AccountRoot(models.Model):

    _inherit = "account.root"

    @api.model
    def _from_account_code(self, code):
        return self.browse(code and code[:1])
        #return self.browse((code and code[:1]) or (code and code[:3]))
        
