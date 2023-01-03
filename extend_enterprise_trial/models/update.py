import logging

from odoo.models import AbstractModel

_logger = logging.getLogger(__name__)


class PublisherWarrantyContract(AbstractModel):
    _inherit = "publisher_warranty.contract"

    def update_notification(self, cron_mode=True):
        """
        Send a message to Odoo's publisher warranty server to check the
        validity of the contracts, get notifications, etc...

        @param cron_mode: If true, catch all exceptions (appropriate for usage in a cron).
        @type cron_mode: boolean
        """
        if not self.env['ir.config_parameter'].sudo().get_param(
                'database.expiration_date'):
            super(PublisherWarrantyContract, self).update_notification(
                cron_mode=cron_mode)
        else:
            if self.env['ir.config_parameter'].sudo().get_param(
                    'database.expiration_reason') == 'trial':
                return True
            else:
                super(PublisherWarrantyContract, self).update_notification(
                    cron_mode=cron_mode)
