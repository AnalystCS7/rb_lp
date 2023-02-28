odoo.define('royal_rewards.royal_rewards_form', function (require) {
    'use strict';

    var core = require('web.core');
    var FormView = require('web.FormView');

    var qweb = core.qweb;

    FormView.include({
        render_buttons: function () {
            this._super.apply(this, arguments);
            if (this.model === 'royal_rewards.reward') {
                this.$buttons.find('.o_form_button_create').text('Create Reward');
            }
            if (this.model === 'royal_rewards.program') {
                var buttonHtml = qweb.render('royal_rewards.reward_button', {widget: this});
                this.$buttons.append(buttonHtml);
            }
        },

        _onButtonClicked: function (event) {
            if (event.currentTarget.classList.contains('o_reward_button')) {
                event.preventDefault();
                this.do_action({
                    type: 'ir.actions.act_window',
                    res_model: 'royal_rewards.reward',
                    views: [[false, 'form']],
                    target: 'current',
                    context: {
                        default_program_id: this.res_id,
                        default_reward_type_id: 1,
                    },
                });
            }
        },
    });
});
