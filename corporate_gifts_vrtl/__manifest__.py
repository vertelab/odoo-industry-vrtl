# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo SA, Open Source Management Solution, third party addon
#    Copyright (C) 2023- Vertel AB (<https://vertel.se>).
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
    'name': 'Industry-vrtl: Corporate Gifts, Vertel',
    'version': '18.0.1.0.0',
    # Version ledger: 14.0 = Odoo version. 1 = Major. Non regressionable code. 2 = Minor. New features that are regressionable. 3 = Bug fixes
    'summary': 'Corporate Gifts, Vertel.',
    'category': 'Industries',
    'description': '''
Corporate Gifts, Vertel
=======================

    Vertel made a collection of Community Edition modules inspired of Odoo Industries series.

    Features:

        - Focused Fix: A small, targeted improvement to standard Odoo behaviour.
    ''',
    #'sequence': '1'
    'author': 'Vertel AB',
    'website': 'https://vertel.se/apps/odoo-industry-vrtl/corporate_gifts_vrtl',
    'images': ['static/description/banner.png'], # 560x280 px.
    'license': 'AGPL-3',
    'contributor': '',
    'maintainer': 'Vertel AB',
    'repository': 'https://github.com/vertelab/odoo-industry-vrtl',
    'depends': [
        # ~ 'knowledge',
        'mail',
        'crm',
        'calendar',
        'contacts',
        'website',
        #'documents',
        #'dms',
        'hr',
        'project',
        'sale_management',
        'account',
        'website_sale',
        'stock',
        'purchase',
        'planning_ce',
       ],
    'data': [
#        'data/data.xml'
    ],
    'installable': 'True',
}
