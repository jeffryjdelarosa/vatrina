# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.exceptions import UserError, ValidationError

class paid(models.Model):
    _inherit = 'account.move'

    paid = fields.Float(string="paid amount", store=True,  required=False, compute='compute_paid' )
    is_bigger = fields.Boolean(string="",)
    pass_bigger = fields.Boolean(string="البيع بالسالب",)

    @api.depends('amount_total','amount_residual')
    def compute_paid(self):
        for rec in self:
            if rec.amount_total > rec.amount_residual:
                rec.paid = rec.amount_total - rec.amount_residual
            else:
                rec.paid = 0.0
            pass

    def action_post(self):
        res = super(paid, self).action_post()
        print('innnnnnnnnnnnnnn111111111111')
        strWarning = _(
            "لايمكن بيع كمية اكبر من الموجودة بالمخزن")
        if self.invoice_line_ids:
            if not self.pass_bigger:
                for rec in self.invoice_line_ids:
                    if rec.quantity > rec.product_id.qty_available:
                        print('innnnnnnnnnnnnnn')
                        raise UserError(strWarning)
        else:
            return res

    @api.onchange('invoice_line_ids')
    def _onchange_bigger(self):
        if self.invoice_line_ids:
            for rec in self.invoice_line_ids:
                if rec.quantity > rec.product_id.qty_available:
                    self.is_bigger = True
        pass