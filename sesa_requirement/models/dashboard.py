from openerp import fields, models, api
from datetime import date
from datetime import  datetime,timedelta

from openerp.exceptions import ValidationError


class HRDashboard(models.Model):
    _name = 'event.dashboard'

    color = fields.Integer(string='Color Index')
    name = fields.Char(string="Name")
    image_kanban=fields.Binary('Image')
    place_count = fields.Integer(string='Place Count', compute='get_place_count_from_event_place')

    @api.depends('place_count')
    @api.one
    def get_place_count_from_event_place(self):
        event_place_model = self.env['event.place']
        place_record = event_place_model.search([], limit=1)
        self.place_count = place_record.place_count if place_record else 0



    def call_place(self,cr,uid,ids,context):
        place_obj = self.pool.get('event.place')
        places = place_obj.search(cr, uid, [('event_district', '=', 'TV')], context=context)
        tvm_place_count = len(places)
        print(tvm_place_count,'count................')
        mod_obj = self.pool.get('ir.model.data')
    	act_obj = self.pool.get('ir.actions.act_window')
    	result = mod_obj.get_object_reference(cr, uid, 'sesa_requirement', 'action_dashboard_places')
        action_id = result and result[1] or False
        result = act_obj.read(cr, uid, [action_id], context=context)[0]
        result['name'] = "THIRUVANANTHAPURAM ({})".format(tvm_place_count)
        return result

    def call_pta(self,cr,uid,ids,context):
        place_obj = self.pool.get('event.place')
        places = place_obj.search(cr, uid, [('event_district', '=', 'PT')], context=context)
        tvm_place_count = len(places)
        print(tvm_place_count, 'count................')
        mod_obj = self.pool.get('ir.model.data')
        act_obj = self.pool.get('ir.actions.act_window')
        result = mod_obj.get_object_reference(cr, uid, 'sesa_requirement', 'action_dashboard_places_pta')
        action_id = result and result[1] or False
        result = act_obj.read(cr, uid, [action_id], context=context)[0]
        result['name'] = "PATHANAMTHITTA ({})".format(tvm_place_count)
        return result


    def call_kollam(self,cr,uid,ids,context):
        place_obj = self.pool.get('event.place')
        places = place_obj.search(cr, uid, [('event_district', '=', 'KL')], context=context)
        tvm_place_count = len(places)
        print(tvm_place_count, 'count................')
        mod_obj = self.pool.get('ir.model.data')
        act_obj = self.pool.get('ir.actions.act_window')
        result = mod_obj.get_object_reference(cr, uid, 'sesa_requirement', 'action_dashboard_places_kl')
        action_id = result and result[1] or False
        result = act_obj.read(cr, uid, [action_id], context=context)[0]
        result['name'] = "KOLLAM ({})".format(tvm_place_count)
        return result


    def call_al(self,cr,uid,ids,context):
        place_obj = self.pool.get('event.place')
        places = place_obj.search(cr, uid, [('event_district', '=', 'AL')], context=context)
        tvm_place_count = len(places)
        print(tvm_place_count, 'count................')
        mod_obj = self.pool.get('ir.model.data')
        act_obj = self.pool.get('ir.actions.act_window')
        result = mod_obj.get_object_reference(cr, uid, 'sesa_requirement', 'action_dashboard_places_al')
        action_id = result and result[1] or False
        result = act_obj.read(cr, uid, [action_id], context=context)[0]
        result['name'] = "ALAPPUZHA ({})".format(tvm_place_count)
        return result

    def call_er(self,cr,uid,ids,context):
        place_obj = self.pool.get('event.place')
        places = place_obj.search(cr, uid, [('event_district', '=', 'ER')], context=context)
        tvm_place_count = len(places)
        print(tvm_place_count, 'count................')
        mod_obj = self.pool.get('ir.model.data')
        act_obj = self.pool.get('ir.actions.act_window')
        result = mod_obj.get_object_reference(cr, uid, 'sesa_requirement', 'action_dashboard_places_er')
        action_id = result and result[1] or False
        result = act_obj.read(cr, uid, [action_id], context=context)[0]
        result['name'] = "ERNAKULAM ({})".format(tvm_place_count)
        return result

    def call_id(self,cr,uid,ids,context):
        place_obj = self.pool.get('event.place')
        places = place_obj.search(cr, uid, [('event_district', '=', 'ID')], context=context)
        tvm_place_count = len(places)
        print(tvm_place_count, 'count................')
        mod_obj = self.pool.get('ir.model.data')
        act_obj = self.pool.get('ir.actions.act_window')
        result = mod_obj.get_object_reference(cr, uid, 'sesa_requirement', 'action_dashboard_places_id')
        action_id = result and result[1] or False
        result = act_obj.read(cr, uid, [action_id], context=context)[0]
        result['name'] = "IDUKKI ({})".format(tvm_place_count)
        return result

    def call_ks(self,cr,uid,ids,context):
        place_obj = self.pool.get('event.place')
        places = place_obj.search(cr, uid, [('event_district', '=', 'KS')], context=context)
        tvm_place_count = len(places)
        print(tvm_place_count, 'count................')
        mod_obj = self.pool.get('ir.model.data')
        act_obj = self.pool.get('ir.actions.act_window')
        result = mod_obj.get_object_reference(cr, uid, 'sesa_requirement', 'action_dashboard_places_ks')
        action_id = result and result[1] or False
        result = act_obj.read(cr, uid, [action_id], context=context)[0]
        result['name'] = "KASARAGOD ({})".format(tvm_place_count)
        return result

    def call_kt(self,cr,uid,ids,context):
        place_obj = self.pool.get('event.place')
        places = place_obj.search(cr, uid, [('event_district', '=', 'KT')], context=context)
        tvm_place_count = len(places)
        print(tvm_place_count, 'count................')
        mod_obj = self.pool.get('ir.model.data')
        act_obj = self.pool.get('ir.actions.act_window')
        result = mod_obj.get_object_reference(cr, uid, 'sesa_requirement', 'action_dashboard_places_kt')
        action_id = result and result[1] or False
        result = act_obj.read(cr, uid, [action_id], context=context)[0]
        result['name'] = "KOTTAYAM ({})".format(tvm_place_count)
        return result

    def call_kz(self,cr,uid,ids,context):
        place_obj = self.pool.get('event.place')
        places = place_obj.search(cr, uid, [('event_district', '=', 'KZ')], context=context)
        tvm_place_count = len(places)
        print(tvm_place_count, 'count................')
        mod_obj = self.pool.get('ir.model.data')
        act_obj = self.pool.get('ir.actions.act_window')
        result = mod_obj.get_object_reference(cr, uid, 'sesa_requirement', 'action_dashboard_places_kz')
        action_id = result and result[1] or False
        result = act_obj.read(cr, uid, [action_id], context=context)[0]
        result['name'] = "KOZHIKODE ({})".format(tvm_place_count)
        return result

    def call_ma(self,cr,uid,ids,context):
        place_obj = self.pool.get('event.place')
        places = place_obj.search(cr, uid, [('event_district', '=', 'MA')], context=context)
        tvm_place_count = len(places)
        print(tvm_place_count, 'count................')
        mod_obj = self.pool.get('ir.model.data')
        act_obj = self.pool.get('ir.actions.act_window')
        result = mod_obj.get_object_reference(cr, uid, 'sesa_requirement', 'action_dashboard_places_ma')
        action_id = result and result[1] or False
        result = act_obj.read(cr, uid, [action_id], context=context)[0]
        result['name'] = "MALAPPURAM ({})".format(tvm_place_count)
        return result

    def call_pl(self,cr,uid,ids,context):
        place_obj = self.pool.get('event.place')
        places = place_obj.search(cr, uid, [('event_district', '=', 'PL')], context=context)
        tvm_place_count = len(places)
        print(tvm_place_count, 'count................')
        mod_obj = self.pool.get('ir.model.data')
        act_obj = self.pool.get('ir.actions.act_window')
        result = mod_obj.get_object_reference(cr, uid, 'sesa_requirement', 'action_dashboard_places_pl')
        action_id = result and result[1] or False
        result = act_obj.read(cr, uid, [action_id], context=context)[0]
        result['name'] = "PALAKKAD ({})".format(tvm_place_count)
        return result

    def call_ts(self,cr,uid,ids,context):
        place_obj = self.pool.get('event.place')
        places = place_obj.search(cr, uid, [('event_district', '=', 'TS')], context=context)
        tvm_place_count = len(places)
        print(tvm_place_count, 'count................')
        mod_obj = self.pool.get('ir.model.data')
        act_obj = self.pool.get('ir.actions.act_window')
        result = mod_obj.get_object_reference(cr, uid, 'sesa_requirement', 'action_dashboard_places_ts')
        action_id = result and result[1] or False
        result = act_obj.read(cr, uid, [action_id], context=context)[0]
        result['name'] = "THRISSUR ({})".format(tvm_place_count)
        return result
    def call_wa(self,cr,uid,ids,context):
        place_obj = self.pool.get('event.place')
        places = place_obj.search(cr, uid, [('event_district', '=', 'WA')], context=context)
        tvm_place_count = len(places)
        print(tvm_place_count, 'count................')
        mod_obj = self.pool.get('ir.model.data')
        act_obj = self.pool.get('ir.actions.act_window')
        result = mod_obj.get_object_reference(cr, uid, 'sesa_requirement', 'action_dashboard_places_wa')
        action_id = result and result[1] or False
        result = act_obj.read(cr, uid, [action_id], context=context)[0]
        result['name'] = "WAYANAD ({})".format(tvm_place_count)
        return result
    
    def call_kn(self,cr,uid,ids,context):
        place_obj = self.pool.get('event.place')
        places = place_obj.search(cr, uid, [('event_district', '=', 'KN')], context=context)
        tvm_place_count = len(places)
        print(tvm_place_count, 'count................')
        mod_obj = self.pool.get('ir.model.data')
        act_obj = self.pool.get('ir.actions.act_window')
        result = mod_obj.get_object_reference(cr, uid, 'sesa_requirement', 'action_dashboard_places_kn')
        action_id = result and result[1] or False
        result = act_obj.read(cr, uid, [action_id], context=context)[0]
        result['name'] = "KANNUR ({})".format(tvm_place_count)
        return result

    def call_admin(self,cr,uid,ids,context):
        return