openerp.sesa_requirement = function (instance) {
    var WebClient = instance.web.WebClient;

    WebClient.include({
        init: function (parent, client_options) {
            this._super(parent, client_options);
            // Your custom initialization code here
            this.set('title_part', { "zopenerp": "" });
        },
    });
};
