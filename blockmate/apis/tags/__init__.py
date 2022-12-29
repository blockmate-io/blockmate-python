# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from blockmate.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    ACCOUNT_PROVIDER_INFO = "Account provider info"
    ADDRESS_NAME_AND_CATEGORY_INFO = "Address name and category info"
    AGGREGATED_INFO = "Aggregated info"
    ANALYTICS = "Analytics"
    AUTHENTICATION = "Authentication"
    ENS = "ENS"
    EXCHANGE_RATE_INFO = "Exchange rate info"
    RISK_INFO = "Risk info"
    USER_MANAGEMENT = "User management"
