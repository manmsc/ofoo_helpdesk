from datetime import datetime, timedelta

from odoo import fields, models, _, api
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT


class IrConfigParameter(models.Model):
    _inherit = 'ir.config_parameter'

    @api.model
    def extend_trial_period(self, ex_date):
        expiration_date_str = self.sudo().get_param(
            'database.expiration_date',
            fields.Date.today().strftime(DEFAULT_SERVER_DATETIME_FORMAT))
        expiration_date = datetime.strptime(expiration_date_str, DEFAULT_SERVER_DATETIME_FORMAT)

        trial_days = int(self.env['ir.config_parameter'].sudo().get_param(
            'database.extend_enterprise_trial', ex_date))

        new_expiration_date = str(expiration_date + timedelta(days=trial_days))
        self.sudo().set_param('database.expiration_date', new_expiration_date)
        return True
