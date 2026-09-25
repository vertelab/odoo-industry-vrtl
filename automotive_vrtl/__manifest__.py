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
    'name': 'Industry-vrtl: Automotive Spareparts, Vertel',
    'version': '18.0.1.0.0',
    # Version ledger: 14.0 = Odoo version. 1 = Major. Non regressionable code. 2 = Minor. New features that are regressionable. 3 = Bug fixes
    'summary': 'Automotive Spareparts, Vertel.',
    'category': 'Industries',
    'description': '''
Automotive Spareparts, Vertel
=============================

    Vertel made a collection of Community Edition modules inspired of Odoo Industries series.

    requirements.repo
        git@github.com:vertelab/odoo-calendar.git /usr/share/odoo-calendar
        git@github.com:vertelab/odoo-planning.git /usr/share/odoo-planning

    Features:

        - Focused Fix: A small, targeted improvement to standard Odoo behaviour.
    ''',
    #'sequence': '1'
    'author': 'Vertel AB',
    'website': 'https://vertel.se/apps/odoo-industry-vrtl/automotive_vrtl',
    'images': ['static/description/banner.png'], # 560x280 px.
    'license': 'AGPL-3',
    'contributor': '',
    'maintainer': 'Vertel AB',
    'repository': 'https://github.com/vertelab/odoo-industry-vrtl',
    'depends': [
        'website_calendar_ce',
        'mail',
        'account',
        'point_of_sale',
        'sale_management',
        'stock',
        #'account_accountant',
        'purchase',
        'planning_ce',
        'hr',
        ],
    'data': [
        'data/data.xml'
    ],
    'installable': 'True',
}
