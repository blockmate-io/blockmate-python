import typing_extensions

from blockmate.paths import PathValues
from blockmate.apis.paths.v1_auth import V1Auth
from blockmate.apis.paths.v1_auth_developer import V1AuthDeveloper
from blockmate.apis.paths.v1_users import V1Users
from blockmate.apis.paths.v1_users_id import V1UsersId
from blockmate.apis.paths.v1_users_id_auth import V1UsersIdAuth
from blockmate.apis.paths.v1_account_provider_connect import V1AccountProviderConnect
from blockmate.apis.paths.v1_account_provider_account_account_id import V1AccountProviderAccountAccountId
from blockmate.apis.paths.v1_aggregate_account_providers import V1AggregateAccountProviders
from blockmate.apis.paths.v1_aggregate_account_provider_hints import V1AggregateAccountProviderHints
from blockmate.apis.paths.v1_aggregate_accounts import V1AggregateAccounts
from blockmate.apis.paths.v1_aggregate_balance import V1AggregateBalance
from blockmate.apis.paths.v1_aggregate_transactions import V1AggregateTransactions
from blockmate.apis.paths.v1_aggregate_nft_metadata import V1AggregateNftMetadata
from blockmate.apis.paths.v1_risk_score import V1RiskScore
from blockmate.apis.paths.v1_risk_score_details import V1RiskScoreDetails
from blockmate.apis.paths.v1_risk_score_details_case_id import V1RiskScoreDetailsCaseId
from blockmate.apis.paths.v1_risk_transaction_score import V1RiskTransactionScore
from blockmate.apis.paths.v1_risk_transaction_score_details import V1RiskTransactionScoreDetails
from blockmate.apis.paths.v1_risk_transaction_score_details_case_id import V1RiskTransactionScoreDetailsCaseId
from blockmate.apis.paths.v1_exchangerate_current import V1ExchangerateCurrent
from blockmate.apis.paths.v1_exchangerate_history import V1ExchangerateHistory
from blockmate.apis.paths.v1_addressname_simple import V1AddressnameSimple
from blockmate.apis.paths.v1_addressname_multi import V1AddressnameMulti
from blockmate.apis.paths.v1_ens_address_from_domain import V1EnsAddressFromDomain
from blockmate.apis.paths.v1_ens_domain_from_address import V1EnsDomainFromAddress
from blockmate.apis.paths.v1_analytics_project_stats import V1AnalyticsProjectStats
from blockmate.apis.paths.v1_analytics_user_stats import V1AnalyticsUserStats
from blockmate.apis.paths.v1_analytics_account_provider_stats import V1AnalyticsAccountProviderStats
from blockmate.apis.paths.v1_analytics_account_provider_account_account_id_stats import V1AnalyticsAccountProviderAccountAccountIdStats

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V1_AUTH: V1Auth,
        PathValues.V1_AUTH_DEVELOPER: V1AuthDeveloper,
        PathValues.V1_USERS: V1Users,
        PathValues.V1_USERS_ID: V1UsersId,
        PathValues.V1_USERS_ID_AUTH: V1UsersIdAuth,
        PathValues.V1_ACCOUNT_PROVIDER_CONNECT: V1AccountProviderConnect,
        PathValues.V1_ACCOUNT_PROVIDER_ACCOUNT_ACCOUNT_ID: V1AccountProviderAccountAccountId,
        PathValues.V1_AGGREGATE_ACCOUNT_PROVIDERS: V1AggregateAccountProviders,
        PathValues.V1_AGGREGATE_ACCOUNT_PROVIDER_HINTS: V1AggregateAccountProviderHints,
        PathValues.V1_AGGREGATE_ACCOUNTS: V1AggregateAccounts,
        PathValues.V1_AGGREGATE_BALANCE: V1AggregateBalance,
        PathValues.V1_AGGREGATE_TRANSACTIONS: V1AggregateTransactions,
        PathValues.V1_AGGREGATE_NFT_METADATA: V1AggregateNftMetadata,
        PathValues.V1_RISK_SCORE: V1RiskScore,
        PathValues.V1_RISK_SCORE_DETAILS: V1RiskScoreDetails,
        PathValues.V1_RISK_SCORE_DETAILS_CASE_ID: V1RiskScoreDetailsCaseId,
        PathValues.V1_RISK_TRANSACTION_SCORE: V1RiskTransactionScore,
        PathValues.V1_RISK_TRANSACTION_SCORE_DETAILS: V1RiskTransactionScoreDetails,
        PathValues.V1_RISK_TRANSACTION_SCORE_DETAILS_CASE_ID: V1RiskTransactionScoreDetailsCaseId,
        PathValues.V1_EXCHANGERATE_CURRENT: V1ExchangerateCurrent,
        PathValues.V1_EXCHANGERATE_HISTORY: V1ExchangerateHistory,
        PathValues.V1_ADDRESSNAME_SIMPLE: V1AddressnameSimple,
        PathValues.V1_ADDRESSNAME_MULTI: V1AddressnameMulti,
        PathValues.V1_ENS_ADDRESS_FROM_DOMAIN: V1EnsAddressFromDomain,
        PathValues.V1_ENS_DOMAIN_FROM_ADDRESS: V1EnsDomainFromAddress,
        PathValues.V1_ANALYTICS_PROJECT_STATS: V1AnalyticsProjectStats,
        PathValues.V1_ANALYTICS_USER_STATS: V1AnalyticsUserStats,
        PathValues.V1_ANALYTICS_ACCOUNT_PROVIDER_STATS: V1AnalyticsAccountProviderStats,
        PathValues.V1_ANALYTICS_ACCOUNT_PROVIDER_ACCOUNT_ACCOUNT_ID_STATS: V1AnalyticsAccountProviderAccountAccountIdStats,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V1_AUTH: V1Auth,
        PathValues.V1_AUTH_DEVELOPER: V1AuthDeveloper,
        PathValues.V1_USERS: V1Users,
        PathValues.V1_USERS_ID: V1UsersId,
        PathValues.V1_USERS_ID_AUTH: V1UsersIdAuth,
        PathValues.V1_ACCOUNT_PROVIDER_CONNECT: V1AccountProviderConnect,
        PathValues.V1_ACCOUNT_PROVIDER_ACCOUNT_ACCOUNT_ID: V1AccountProviderAccountAccountId,
        PathValues.V1_AGGREGATE_ACCOUNT_PROVIDERS: V1AggregateAccountProviders,
        PathValues.V1_AGGREGATE_ACCOUNT_PROVIDER_HINTS: V1AggregateAccountProviderHints,
        PathValues.V1_AGGREGATE_ACCOUNTS: V1AggregateAccounts,
        PathValues.V1_AGGREGATE_BALANCE: V1AggregateBalance,
        PathValues.V1_AGGREGATE_TRANSACTIONS: V1AggregateTransactions,
        PathValues.V1_AGGREGATE_NFT_METADATA: V1AggregateNftMetadata,
        PathValues.V1_RISK_SCORE: V1RiskScore,
        PathValues.V1_RISK_SCORE_DETAILS: V1RiskScoreDetails,
        PathValues.V1_RISK_SCORE_DETAILS_CASE_ID: V1RiskScoreDetailsCaseId,
        PathValues.V1_RISK_TRANSACTION_SCORE: V1RiskTransactionScore,
        PathValues.V1_RISK_TRANSACTION_SCORE_DETAILS: V1RiskTransactionScoreDetails,
        PathValues.V1_RISK_TRANSACTION_SCORE_DETAILS_CASE_ID: V1RiskTransactionScoreDetailsCaseId,
        PathValues.V1_EXCHANGERATE_CURRENT: V1ExchangerateCurrent,
        PathValues.V1_EXCHANGERATE_HISTORY: V1ExchangerateHistory,
        PathValues.V1_ADDRESSNAME_SIMPLE: V1AddressnameSimple,
        PathValues.V1_ADDRESSNAME_MULTI: V1AddressnameMulti,
        PathValues.V1_ENS_ADDRESS_FROM_DOMAIN: V1EnsAddressFromDomain,
        PathValues.V1_ENS_DOMAIN_FROM_ADDRESS: V1EnsDomainFromAddress,
        PathValues.V1_ANALYTICS_PROJECT_STATS: V1AnalyticsProjectStats,
        PathValues.V1_ANALYTICS_USER_STATS: V1AnalyticsUserStats,
        PathValues.V1_ANALYTICS_ACCOUNT_PROVIDER_STATS: V1AnalyticsAccountProviderStats,
        PathValues.V1_ANALYTICS_ACCOUNT_PROVIDER_ACCOUNT_ACCOUNT_ID_STATS: V1AnalyticsAccountProviderAccountAccountIdStats,
    }
)
