
{
    'name': 'CustomButton',
    'summary': '',
    'version': '1.0',

    'description': """

    """,

    # 'author': '',
    # 'maintainer': '',
    # 'contributors': [''],

    # 'website': '',

    'license': 'AGPL-3',
    'category': 'Uncategorized',

    'depends': [
        'base', 'point_of_sale',
    ],
    'external_dependencies': {
        'python': [
        ],
    },
    'data': [
        'views/templates.xml',

    ],
    'demo': [
    ],
    'js': [
    ],
    'css': [
    ],
    'qweb': [
	'static/src/xml/custom_button.xml',
    ],
    'images': [
    ],
    'test': [
    ],

    'installable': True
}
