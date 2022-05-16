from odoo import models, fields, api



class LP_Department(models.Model):
    _inherit = ['hr.department']

    lp_type = fields.Selection([('director', 'Director'),
                                ('it_office', 'Office'),
                                ('department', 'Department'),
                                ('section', 'Section')],
                               'Type', default="section")

    lp_category = fields.Selection([('delivery', 'Delivery'),
                                ('operations', 'Operations'),
                                ('process_management', 'Process Management'),
                                ('quality_and_support', 'Quality & Support'),
                                ('sales_and_marketing','Sales & Marketing'),
                                ('accounting','Accounting')],
                               'Category')

    lp_analytic_account_group = fields.Many2one('account.analytic.group', string='Analytical Account Group')