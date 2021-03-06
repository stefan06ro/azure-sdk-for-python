# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class OAuth2Permission(Model):
    """Represents an OAuth 2.0 delegated permission scope. The specified OAuth 2.0
    delegated permission scopes may be requested by client applications
    (through the requiredResourceAccess collection on the Application object)
    when calling a resource application. The oauth2Permissions property of the
    ServicePrincipal entity and of the Application entity is a collection of
    OAuth2Permission.

    :param admin_consent_description: Permission help text that appears in the
     admin consent and app assignment experiences.
    :type admin_consent_description: str
    :param admin_consent_display_name: Display name for the permission that
     appears in the admin consent and app assignment experiences.
    :type admin_consent_display_name: str
    :param id: Unique scope permission identifier inside the oauth2Permissions
     collection.
    :type id: str
    :param is_enabled: When creating or updating a permission, this property
     must be set to true (which is the default). To delete a permission, this
     property must first be set to false. At that point, in a subsequent call,
     the permission may be removed.
    :type is_enabled: bool
    :param type: Specifies whether this scope permission can be consented to
     by an end user, or whether it is a tenant-wide permission that must be
     consented to by a Company Administrator. Possible values are "User" or
     "Admin".
    :type type: str
    :param user_consent_description: Permission help text that appears in the
     end user consent experience.
    :type user_consent_description: str
    :param user_consent_display_name: Display name for the permission that
     appears in the end user consent experience.
    :type user_consent_display_name: str
    :param value: The value of the scope claim that the resource application
     should expect in the OAuth 2.0 access token.
    :type value: str
    """

    _attribute_map = {
        'admin_consent_description': {'key': 'adminConsentDescription', 'type': 'str'},
        'admin_consent_display_name': {'key': 'adminConsentDisplayName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'is_enabled': {'key': 'isEnabled', 'type': 'bool'},
        'type': {'key': 'type', 'type': 'str'},
        'user_consent_description': {'key': 'userConsentDescription', 'type': 'str'},
        'user_consent_display_name': {'key': 'userConsentDisplayName', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(self, *, admin_consent_description: str=None, admin_consent_display_name: str=None, id: str=None, is_enabled: bool=None, type: str=None, user_consent_description: str=None, user_consent_display_name: str=None, value: str=None, **kwargs) -> None:
        super(OAuth2Permission, self).__init__(**kwargs)
        self.admin_consent_description = admin_consent_description
        self.admin_consent_display_name = admin_consent_display_name
        self.id = id
        self.is_enabled = is_enabled
        self.type = type
        self.user_consent_description = user_consent_description
        self.user_consent_display_name = user_consent_display_name
        self.value = value
