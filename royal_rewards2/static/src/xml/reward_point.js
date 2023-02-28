odoo.define('royalbeards.reward_point', function (require) {
    'use strict';

    var core = require('web.core');
    var Widget = require('web.Widget');

    var RewardPointWidget = Widget.extend({
        template: 'RewardPointWidget',

        init: function (parent, points) {
            this._super(parent);
            this.points = points;
        },
    });

    core.action_registry.add('royalbeards.reward_point', RewardPointWidget);

    return RewardPointWidget;
});
