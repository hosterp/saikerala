openerp.sesa_requirement = function (instance) {
    var WebClient = instance.web.WebClient;

    WebClient.include({
        init: function (parent, client_options) {
            this._super(parent, client_options);
            // Custom initialization code
            this.set('title_part', { "zopenerp": "" });
        },
        show_application: function () {
            this._super.apply(this, arguments);
            // Force display of all menu items
            var menu = document.querySelector('.oe_main_menu_navbar');
            if (menu) {
                menu.classList.add('show');
            }
        }
    });
};

$(document).ready(function () {
    // Auto-select first radio button
    $('.oe_form_field_radio input[type="radio"]').first().prop('checked', true);

    // Tab navigation for form inputs on Enter key
    $(document).on('keydown', 'input[type="text"], textarea, .o_field_many2one input, .oe_form_field_radio input[type="radio"], .oe_form_field_selection select', function(event) {
        if (event.which === 13) {
            event.preventDefault();

            var inputs = $('input[type="text"], textarea, .o_field_many2one input, .oe_form_field_radio input[type="radio"], .oe_form_field_selection select').filter(':visible:not([readonly]):not(:disabled)');
            var index = inputs.index(this);
            if (index < inputs.length - 1) {
                inputs.eq(index + 1).focus().select();
            } else {
                inputs.eq(0).focus().select();
            }
        }
    });

    // Hide date picker on Enter key press
    $(document).on('keydown', function(e) {
        if (e.key === 'Enter' && $('.ui-datepicker').is(':visible')) {
            $('.ui-datepicker').hide();
        }
    });

    // Auto-resize textarea based on content
    $('textarea.field_text').each(function() {
        // Set initial size
        $(this).css({ width: '120px', height: '30px', resize: 'none', overflow: 'hidden' });

        // Adjust width and height based on content
        $(this).on('input', function() {
            this.style.width = '120px';
            this.style.height = '30px';

            // Calculate the new size
            this.style.width = (this.scrollWidth + 2) + 'px';
            this.style.height = (this.scrollHeight + 2) + 'px';
        });
    });
});



