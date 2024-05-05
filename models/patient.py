# -*- coding: utf-8 -*-
from odoo import api, fields, models


class PharmacyPatient(models.Model):
    _name = "pharmacy.patient"
    _inherit=['mail.thread','mail.activity.mixin']
    _description = "Pharmacy Patient"

    name = fields.Char(string='Name',tracking=True)
    ref= fields.Char(string='Reference',tracking=True)
    age = fields.Char(string='Age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    address = fields.Text(string='Address',tracking=True)
    allergies = fields.Text(string='Allergies')
    contact_info = fields.Char(string='Contact Information',tracking=True)