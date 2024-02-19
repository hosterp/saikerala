from openerp import fields, models, api


class Event(models.Model):
    _name = 'event.event'
    _rec_name = 'user'

    # @api.model
    #    def default_get(self,field_list):
    #        res = super(Event,self).default_get(field_list)
    #        print "sssssssssssssssssssssssssssssssss",event_place
    #        res.update({'event_place':})
    #        return res

    @api.multi
    def action_completed(self):
        self.state = 'completed'

    @api.multi
    def action_cancel(self):
        self.state = 'cancel'

    # event = fields.Char("Event")
    desc = fields.Text("Details")
    date = fields.Datetime("Date of event")
    # event_place = fields.Char("Place")
    state = fields.Selection([('draft', 'Draft'), ('completed', 'Completed'), ('cancel', 'Cancelled')], default='draft',
                             string="Status")
    user = fields.Many2one('hr.employee')
    reporting_incharge = fields.Many2one('hr.employee',string="Reporting In-Charge")
    event_place = fields.Many2one('event.place', "Place")
    # event_district = fields.Many2one('event.district',"District")
    event_district = fields.Selection([('AL', 'ALAPPUZHA'),
                                       ('ER', 'ERNAKULAM'),
                                       ('ID', 'IDUKKI'),
                                       ('KN', 'KANNUR'),
                                       ('KS', 'KASARAGOD'),
                                       ('KL', 'KOLLAM'),
                                       ('KT', 'KOTTAYAM'),
                                       ('KZ', 'KOZHIKODE'),
                                       ('MA', 'MALAPPURAM'),
                                       ('PL', 'PALAKKAD'),
                                       ('PT', 'PATHANAMTHITTA'),
                                       ('TV', 'THIRUVANANTHAPURAM'),
                                       ('TS', 'THRISSUR'),
                                       ('WA', 'WAYANAD')])
    event_category = fields.Many2one('event.category', "Event Category")
    event_type = fields.Many2one('event.type')
    total_attendees = fields.Integer("Total Attendees")
    total_devotees_attended = fields.Integer("Total devotees attended")
    advance = fields.Integer("Advance")
    expense = fields.Integer("Expense")
    balance = fields.Integer("Balance")
    rem_expense = fields.Text("Remark")
    remark = fields.Text("Remark")
    attachment = fields.Many2many('ir.attachment', 'attach_rel', 'doc_id', 'attach_id3',
                                  string="Attachment",
                                  help='You can attach the copy of your document', copy=False)
    contact_details=fields.Char()
    revived_samithi=fields.Boolean(string="Revived Samithi")
    time = fields.Float(string="Time")



    @api.onchange('event_district')
    def onchange_event_district(self):
        for record in self:
            if record.event_district:
                return {'domain':{'event_place':[('event_district','=',record.event_district)]}}

    @api.onchange('event_category')
    def onchange_event_category(self):
        for record in self:
            if record.event_category:
                return {'domain':{'event_type':[('event_category','=',record.event_category.event_category)]}}


class Attachment(models.Model):
    _inherit = 'ir.attachment'

    attach_rel = fields.Many2many('res.partner', 'attachment', 'attachment_id3', 'document_id', string="Attachment",
                                  invisible=1)


class EventCategory(models.Model):
    _name = 'event.category'
    _rec_name = 'event_category'

    event_category = fields.Char('Event Category')


class EventType(models.Model):
    _name = 'event.type'
    _rec_name = 'event_type'

    event_type = fields.Char("Event Type")
    event_category = fields.Many2one('event.category')


class EventExpenses(models.Model):
    _name = 'event.expense'

    event = fields.Many2one('event.event')
    advance = fields.Integer("Advance")
    expense = fields.Integer("Expense")
    balance = fields.Integer("Balance")
    rem_expense = fields.Text("Remark")
    state = fields.Selection([('draft', 'Draft'), ('paid', 'Paid')], default='draft',
                             string="Status")
    event_category = fields.Many2one('event.category', "Event Category")
    event_type = fields.Many2one('event.type')

# class Activity(models.Model):
#     _name = 'activity.activity'

#     user = fields.Many2one('event.user')
#     event_place = fields.Many2one('event.place',"Place")
# 	event_district = fields.Many2one('event.district',"District")
#     event_name = fields.Many2one('event.event',"Event")
# 	desc = fields.Text("Details")
#     date_event = fields.Date("Date of event") 


class Place(models.Model):
    _name = 'event.place'
    _rec_name = 'place'

    place = fields.Char('Place')
    event_district = fields.Selection([('AL', 'AALAPUZHA'),
                                       ('ER', 'ERNAKULAM'),
                                       ('ID', 'IDUKKI'),
                                       ('KN', 'KANNUR'),
                                       ('KS', 'KASARAGOD'),
                                       ('KL', 'KOLLAM'),
                                       ('KT', 'KOTTAYAM'),
                                       ('KZ', 'KOZHIKODE'),
                                       ('MA', 'MALAPPURAM'),
                                       ('PL', 'PALAKKAD'),
                                       ('PT', 'PATHANAMTHITTA'),
                                       ('TV', 'THIRUVANANTHAPURAM'),
                                       ('TS', 'THRISSUR'),
                                       ('WA', 'WAYANAD')])

    date=fields.Date(default=fields.Date.today,required='True')

    def call_event(self, cr, uid, ids, context):
        mod_obj = self.pool.get('ir.model.data')
        act_obj = self.pool.get('ir.actions.act_window')
        result = mod_obj.get_object_reference(cr, uid, 'sesa_requirement', 'action_activity')
        id = result and result[1] or False
        result = act_obj.read(cr, uid, [id], context=context)[0]
        return result
