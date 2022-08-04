from odoo import api, fields, models


class HelpdeskTicket(models.Model):
	_inherit = "helpdesk.ticket"

	issue_type = fields.Selection([
		('database', "Database Issue"),
		('email', "Email Issue"),
		('website', "Website Issue")
	], string="Issue Type")

	type_name = fields.Char(string="Type Name", compute="_compute_ticket_type_name")

	@api.depends('ticket_type_id')
	def _compute_ticket_type_name(self):
		for rec in self:
			rec.type_name = rec.ticket_type_id.name

	def _message_post_after_hook(self, message, msg_vals):
		res = super(HelpdeskTicket, self)._message_post_after_hook(message, msg_vals)

		# this function is for automation of changing helpdesk ticket stage to customer reply when customer replied ticket.
		# to trigger automation, some requirements are needed:
		# 1. message_type is comment
		# 2. message subtype is discussion
		# 3. author must be same as customer in ticket
		# 4. the current stage is not a new stage

		author_id = msg_vals['author_id']
		message_type = msg_vals['message_type']
		subtype_id = msg_vals['subtype_id']
		customer_id = self.partner_id
		stage_id = self.stage_id

		if author_id:
			if message_type == 'comment' and subtype_id == 1 and author_id == customer_id.id and stage_id.id != 1:
				self.env['helpdesk.ticket'].search(
					[('id', '=', self.id)]).write({'stage_id': 6})
		else:
			pass

		return res



