# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo SA, Open Source Management Solution, third party addon
#    Copyright (C) 2024- Vertel AB (<https://vertel.se>).
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
    'name': 'Industry-vrtl: ITSM, Vertel',
    'version': '18.0.1.0.0',
    # Version ledger: XX.0 = Odoo version. 1 = Major. Non regressionable code. 2 = Minor. New features that are regressionable. 3 = Bug fixes
    'summary': 'IT System Management, Vertel.',
    'category': 'Industries',
    'description': '''
ITSM, Vertel
============

    Dependencies origin från Vertel and OCA.
        https://github.com/OCA/account-financial-tools
        https://github.com/OCA/knowledge
        https://github.com/OCA/helpdesk
        https://github.com/OCA/hr
        https://github.com/OCA/server-ux
        https://github.com/OCA/server-backend
        https://github.com/OCA/reporting-engine

    https://github.com/vertelab/odoo-account/
        https://github.com/vertelab/odoo-user-mail/
        https://github.com/vertelab/odoo-base

    Features:

        - Focused Fix: A small, targeted improvement to standard Odoo behaviour.
    ''',
    #'sequence': '1'
    'author': 'Vertel AB',
    'website': 'https://vertel.se/apps/odoo-industry-vrtl/industries_itsm',
    'images': ['static/description/banner.png'], # 560x280 px.
    'license': 'AGPL-3',
    'contributor': '',
    'maintainer': 'Vertel AB',
    'repository': 'https://github.com/vertelab/odoo-industry-vrtl',
    'depends': [
    'account',
    'website',
    'stock',
    'purchase',
    'project',
    'hr',
    'document_knowledge',
    'helpdesk_mgmt',
    'contacts',
    'calendar',
    'purchase_price_diff',
    'stock_account',
    'website_sms',
    'purchase_stock',
    'account_asset_lot_stock',
    'account_asset_lot_stock_personal_equipment',
    'account_asset_management',
    'account_sequence',
    'analytic',
    'attachment_indexation',
    'barcodes',
    'barcodes_gs1_nomenclature',
    'base',
    'base_import',
    'base_install_request',
    'base_setup',
    'base_tier_validation',
    'base_user_role',
    'base_user_role_company',
    'base_user_role_mass_addition',
    'base_vat',
    'bus',
    'calendar_sms',
    'document_page',
    'helpdesk_escalation',
    'helpdesk_hierarchy_category',
    'helpdesk_mgmt_project',
    'helpdesk_mgmt_sla',
    'helpdesk_mgmt_sla_notification',
    'helpdesk_mgmt_translation',
    'helpdesk_related_ticket',
    'helpdesk_type',
    'hr_gamification',
    'hr_org_chart',
    'hr_personal_equipment_request',
    'hr_personal_equipment_request_tier_validation',
    'hr_personal_equipment_stock',
    'knowledge_forum_website',
    'link_tracker',
    'portal_rating',
    'product',
    'project_purchase',
    'project_sms',
    'rating',
    'report_xlsx',
    'report_xlsx_helper',
    'resource',
    'sms',
    'snailmail',
    'snailmail_account',
    'social_media',
    'stock_sms',
    'uom',
    'utm',
    'web',
    'web_editor',
    'web_kanban_gauge',
    'web_tour',
    'web_unsplash',
    'website_form_project',
    'website_links',
    'website_mail',
    'website_mass_mailing',
    'website_partner',
    'website_payment',
    'website_profile',
    'mass_mailing_themes',
    'gamification',
    'website_forum',
    'portal',
    'phone_validation',
    ],
    'data': [
        #'data/data.xml'
    ],
    'installable': 'True',
}
