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
    'name': 'Industry-vrtl: l10n_se_account, Vertel',
    'version': '1.0.0',
    # Version ledger: 14.0 = Odoo version. 1 = Major. Non regressionable code. 2 = Minor. New features that are regressionable. 3 = Bug fixes
    'summary': 'l10n_se_account, Vertel',
    'category': 'Industries',
    'description': """
    l10n_se_account, Vertel Style
    
    Vertel made a collection of Community Edition modules inspired of Odoo Industries series.
    
    
    odoo-l10n_se
    git@github.com:OCA/bank-statement-import.git

    
    """,
    'author': 'Vertel AB',
    'website': 'https://vertel.se/apps/odoo-industry-vrtl/l10n_se_account_k2',
    'images': ['static/description/banner.png'], # 560x280 px.
    'license': 'AGPL-3',
    'contributor': '',
    'maintainer': 'Vertel AB',
    'repository': 'https://github.com/vertelab/odoo-industry-vrtl',
    'depends': [
        'l10n_se',
        'l10n_se_extended',
        'l10n_se_mis',
        'l10n_se_tax_report',
        'account_period_vrtl',
        'account_statement_import_camt54',
        'account_reconcile_oca',
        #'account_banking_sepa_direct_debit', Waiting for 18 version
        #'account_banking_sepa_credit_transfer', Waiting for 18 version
        #'account_payment_order', Waiting for 18 version
        
        ],
    'data': [],
    'installable': 'True',
    'post_init_hook': 'try_load_k2',
}
##https://github.com/OCA/bank-statement-import
##https://github.com/vertelab/odoo-l10n_se
##https://github.com/vertelab/odoo-account
##https://github.com/OCA/bank-payment
