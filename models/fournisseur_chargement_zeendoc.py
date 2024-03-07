from datetime import timedelta

from odoo import api, fields, models, _
from odoo.exceptions import UserError
import logging
import requests

_logger = logging.getLogger(__name__)


# class chargementFournisseur(models.Model):
class fournisseur_chargement_zeendoc(models.Model):
    _inherit = "res.partner"

    def synchronisation_function(self):
        # suppliers = self.env['res.partner'].search([("supplier_rank",">",0)])

        # for supplier in suppliers
        # ValidationError(_('voulez-vous vraiment ?'))
        url = "https://geo.api.gouv.fr/communes?"
        params = {
            'codePostal': '78000'
        }
        reponse = requests.get(url, params=params)
        message = "Mise-a-jour avec succes : " + str(reponse.json())
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'message': message,
                'type': 'success',
                'sticky': False,
            }
        }

        # res = super().create(vals)

        # {'search_default_supplier': 1,'res_partner_search_mode': 'supplier', 'default_is_company': True, 'default_supplier_rank': 1}
        # [["supplier_rank",">",0]]

        # return res


