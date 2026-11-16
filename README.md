# odoo-industry-vrtl


We update and upgrade.

## Porteringsstatus

18.0 är baseline. 19.0/20.0 visar om p-filen har ett villkor för utgåvan
— inte om grenen finns. Blockerare är `depends` som saknas i 20.0
(kärna + alla 20.0-grenar).

| Modul | Beskrivning | Manifest | p-fil | 19.0 | 20.0 | Blockerare |
|---|---|---|---|---|---|---|
| art_craft_vrtl | The Arts & Craft Shop, Vertel. | 1.0.0 | 0 | — | — | — |
| automotive_vrtl | Automotive Spareparts, Vertel. | 1.0.0 | 0 | — | — | `planning_ce` |
| bar_and_lounge_vrtl | Bar & Lounge, Vertel. | 1.0.0 | 0 | — | — | `planning_ce` |
| cake_shop_vrtl | Cake Shop, Vertel. | 1.0.0 | 0 | — | — | — |
| certification_organism_vrtl | Certification Auditors, Vertel. | 1.0.0 | 0 | — | — | — |
| clothing_boutique_vrtl | Clothing and Boutique, Vertel. | 1.0.0 | 0 | — | — | — |
| corporate_gifts_vrtl | Corporate Gifts, Vertel. | 1.0.0 | 0 | — | — | `planning_ce` |
| hair_salon_vrtl | Hair Salon, Vertel. | 1.0.0 | 0 | — | — | — |
| hardware_shop_vrtl | Hardware shop, Vertel. | 1.0.0 | 0 | — | — | `planning_ce` |
| industries_contractor | IT System Management, Vertel. | 1.0.0 | 0 | — | — | `product_contract` |
| industries_csrd | CSRD, a collection of modules, Vertel. | 1.0.0 | 0 | — | — | — |
| industries_itsm | IT System Management, Vertel | 1.0 | 2 | — | — | `helpdesk_mgmt` `purchase_price_diff` `account_asset_management` `account_sequence` `base_tier_validation` `base_user_role` `base_user_role_company` `base_vat` `helpdesk_escalation` `helpdesk_hierarchy_category` `helpdesk_mgmt_project` `helpdesk_mgmt_sla` `helpdesk_mgmt_sla_notification` `helpdesk_mgmt_translation` `helpdesk_related_ticket` `helpdesk_type` `hr_org_chart` `hr_personal_equipment_request` `hr_personal_equipment_request_tier_validation` `hr_personal_equipment_stock` `report_xlsx_helper` `web_editor` `web_kanban_gauge` `website_form_project` |
| industries_lms | Learning Management System, Vertel. | 1.0.0 | 0 | — | — | `event_waitlist_website` `website_event_portal` `event_lms` `event_hr` `event_lms_td` `base_user_role` `document_page_access_group` |
| industries_lms_demo | Learning Management System, Vertel - DEMO. | 1.0.0 | 0 | — | — | — |
| industry_lawyer_vrtl | Industry Lawyer, Vertel. | 1.0.0 | 0 | — | — | `planning_ce` `hr_timesheet_sheet` |
| industry_real_estate_vrtl | Real Estate Agency, Vertel. | 1.0.1 | 0 | — | — | `sale_subscription` |
| l10n_se_account_k2 | L10n_se_account, Vertel. | 1.0.0 | 0 | — | — | `account_statement_import_camt54` `account_reconcile_oca` |
| l10n_se_payroll | L10n_se_payroll, Vertel. | 1.0.0 | 0 | — | — | — |
| larplattform_lms | Complete installation package for a learning platform (LMS). | 1.0.0 | 0 | — | — | `bt_ajax_upload_file_common` `bt_survey_ajax_upload_file` `event_waitlist_website` `website_event_portal` `account_payment_term` `base_user_role` `base_user_role_company` `base_vat` `event_elearning` `event_hr_elearning_overview` `event_hr_requirement` `event_reservation` `event_url_portal` `hr_org_chart` `letsencrypt` `letsencrypt_nginx` `sale_async_emails` `sale_product_configurator` `survey_department` `survey_likert_scale` `survey_manual_review` `web_editor` `website_event_portal_elearning` `website_form_project` `website_jitsi` `website_portal_department` `website_event_jitsi` |
| non_profit_organization_vrtl | Nonprofit Organization, Vertel. | 1.0.0 | 0 | — | — | `sale_subscription` |
| photography_vrtl | Photographer, Vertel. | 1.0.0 | 0 | — | — | — |
| software_reseller_vrtl | Software Reseller, Vertel. | 1.0.0 | 0 | — | — | `sale_subscription` `planning_ce` `account_accountant` |
| sports_club_vrtl | Sports Club, Vertel. | 1.0.0 | 0 | — | — | `planning_ce` `contact` `social` |
| surveyor_vrtl | Surveyor, Vertel. | 1.0.1 | 0 | — | — | `planning_ce` |
