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
    'name': 'Industry-vrtl: Lärplattform, LMS',
    'version': '18.0.1.0.0',
    # Version ledger: XX.0 = Odoo version. 1 = Major. Non regressionable code. 2 = Minor. New features that are regressionable. 3 = Bug fixes
    'summary': "Complete installation package for a learning platform (LMS).",
    'category': 'Industries',
    'description': '''
Lärplattform, LMS
=================

    Vertel made a collection of Community Edition modules inspired of Odoo Industries series.

    Features:

        - Focused Fix: A small, targeted improvement to standard Odoo behaviour.
    ''',
    #'sequence': '1'
    'author': 'Vertel Sverige AB',
    'website': 'https://vertel.se/apps/odoo-industry-vrtl/larplattform_lms',
    'images': ['static/description/banner.png'], # 560x280 px.
    'license': 'AGPL-3',
    'contributor': '',
    'maintainer': 'Vertel Sverige AB',
    'repository': 'https://github.com/vertelab/odoo-industry-vrtl',
    'depends': [ 
    #Tekniskt namn
    'sale_management',
    'account',
    'website',
    'project',
    'mass_mailing',
    'hr',
    'bt_ajax_upload_file_common',
    'bt_survey_ajax_upload_file',
    'event_waitlist_website',
    'l10n_se_extended',
    'website_event_portal',
    'website_slides',
    'website_event',
    'mail',
    'contacts',
    'survey',
    'project_todo',
    'hr_skills',
    'website_sms',
    'account_edi_ubl_cii',
    'account_payment',
    'account_payment_term',
    'analytic',
    'auth_admin',
    'auth_signup',
    'auth_totp',
    'auth_totp_mail',
    'auth_totp_portal',
    'barcodes',
    'base',
    'base_import',
    'base_import_module',
    'base_install_request',
    'base_setup',
    'base_user_role',
    'base_user_role_company',
    'base_vat',
    'bus',
    'digest',
    'event',
    'event_elearning',
    'event_hr_elearning_overview',
    'event_hr_requirement',
    'event_reservation',
    'event_sale',
    'event_sms',
    'event_url_portal',
    'google_gmail',
    'google_recaptcha',
    'hr_gamification',
    'hr_org_chart',
    'hr_skills_slides',
    'hr_skills_survey',
    'iap',
    'iap_mail',
    'l10n_se',
    'letsencrypt',
    'letsencrypt_nginx',
    'link_tracker',
    'mail_bot',
    'mail_bot_hr',
    'mass_mailing_event',
    'mass_mailing_sale',
    'mass_mailing_slides',
    'partner_autocomplete',
    'payment',
    'portal_rating',
    'privacy_lookup',
    'product',
    'project_account',
    'project_sms',
    'rating',
    'resource',
    'sale',
    'sale_async_emails',
    'sale_pdf_quote_builder',
    'sale_product_configurator',
    'sale_project',
    'sale_service',
    'sale_sms',
    'sales_team',
    'sms',
    'snailmail',
    'snailmail_account',
    'social_media',
    'spreadsheet',
    'spreadsheet_account',
    'spreadsheet_dashboard',
    'spreadsheet_dashboard_account',
    'spreadsheet_dashboard_event_sale',
    'spreadsheet_dashboard_sale',
    'survey_department',
    'survey_likert_scale',
    'survey_manual_review',
    'uom',
    'utm',
    'web',
    'web_editor',
    'web_hierarchy',
    'web_tour',
    'web_unsplash',
    'website_event_portal_elearning',
    'website_form_project',
    'website_jitsi',
    'website_links',
    'website_mail',
    'website_mass_mailing',
    'website_partner',
    'website_payment',
    'website_portal_department',
    'website_profile',
    'website_slides_forum',
    'website_slides_survey',
    'mass_mailing_themes',
    'gamification',
    'website_forum',
    'website_event_jitsi',
    'portal',
    'onboarding',
    'http_routing',
    'phone_validation',
    ],
    'data': [
#        'data/data.xml'
    ],
    'installable': 'True',
}
