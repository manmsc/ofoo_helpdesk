odoo.define('extend_enterprise_trial.ExpirationPanel', function (require) {
    "use strict";

    const { ExpirationPanel } = require("@web_enterprise/webclient/home_menu/expiration_panel");
    const { patch } = require('web.utils');
    var rpc = require('web.rpc');

    patch(ExpirationPanel.prototype, "extend_enterprise_trial/static/src/js/expiration_panel.js", {
        /**
         * @private
         */
        async _onExtendTrial() {
            var ex = document.getElementById("expiration_date").value;
            if (ex < 1 || ex > 365){
                  alert("Please key in any integer number between 1 to 365.");
            }
            else{
                return rpc.query({
                    model: 'ir.config_parameter',
                    method: 'extend_trial_period',
                    args: [ex],
                }).then(function () {
                    window.location.reload();
                });
            }
        }
    });

});
