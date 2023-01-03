{
    'name': 'Extend Enterprise Trial',
    'version': '16.0.1.0.0',
    'author': 'Onnet Consulting Sdn Bhd',
    'category': 'Hidden',
    'description': """
Extend Enterprise Trial
=======================
Easily extend the enterprise trial period with just one click!

Default trial period is **90 days**.

But It can be easily customizable. Set the System Parameter,

**database.extend_enterprise_trial** to any **integer value**.
    """,
    'website': 'https://on.net.my/',
    'depends': ['web_enterprise', 'mail'],
    'data': [
    ],
    'assets': {
        'web.assets_backend': [
            'extend_enterprise_trial/static/src/js/expiration_panel.js',
            'extend_enterprise_trial/static/src/xml/base.xml',
        ],
    },
    'installable': True,
    'auto_install': False,
}
