# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from blockmate.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V1_AUTH = "/v1/auth"
    V1_AUTH_DEVELOPER = "/v1/auth/developer"
    V1_USERS = "/v1/users"
    V1_USERS_ID = "/v1/users/{id}"
    V1_USERS_ID_AUTH = "/v1/users/{id}/auth"
    V1_AGGREGATE_ACCOUNT_PROVIDERS = "/v1/aggregate/account_providers"
    V1_AGGREGATE_ACCOUNT_PROVIDER_HINTS = "/v1/aggregate/account_provider_hints"
    V1_AGGREGATE_ACCOUNTS = "/v1/aggregate/accounts"
    V1_AGGREGATE_BALANCE = "/v1/aggregate/balance"
    V1_AGGREGATE_TRANSACTIONS = "/v1/aggregate/transactions"
    V1_AGGREGATE_NFT_METADATA = "/v1/aggregate/nft_metadata"
    V1_ACCOUNT_PROVIDER_CONNECT = "/v1/{account_provider}/connect"
    V1_ACCOUNT_PROVIDER_ACCOUNT_ACCOUNT_ID = "/v1/{account_provider}/account/{account_id}"
    V1_RISK_SCORE = "/v1/risk/score"
    V1_RISK_SCORE_DETAILS = "/v1/risk/score/details"
    V1_RISK_SCORE_DETAILS_CASE_ID = "/v1/risk/score/details/{case_id}"
    V1_RISK_TRANSACTION_SCORE = "/v1/risk/transaction/score"
    V1_RISK_TRANSACTION_SCORE_DETAILS = "/v1/risk/transaction/score/details"
    V1_RISK_TRANSACTION_SCORE_DETAILS_CASE_ID = "/v1/risk/transaction/score/details/{case_id}"
    V1_EXCHANGERATE_CURRENT = "/v1/exchangerate/current"
    V1_EXCHANGERATE_HISTORY = "/v1/exchangerate/history"
    V1_ADDRESSNAME_SIMPLE = "/v1/addressname/simple"
