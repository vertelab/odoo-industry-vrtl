# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo SA, Open Source Management Solution, third party addon
#    Copyright (C) 2024- Vertel Sverige AB (<https://vertel.se>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Industry-vrtl-demo: LMS, Vertel',
    'version': '18.0.1.0.0',
    # Version ledger: XX.0 = Odoo version. 1 = Major. Non regressionable code. 2 = Minor. New features that are regressionable. 3 = Bug fixes
    'summary': 'Learning Management System, Vertel - DEMO.',
    'category': 'Industries',
    'description': '''
LMS, Vertel
===========

    This module is depending on industries_lms
        and adding some demo data for this parent module!

    Features:

        - Demo Data: Ships pre-configured demo data for the industry.
    ''',
    #'sequence': '1'
    'author': 'Vertel Sverige AB',
    'website': 'https://vertel.se/apps/odoo-industry-vrtl/industries_lms_demo',
    'images': ['static/description/banner.png'], # 560x280 px.
    'license': 'AGPL-3',
    'contributor': '',
    'maintainer': 'Vertel Sverige AB',
    'repository': 'https://github.com/vertelab/odoo-industry-vrtl_demo',
    'depends': [
        'website_slides',
        'industries_lms',
    ],
    
    'data': [
        'data/gamification_data.xml',
        'data/mail_activity_type_data.xml',
        'data/mail_message_subtype_data.xml',
        'data/website_data.xml',
        'data/slide_data.xml',
        'data/mail_template_data.xml',
        'data/mail_templates.xml',
        # ~ 'data/slides_tour.xml',
        'data/res_users_demo.xml',
        'data/slide_channel_tag_demo.xml',
        'data/slide_channel_demo.xml',
        'data/slide_slide_demo.xml',
        #'data/slide_user_demo.xml',
        #'data/slide_user_gamification_demo.xml',
    ],

    # ~ 'demo': [
        # ~ 'data/res_users_demo.xml',
        # ~ 'data/slide_channel_tag_demo.xml',
        # ~ 'data/slide_channel_demo.xml',
        # ~ 'data/slide_slide_demo.xml',
        # ~ 'data/slide_user_demo.xml',
        # ~ 'data/slide_user_gamification_demo.xml',

    # ~ ],
    'installable': True,
}
