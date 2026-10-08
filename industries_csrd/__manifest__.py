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
    'name': 'Industry-vrtl: CSRD, Vertel',
    'version': '18.0.1.0.0',
    # Version ledger: XX.0 = Odoo version. 1 = Major. Non regressionable code. 2 = Minor. New features that are regressionable. 3 = Bug fixes
    'summary': 'CSRD, a collection of modules, Vertel.',
    'category': 'Industries',
    'description': '''
CSRD, Vertel
============

    Vertel made a collection of Community Edition modules inspired of Odoo Industries series.

    Features:

        - Focused Fix: A small, targeted improvement to standard Odoo behaviour.
    ''',
    #'sequence': '1'
    'author': 'Vertel Sverige AB',
    'website': 'https://vertel.se/apps/odoo-industry-vrtl/industries_csrd',
    'images': ['static/description/banner.png'], # 560x280 px.
    'license': 'AGPL-3',
    'contributor': '',
    'maintainer': 'Vertel Sverige AB',
    'repository': 'https://github.com/vertelab/odoo-industry-vrtl',
    'depends': [
        # 2024-12-13 insert depending moduels here!
       # 'mail',
       # 'account',
       # 'point_of_sale',
        ],
    'data': [
#        'data/data.xml'
    ],
    'installable': 'True',
}
