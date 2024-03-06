from datetime import timedelta

from odoo import api, fields, models, _
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)


class chargementFournisseur(models.Model):
    _inherit = "res.partner"

    def synchronisation_function(self):
        suppliers = self.env['res.partner'].search([("supplier_rank", ">", 0])

                                                    for supplier in suppliers
        return {
            'warning': {'title': "Warning", 'message': "Mise-a-jour de la liste de fournisseurs",
                        'type': 'notification'},
        }

        # res = super().create(vals)

        # {'search_default_supplier': 1,'res_partner_search_mode': 'supplier', 'default_is_company': True, 'default_supplier_rank': 1}
        # [["supplier_rank",">",0]]

        # return res


