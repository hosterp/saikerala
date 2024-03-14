from openerp import fields, models, api

class DistrictLevelMeetings(models.Model):
    _name = 'event.district'

    date = fields.Date(string="Date", default=fields.Date.today)
    events_planned = fields.Text(string="Programs/Events Planned")
    no_monthily_meeting = fields.Integer(string="Monthly Meetings")
    no_family = fields.Integer(string='No. of Families Attend Family Narayana Seva')
    no_saplings = fields.Integer(string='No. of Saplings Planted (Prematharu)')
    missing_activities = fields.Integer(string='Missing Activities')

    @api.multi
    def print_activity_district_level_meeting_details_report(self):
        datas = {
            'ids': self._ids,
            'model': self._name,
            'form': self.read(),
            'context': self._context,
        }
        data = self.env['ir.actions.report.xml'].search(
            [('model', '=', 'event.district'),
             ('report_name', '=', 'sesa_requirement.activity_district_level_meeting_details_report_template',)])
        if data.download_filename:
            data.download_filename = 'DistrictLevelMeetingReport'
        return {
            'type': 'ir.actions.report.xml',
            'report_name': 'sesa_requirement.activity_district_level_meeting_details_report_template',
            'datas': datas,
            'report_type': 'qweb-pdf',
        }