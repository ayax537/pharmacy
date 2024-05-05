from odoo import models, fields

class MedicationDispensing(models.Model):
    _name = 'pharmacy_management.medication.dispensing'
    _inherit=['mail.thread','mail.activity.mixin']
    _description = 'Medication Dispensing'

    patient_id = fields.Many2one('res.partner', string='Patient', required=True, domain="[('is_company', '=', False)]",tracking=True)
    dispensing_date = fields.Date(string='Dispensing Date')
    dispensed_medication = fields.Char(string='Dispensed Medication')
    quantity = fields.Float(string='Quantity')
    pharmacy = fields.Many2one('res.partner', string='Pharmacy', domain="[('is_company', '=', True)]")