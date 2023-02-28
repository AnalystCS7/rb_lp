odoo.define('royal_rewards.royal_rewards', function (require) {
    'use strict';

    var rpc = require('web.rpc');
    var publicWidget = require('web.public.widget');

    publicWidget.registry.RoyalRewards = publicWidget.Widget.extend({
        selector: '.royal_rewards_widget',
        xmlDependencies: ['/royal_rewards/static/src/xml/royal_rewards.xml'],

        events: {
            'click .btn-redeem-points': '_onClickRedeemPoints',
            'click .btn-apply-promo': '_onClickApplyPromo',
        },

        init: function () {
            this._super.apply(this, arguments);
            this.rewardProgramId = parseInt(this.$el.data('reward-program-id'));
            this.customerBalance = parseFloat(this.$el.data('customer-balance'));
            this.redeemedPoints = 0;
            this.appliedPromo = null;
            this.promoAppliedMessage = null;
            this.$('.royal_rewards_points_balance').text(this.customerBalance);
        },

        start: function () {
            return this._super.apply(this, arguments).then(this._loadData.bind(this));
        },

        _loadData: function () {
            var self = this;
            var rpcPromises = [];
            rpcPromises.push(rpc.query({
                model: 'res.partner',
                method: 'search_read',
                args: [[['id', '=', odoo.session_info.partner_id]], ['royal_rewards_balance']],
                kwargs: {context: odoo.session_info.user_context},
            }).then(function (partners) {
                if (partners.length > 0) {
                    self.customerBalance = partners[0].royal_rewards_balance;
                    self.$('.royal_rewards_points_balance').text(self.customerBalance);
                }
            }));
            rpcPromises.push(rpc.query({
                model: 'royal_rewards.reward',
                method: 'get_reward_types',
                args: [],
            }).then(function (rewardTypes) {
                self.rewardTypes = rewardTypes;
            }));
            return Promise.all(rpcPromises);
        },

        _onClickRedeemPoints: function (ev) {
            var self = this;
            ev.preventDefault();
            var pointsToRedeem = parseInt(this.$('.royal_rewards_input_points_to_redeem').val());
            if (isNaN(pointsToRedeem) || pointsToRedeem <= 0) {
                this._showMessage('error', 'Invalid points value.');
                return;
            }
            if (pointsToRedeem > this.customerBalance) {
                this._showMessage('error', 'Not enough points to redeem.');
                return;
            }
            var rewardTypeId = parseInt(this.$('.royal_rewards_select_reward_type').val());
            if (isNaN(rewardTypeId)) {
                this._showMessage('error', 'Invalid reward type.');
                return;
            }
            var rpcPromise = rpc.query({
                model: 'royal_rewards.reward',
                method: 'redeem_points',
                args: [[self.rewardProgramId], rewardTypeId, pointsToRedeem],
            }).then(function (result) {
                self.customerBalance -= pointsToRedeem;
                self.$('.royal_rewards_points_balance').text(self.customerBalance);
                self.redeemedPoints += pointsToRedeem;
                self._showMessage('success', 'Points redeemed successfully.');
            });
            return Promise.all([rpcPromise]);
        },
        _onClickApplyPromo: function (ev) {
            var self = this;
            ev.preventDefault();
            var promoCode = this.$('.royal_rewards_input_promo_code').val();
            if (!promoCode) {
                this._showMessage('error', 'Please enter a valid promo code.');
                return;
            }
            var rpcPromise = rpc.query({
                model: 'royal_rewards.reward',
                method: 'apply_promo_code',
                args: [[self.rewardProgramId], promoCode],
            }).then(function (result) {
                if (result) {
                    self.appliedPromo = result;
                    self.promoAppliedMessage = 'Promo code applied successfully: ' + result.promo_code;
                    self.$('.royal_rewards_applied_promo_code').text(self.promoAppliedMessage);
                } else {
                    self._showMessage('error', 'Invalid promo code.');
                }
            });
            return Promise.all([rpcPromise]);
        },

        _showMessage: function (type, message) {
            var messageClass = 'alert-' + type;
            var $messageEl = $('<div/>', {
                class: 'alert ' + messageClass,
                text: message,
            });
            this.$('.royal_rewards_messages').empty().append($messageEl).show();
            setTimeout(function () {
                $messageEl.fadeOut(1000, function () {
                    $messageEl.remove();
                });
            }, 3000);
        },
    });
});
