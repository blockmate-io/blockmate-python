import typing_extensions

from blockmate.apis.tags import TagValues
from blockmate.apis.tags.address_name_and_category_info_api import AddressNameAndCategoryInfoApi
from blockmate.apis.tags.aggregated_info_api import AggregatedInfoApi
from blockmate.apis.tags.analytics_api import AnalyticsApi
from blockmate.apis.tags.authentication_api import AuthenticationApi
from blockmate.apis.tags.ens_api import ENSApi
from blockmate.apis.tags.exchange_rate_info_api import ExchangeRateInfoApi
from blockmate.apis.tags.risk_info_api import RiskInfoApi
from blockmate.apis.tags.user_account_management_api import UserAccountManagementApi
from blockmate.apis.tags.user_management_api import UserManagementApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ADDRESS_NAME_AND_CATEGORY_INFO: AddressNameAndCategoryInfoApi,
        TagValues.AGGREGATED_INFO: AggregatedInfoApi,
        TagValues.ANALYTICS: AnalyticsApi,
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.ENS: ENSApi,
        TagValues.EXCHANGE_RATE_INFO: ExchangeRateInfoApi,
        TagValues.RISK_INFO: RiskInfoApi,
        TagValues.USER_ACCOUNT_MANAGEMENT: UserAccountManagementApi,
        TagValues.USER_MANAGEMENT: UserManagementApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ADDRESS_NAME_AND_CATEGORY_INFO: AddressNameAndCategoryInfoApi,
        TagValues.AGGREGATED_INFO: AggregatedInfoApi,
        TagValues.ANALYTICS: AnalyticsApi,
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.ENS: ENSApi,
        TagValues.EXCHANGE_RATE_INFO: ExchangeRateInfoApi,
        TagValues.RISK_INFO: RiskInfoApi,
        TagValues.USER_ACCOUNT_MANAGEMENT: UserAccountManagementApi,
        TagValues.USER_MANAGEMENT: UserManagementApi,
    }
)
