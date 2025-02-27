# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _, Command, SUPERUSER_ID

import logging

_logger = logging.getLogger(__name__)

class Company(models.Model):

    _inherit = "res.company"

    l10n_py_streetnmbr = fields.Char(
        "NumberHouse", compute='_compute_address', inverse='_inverse_streetnmbr')
    l10n_py_district_id = fields.Many2one(
        "l10n_py_district", compute='_compute_address', inverse='_inverse_district')
    l10n_py_city_id = fields.Many2one(
        "l10n_py_city", compute='_compute_address', inverse='_inverse_cityId')

    l10n_py_set_responsibility_type_id = fields.Many2one(
        domain="[('code', 'in', [1, 2, 3, 4])]", 
        related='partner_id.l10n_py_set_responsibility_type_id', readonly=False)

    l10n_py_regulation_type = fields.Selection([
        ('0','Sin Definir'),('1','Régimen de Turismo'),
        ('2','Importador'),('3','Exportador'),
        ('4','Maquila'),('5','Ley N° 60/90'),
        ('6','Régimen del Pequeño Productor'),
        ('7','Régimen del Mediano Productor'),
        ('8','Régimen Contable')
    ], default = '0', string = "Tipo de Régimen")

    l10n_py_affectation_type = fields.Selection([
        ('1','Gravado IVA'),
        ('2','Exonerado (Art.83 - 125)'),
        ('3','Exento'),
        ('4','Gravado parcial')
    ], default = '1', string = 'Tipo de Afectacion')
    
    l10n_py_establecimiento = fields.Integer("Establecimiento", default = 1)
    
    def _get_company_address_field_names(self):
        """ Return a list of fields coming from the address partner to match
        on company address fields. Fields are labeled same on both models. """
        return [
            'street', 'l10n_py_streetnmbr', 'street2', 
            'city', 'zip', 'state_id', 'l10n_py_district_id', 
            'l10n_py_city_id', 'country_id']

    def _inverse_streetnmbr(self):
        for company in self:
            company.partner_id.l10n_py_streetnmbr = company.l10n_py_streetnmbr

    def _inverse_district(self):
        for company in self:
            company.partner_id.l10n_py_district_id = company.l10n_py_district_id

    def _inverse_cityId(self):
        for company in self:
            company.partner_id.l10n_py_city_id = company.l10n_py_city_id
