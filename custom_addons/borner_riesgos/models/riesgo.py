from odoo import models, fields
import random

class BornerRiesgo(models.Model):
    _name = 'borner.riesgo'
    _description = 'Registro de Riesgos Financieros'

    fecha = fields.Date(required=True)
    proveedor_id = fields.Many2one('res.partner', string='Proveedor', required=True)
    concepto = fields.Char(required=True)
    monto = fields.Float(required=True)
    estado = fields.Selection([
        ('borrador', 'Borrador'),
        ('revision', 'En revisión'),
        ('aprobado', 'Aprobado'),
    ], default='borrador', required=True)
    riesgo = fields.Integer(string='Riesgo (%)')

    def action_evaluar_riesgo(self):
        for record in self:
            record.riesgo = random.randint(0, 100)
            record.estado = 'revision'
