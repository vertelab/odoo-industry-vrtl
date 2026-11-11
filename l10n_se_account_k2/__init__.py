# -*- coding: utf-8 -*-
"""K2 chart loader for l10n_se_account_k2.

Odoo 18 (lantteknik, 2026-11-10): the original hook called
``try_loading('extended_se_K2', company)`` for EVERY company in the
database. On a database that already holds reconciled journal entries
this aborts the whole module install with:

    UserError: You cannot do this modification on a reconciled journal
    entry. You can just change some non legal fields or you must
    unreconcile first.

Two guards are added:

1. Only companies that have not yet been given a chart of accounts are
   candidates. A company that already runs on a chart must not be
   re-templated by a helper hook.
2. A failure on one company is logged and skipped instead of aborting
   the registry load, so a demo company with test data can never block
   the production company from getting its chart.
"""
import logging

from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)

# Chart template codes that mean "no real chart installed yet".
_EMPTY_CHARTS = {False, "", "generic"}


def try_load_k2(env):
    chart_template = "extended_se_K2"
    template_model = env["account.chart.template"]
    companies = env["res.company"].search([])
    for company in companies:
        current = company.chart_template or False
        if current not in _EMPTY_CHARTS:
            _logger.info(
                "l10n_se_account_k2: %s already has chart %s, skipping K2 load",
                company.display_name,
                current,
            )
            continue
        try:
            template_model.try_loading(chart_template, company)
            _logger.info(
                "l10n_se_account_k2: loaded %s for %s",
                chart_template,
                company.display_name,
            )
        except (UserError, Exception) as exc:  # noqa: BLE001 - one company must not abort install
            _logger.warning(
                "l10n_se_account_k2: could not load %s for %s: %s",
                chart_template,
                company.display_name,
                exc,
            )
