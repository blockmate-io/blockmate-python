# coding: utf-8

"""
    Blockmate

    Blockmate API OpenAPI documentation  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""

from blockmate.paths.v1_auth_developer.get import UserApiAuthenticateDeveloper
from blockmate.paths.v1_auth.get import UserApiAuthenticateProject


class AuthenticationApi(
    UserApiAuthenticateDeveloper,
    UserApiAuthenticateProject,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass