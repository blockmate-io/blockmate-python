# coding: utf-8

"""
    Blockmate

    Blockmate API OpenAPI documentation  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""

from blockmate.paths.v1_aggregate_account_provider_hints.get import AccountProviderHintsList
from blockmate.paths.v1_aggregate_account_providers.get import AccountProvidersList
from blockmate.paths.v1_aggregate_accounts.get import Accounts
from blockmate.paths.v1_aggregate_balance.get import Balance
from blockmate.paths.v1_aggregate_transactions.get import Transactions


class AggregatedInfoApi(
    AccountProviderHintsList,
    AccountProvidersList,
    Accounts,
    Balance,
    Transactions,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
