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
    'name': 'Industry-vrtl: LMS, Vertel',
    'version': '18.0.1.0.0',
    # Version ledger: XX.0 = Odoo version. 1 = Major. Non regressionable code. 2 = Minor. New features that are regressionable. 3 = Bug fixes
    'summary': 'Learning Management System, Vertel.',
    'category': 'Industries',
    'description': '''
LMS, Vertel
===========

    Dependencies origin från Vertel.
        odoo-event
        odoo-hr
        odoo-website
        https://github.com/vertelab/odoo-event
        https://github.com/vertelab/odoo-website
        https://github.com/vertelab/odoo-hr

    OCA
        base_user_role
        https://github.com/OCA/server-backend
        https://github.com/OCA/knowledge

    Features:

        - Focused Fix: A small, targeted improvement to standard Odoo behaviour.
    ''',
    #'sequence': '1'
    'author': 'Vertel Sverige AB',
    'website': 'https://vertel.se/apps/odoo-industry-vrtl/industries_lms',
    'images': ['static/description/banner.png'], # 560x280 px.
    'license': 'AGPL-3',
    'contributor': '',
    'maintainer': 'Vertel Sverige AB',
    'repository': 'https://github.com/vertelab/odoo-industry-vrtl',
    'depends': [
        'event_waitlist_website',
        'website_event_portal',
        'event_lms',
        'event_hr',
        'event_lms_td',
        'base_user_role',
        'document_knowledge',
        'document_page_access_group',
    ],
    'data': [
        #'data/data.xml'
    ],
    'installable': 'True',
}
