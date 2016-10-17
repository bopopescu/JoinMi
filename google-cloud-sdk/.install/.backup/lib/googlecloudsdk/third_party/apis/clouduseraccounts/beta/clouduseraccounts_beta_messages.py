"""Generated message classes for clouduseraccounts version beta.

Creates and manages users and groups for accessing Google Compute Engine
virtual machines.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from apitools.base.protorpclite import messages as _messages


package = 'clouduseraccounts'


class AuthorizedKeysView(_messages.Message):
  """A list of authorized public keys for a user account.

  Fields:
    keys: [Output Only] The list of authorized public keys in SSH format.
    sudoer: [Output Only] Whether the user has the ability to elevate on the
      instance that requested the authorized keys.
  """

  keys = _messages.StringField(1, repeated=True)
  sudoer = _messages.BooleanField(2)


class ClouduseraccountsGlobalAccountsOperationsDeleteRequest(_messages.Message):
  """A ClouduseraccountsGlobalAccountsOperationsDeleteRequest object.

  Fields:
    operation: Name of the Operations resource to delete.
    project: Project ID for this request.
  """

  operation = _messages.StringField(1, required=True)
  project = _messages.StringField(2, required=True)


class ClouduseraccountsGlobalAccountsOperationsDeleteResponse(_messages.Message):
  """An empty ClouduseraccountsGlobalAccountsOperationsDelete response."""


class ClouduseraccountsGlobalAccountsOperationsGetRequest(_messages.Message):
  """A ClouduseraccountsGlobalAccountsOperationsGetRequest object.

  Fields:
    operation: Name of the Operations resource to return.
    project: Project ID for this request.
  """

  operation = _messages.StringField(1, required=True)
  project = _messages.StringField(2, required=True)


class ClouduseraccountsGlobalAccountsOperationsListRequest(_messages.Message):
  """A ClouduseraccountsGlobalAccountsOperationsListRequest object.

  Fields:
    filter: Sets a filter expression for filtering listed resources, in the
      form filter={expression}. Your {expression} must be in the format:
      field_name comparison_string literal_string.  The field_name is the name
      of the field you want to compare. Only atomic field types are supported
      (string, number, boolean). The comparison_string must be either eq
      (equals) or ne (not equals). The literal_string is the string value to
      filter to. The literal value must be valid for the type of field you are
      filtering by (string, number, boolean). For string fields, the literal
      value is interpreted as a regular expression using RE2 syntax. The
      literal value must match the entire field.  For example, to filter for
      instances that do not have a name of example-instance, you would use
      filter=name ne example-instance.  You can filter on nested fields. For
      example, you could filter on instances that have set the
      scheduling.automaticRestart field to true. Use filtering on nested
      fields to take advantage of labels to organize and search for results
      based on label values.  To filter on multiple expressions, provide each
      separate expression within parentheses. For example,
      (scheduling.automaticRestart eq true) (zone eq us-central1-f). Multiple
      expressions are treated as AND expressions, meaning that resources must
      match all expressions to pass the filters.
    maxResults: The maximum number of results per page that should be
      returned. If the number of available results is larger than maxResults,
      Compute Engine returns a nextPageToken that can be used to get the next
      page of results in subsequent list requests.
    orderBy: Sorts list results by a certain order. By default, results are
      returned in alphanumerical order based on the resource name.  You can
      also sort results in descending order based on the creation timestamp
      using orderBy="creationTimestamp desc". This sorts results based on the
      creationTimestamp field in reverse chronological order (newest result
      first). Use this to sort resources like operations so that the newest
      operation is returned first.  Currently, only sorting by name or
      creationTimestamp desc is supported.
    pageToken: Specifies a page token to use. Set pageToken to the
      nextPageToken returned by a previous list request to get the next page
      of results.
    project: Project ID for this request.
  """

  filter = _messages.StringField(1)
  maxResults = _messages.IntegerField(2, variant=_messages.Variant.UINT32, default=500)
  orderBy = _messages.StringField(3)
  pageToken = _messages.StringField(4)
  project = _messages.StringField(5, required=True)


class ClouduseraccountsGroupsAddMemberRequest(_messages.Message):
  """A ClouduseraccountsGroupsAddMemberRequest object.

  Fields:
    groupName: Name of the group for this request.
    groupsAddMemberRequest: A GroupsAddMemberRequest resource to be passed as
      the request body.
    project: Project ID for this request.
  """

  groupName = _messages.StringField(1, required=True)
  groupsAddMemberRequest = _messages.MessageField('GroupsAddMemberRequest', 2)
  project = _messages.StringField(3, required=True)


class ClouduseraccountsGroupsDeleteRequest(_messages.Message):
  """A ClouduseraccountsGroupsDeleteRequest object.

  Fields:
    groupName: Name of the Group resource to delete.
    project: Project ID for this request.
  """

  groupName = _messages.StringField(1, required=True)
  project = _messages.StringField(2, required=True)


class ClouduseraccountsGroupsGetRequest(_messages.Message):
  """A ClouduseraccountsGroupsGetRequest object.

  Fields:
    groupName: Name of the Group resource to return.
    project: Project ID for this request.
  """

  groupName = _messages.StringField(1, required=True)
  project = _messages.StringField(2, required=True)


class ClouduseraccountsGroupsInsertRequest(_messages.Message):
  """A ClouduseraccountsGroupsInsertRequest object.

  Fields:
    group: A Group resource to be passed as the request body.
    project: Project ID for this request.
  """

  group = _messages.MessageField('Group', 1)
  project = _messages.StringField(2, required=True)


class ClouduseraccountsGroupsListRequest(_messages.Message):
  """A ClouduseraccountsGroupsListRequest object.

  Fields:
    filter: Sets a filter expression for filtering listed resources, in the
      form filter={expression}. Your {expression} must be in the format:
      field_name comparison_string literal_string.  The field_name is the name
      of the field you want to compare. Only atomic field types are supported
      (string, number, boolean). The comparison_string must be either eq
      (equals) or ne (not equals). The literal_string is the string value to
      filter to. The literal value must be valid for the type of field you are
      filtering by (string, number, boolean). For string fields, the literal
      value is interpreted as a regular expression using RE2 syntax. The
      literal value must match the entire field.  For example, to filter for
      instances that do not have a name of example-instance, you would use
      filter=name ne example-instance.  You can filter on nested fields. For
      example, you could filter on instances that have set the
      scheduling.automaticRestart field to true. Use filtering on nested
      fields to take advantage of labels to organize and search for results
      based on label values.  To filter on multiple expressions, provide each
      separate expression within parentheses. For example,
      (scheduling.automaticRestart eq true) (zone eq us-central1-f). Multiple
      expressions are treated as AND expressions, meaning that resources must
      match all expressions to pass the filters.
    maxResults: The maximum number of results per page that should be
      returned. If the number of available results is larger than maxResults,
      Compute Engine returns a nextPageToken that can be used to get the next
      page of results in subsequent list requests.
    orderBy: Sorts list results by a certain order. By default, results are
      returned in alphanumerical order based on the resource name.  You can
      also sort results in descending order based on the creation timestamp
      using orderBy="creationTimestamp desc". This sorts results based on the
      creationTimestamp field in reverse chronological order (newest result
      first). Use this to sort resources like operations so that the newest
      operation is returned first.  Currently, only sorting by name or
      creationTimestamp desc is supported.
    pageToken: Specifies a page token to use. Set pageToken to the
      nextPageToken returned by a previous list request to get the next page
      of results.
    project: Project ID for this request.
  """

  filter = _messages.StringField(1)
  maxResults = _messages.IntegerField(2, variant=_messages.Variant.UINT32, default=500)
  orderBy = _messages.StringField(3)
  pageToken = _messages.StringField(4)
  project = _messages.StringField(5, required=True)


class ClouduseraccountsGroupsRemoveMemberRequest(_messages.Message):
  """A ClouduseraccountsGroupsRemoveMemberRequest object.

  Fields:
    groupName: Name of the group for this request.
    groupsRemoveMemberRequest: A GroupsRemoveMemberRequest resource to be
      passed as the request body.
    project: Project ID for this request.
  """

  groupName = _messages.StringField(1, required=True)
  groupsRemoveMemberRequest = _messages.MessageField('GroupsRemoveMemberRequest', 2)
  project = _messages.StringField(3, required=True)


class ClouduseraccountsLinuxGetAuthorizedKeysViewRequest(_messages.Message):
  """A ClouduseraccountsLinuxGetAuthorizedKeysViewRequest object.

  Fields:
    instance: The fully-qualified URL of the virtual machine requesting the
      view.
    login: Whether the view was requested as part of a user-initiated login.
    project: Project ID for this request.
    user: The user account for which you want to get a list of authorized
      public keys.
    zone: Name of the zone for this request.
  """

  instance = _messages.StringField(1, required=True)
  login = _messages.BooleanField(2)
  project = _messages.StringField(3, required=True)
  user = _messages.StringField(4, required=True)
  zone = _messages.StringField(5, required=True)


class ClouduseraccountsLinuxGetLinuxAccountViewsRequest(_messages.Message):
  """A ClouduseraccountsLinuxGetLinuxAccountViewsRequest object.

  Fields:
    filter: Sets a filter expression for filtering listed resources, in the
      form filter={expression}. Your {expression} must be in the format:
      field_name comparison_string literal_string.  The field_name is the name
      of the field you want to compare. Only atomic field types are supported
      (string, number, boolean). The comparison_string must be either eq
      (equals) or ne (not equals). The literal_string is the string value to
      filter to. The literal value must be valid for the type of field you are
      filtering by (string, number, boolean). For string fields, the literal
      value is interpreted as a regular expression using RE2 syntax. The
      literal value must match the entire field.  For example, to filter for
      instances that do not have a name of example-instance, you would use
      filter=name ne example-instance.  You can filter on nested fields. For
      example, you could filter on instances that have set the
      scheduling.automaticRestart field to true. Use filtering on nested
      fields to take advantage of labels to organize and search for results
      based on label values.  To filter on multiple expressions, provide each
      separate expression within parentheses. For example,
      (scheduling.automaticRestart eq true) (zone eq us-central1-f). Multiple
      expressions are treated as AND expressions, meaning that resources must
      match all expressions to pass the filters.
    instance: The fully-qualified URL of the virtual machine requesting the
      views.
    maxResults: The maximum number of results per page that should be
      returned. If the number of available results is larger than maxResults,
      Compute Engine returns a nextPageToken that can be used to get the next
      page of results in subsequent list requests.
    orderBy: Sorts list results by a certain order. By default, results are
      returned in alphanumerical order based on the resource name.  You can
      also sort results in descending order based on the creation timestamp
      using orderBy="creationTimestamp desc". This sorts results based on the
      creationTimestamp field in reverse chronological order (newest result
      first). Use this to sort resources like operations so that the newest
      operation is returned first.  Currently, only sorting by name or
      creationTimestamp desc is supported.
    pageToken: Specifies a page token to use. Set pageToken to the
      nextPageToken returned by a previous list request to get the next page
      of results.
    project: Project ID for this request.
    zone: Name of the zone for this request.
  """

  filter = _messages.StringField(1)
  instance = _messages.StringField(2, required=True)
  maxResults = _messages.IntegerField(3, variant=_messages.Variant.UINT32, default=500)
  orderBy = _messages.StringField(4)
  pageToken = _messages.StringField(5)
  project = _messages.StringField(6, required=True)
  zone = _messages.StringField(7, required=True)


class ClouduseraccountsUsersAddPublicKeyRequest(_messages.Message):
  """A ClouduseraccountsUsersAddPublicKeyRequest object.

  Fields:
    project: Project ID for this request.
    publicKey: A PublicKey resource to be passed as the request body.
    user: Name of the user for this request.
  """

  project = _messages.StringField(1, required=True)
  publicKey = _messages.MessageField('PublicKey', 2)
  user = _messages.StringField(3, required=True)


class ClouduseraccountsUsersDeleteRequest(_messages.Message):
  """A ClouduseraccountsUsersDeleteRequest object.

  Fields:
    project: Project ID for this request.
    user: Name of the user resource to delete.
  """

  project = _messages.StringField(1, required=True)
  user = _messages.StringField(2, required=True)


class ClouduseraccountsUsersGetRequest(_messages.Message):
  """A ClouduseraccountsUsersGetRequest object.

  Fields:
    project: Project ID for this request.
    user: Name of the user resource to return.
  """

  project = _messages.StringField(1, required=True)
  user = _messages.StringField(2, required=True)


class ClouduseraccountsUsersInsertRequest(_messages.Message):
  """A ClouduseraccountsUsersInsertRequest object.

  Fields:
    project: Project ID for this request.
    user: A User resource to be passed as the request body.
  """

  project = _messages.StringField(1, required=True)
  user = _messages.MessageField('User', 2)


class ClouduseraccountsUsersListRequest(_messages.Message):
  """A ClouduseraccountsUsersListRequest object.

  Fields:
    filter: Sets a filter expression for filtering listed resources, in the
      form filter={expression}. Your {expression} must be in the format:
      field_name comparison_string literal_string.  The field_name is the name
      of the field you want to compare. Only atomic field types are supported
      (string, number, boolean). The comparison_string must be either eq
      (equals) or ne (not equals). The literal_string is the string value to
      filter to. The literal value must be valid for the type of field you are
      filtering by (string, number, boolean). For string fields, the literal
      value is interpreted as a regular expression using RE2 syntax. The
      literal value must match the entire field.  For example, to filter for
      instances that do not have a name of example-instance, you would use
      filter=name ne example-instance.  You can filter on nested fields. For
      example, you could filter on instances that have set the
      scheduling.automaticRestart field to true. Use filtering on nested
      fields to take advantage of labels to organize and search for results
      based on label values.  To filter on multiple expressions, provide each
      separate expression within parentheses. For example,
      (scheduling.automaticRestart eq true) (zone eq us-central1-f). Multiple
      expressions are treated as AND expressions, meaning that resources must
      match all expressions to pass the filters.
    maxResults: The maximum number of results per page that should be
      returned. If the number of available results is larger than maxResults,
      Compute Engine returns a nextPageToken that can be used to get the next
      page of results in subsequent list requests.
    orderBy: Sorts list results by a certain order. By default, results are
      returned in alphanumerical order based on the resource name.  You can
      also sort results in descending order based on the creation timestamp
      using orderBy="creationTimestamp desc". This sorts results based on the
      creationTimestamp field in reverse chronological order (newest result
      first). Use this to sort resources like operations so that the newest
      operation is returned first.  Currently, only sorting by name or
      creationTimestamp desc is supported.
    pageToken: Specifies a page token to use. Set pageToken to the
      nextPageToken returned by a previous list request to get the next page
      of results.
    project: Project ID for this request.
  """

  filter = _messages.StringField(1)
  maxResults = _messages.IntegerField(2, variant=_messages.Variant.UINT32, default=500)
  orderBy = _messages.StringField(3)
  pageToken = _messages.StringField(4)
  project = _messages.StringField(5, required=True)


class ClouduseraccountsUsersRemovePublicKeyRequest(_messages.Message):
  """A ClouduseraccountsUsersRemovePublicKeyRequest object.

  Fields:
    fingerprint: The fingerprint of the public key to delete. Public keys are
      identified by their fingerprint, which is defined by RFC4716 to be the
      MD5 digest of the public key.
    project: Project ID for this request.
    user: Name of the user for this request.
  """

  fingerprint = _messages.StringField(1, required=True)
  project = _messages.StringField(2, required=True)
  user = _messages.StringField(3, required=True)


class Group(_messages.Message):
  """A Group resource.

  Fields:
    creationTimestamp: [Output Only] Creation timestamp in RFC3339 text
      format.
    description: An optional textual description of the resource; provided by
      the client when the resource is created.
    id: [Output Only] Unique identifier for the resource; defined by the
      server.
    kind: [Output Only] Type of the resource. Always clouduseraccounts#group
      for groups.
    members: [Output Only] A list of URLs to User resources who belong to the
      group. Users may only be members of groups in the same project.
    name: Name of the resource; provided by the client when the resource is
      created.
    selfLink: [Output Only] Server defined URL for the resource.
  """

  creationTimestamp = _messages.StringField(1)
  description = _messages.StringField(2)
  id = _messages.IntegerField(3, variant=_messages.Variant.UINT64)
  kind = _messages.StringField(4, default=u'clouduseraccounts#group')
  members = _messages.StringField(5, repeated=True)
  name = _messages.StringField(6)
  selfLink = _messages.StringField(7)


class GroupList(_messages.Message):
  """A GroupList object.

  Fields:
    id: [Output Only] Unique identifier for the resource; defined by the
      server.
    items: [Output Only] A list of Group resources.
    kind: [Output Only] Type of resource. Always clouduseraccounts#groupList
      for lists of groups.
    nextPageToken: [Output Only] A token used to continue a truncated list
      request.
    selfLink: [Output Only] Server defined URL for this resource.
  """

  id = _messages.StringField(1)
  items = _messages.MessageField('Group', 2, repeated=True)
  kind = _messages.StringField(3, default=u'clouduseraccounts#groupList')
  nextPageToken = _messages.StringField(4)
  selfLink = _messages.StringField(5)


class GroupsAddMemberRequest(_messages.Message):
  """A GroupsAddMemberRequest object.

  Fields:
    users: Fully-qualified URLs of the User resources to add.
  """

  users = _messages.StringField(1, repeated=True)


class GroupsRemoveMemberRequest(_messages.Message):
  """A GroupsRemoveMemberRequest object.

  Fields:
    users: Fully-qualified URLs of the User resources to remove.
  """

  users = _messages.StringField(1, repeated=True)


class LinuxAccountViews(_messages.Message):
  """A list of all Linux accounts for this project. This API is only used by
  Compute Engine virtual machines to get information about user accounts for a
  project or instance. Linux resources are read-only views into users and
  groups managed by the Compute Engine Accounts API.

  Fields:
    groupViews: [Output Only] A list of all groups within a project.
    kind: [Output Only] Type of the resource. Always
      clouduseraccounts#linuxAccountViews for Linux resources.
    userViews: [Output Only] A list of all users within a project.
  """

  groupViews = _messages.MessageField('LinuxGroupView', 1, repeated=True)
  kind = _messages.StringField(2, default=u'clouduseraccounts#linuxAccountViews')
  userViews = _messages.MessageField('LinuxUserView', 3, repeated=True)


class LinuxGetAuthorizedKeysViewResponse(_messages.Message):
  """A LinuxGetAuthorizedKeysViewResponse object.

  Fields:
    resource: [Output Only] A list of authorized public keys for a user.
  """

  resource = _messages.MessageField('AuthorizedKeysView', 1)


class LinuxGetLinuxAccountViewsResponse(_messages.Message):
  """A LinuxGetLinuxAccountViewsResponse object.

  Fields:
    resource: [Output Only] A list of authorized user accounts and groups.
  """

  resource = _messages.MessageField('LinuxAccountViews', 1)


class LinuxGroupView(_messages.Message):
  """A detailed view of a Linux group.

  Fields:
    gid: [Output Only] The Group ID.
    groupName: [Output Only] Group name.
    members: [Output Only] List of user accounts that belong to the group.
  """

  gid = _messages.IntegerField(1, variant=_messages.Variant.UINT32)
  groupName = _messages.StringField(2)
  members = _messages.StringField(3, repeated=True)


class LinuxUserView(_messages.Message):
  """A detailed view of a Linux user account.

  Fields:
    gecos: [Output Only] The GECOS (user information) entry for this account.
    gid: [Output Only] User's default group ID.
    homeDirectory: [Output Only] The path to the home directory for this
      account.
    shell: [Output Only] The path to the login shell for this account.
    uid: [Output Only] User ID.
    username: [Output Only] The username of the account.
  """

  gecos = _messages.StringField(1)
  gid = _messages.IntegerField(2, variant=_messages.Variant.UINT32)
  homeDirectory = _messages.StringField(3)
  shell = _messages.StringField(4)
  uid = _messages.IntegerField(5, variant=_messages.Variant.UINT32)
  username = _messages.StringField(6)


class Operation(_messages.Message):
  """An Operation resource, used to manage asynchronous API requests.

  Enums:
    StatusValueValuesEnum: [Output Only] The status of the operation, which
      can be one of the following: PENDING, RUNNING, or DONE.

  Messages:
    ErrorValue: [Output Only] If errors are generated during processing of the
      operation, this field will be populated.
    WarningsValueListEntry: A WarningsValueListEntry object.

  Fields:
    clientOperationId: [Output Only] Reserved for future use.
    creationTimestamp: [Output Only] Creation timestamp in RFC3339 text
      format.
    description: [Output Only] A textual description of the operation, which
      is set when the operation is created.
    endTime: [Output Only] The time that this operation was completed. This
      value is in RFC3339 text format.
    error: [Output Only] If errors are generated during processing of the
      operation, this field will be populated.
    httpErrorMessage: [Output Only] If the operation fails, this field
      contains the HTTP error message that was returned, such as NOT FOUND.
    httpErrorStatusCode: [Output Only] If the operation fails, this field
      contains the HTTP error status code that was returned. For example, a
      404 means the resource was not found.
    id: [Output Only] The unique identifier for the resource. This identifier
      is defined by the server.
    insertTime: [Output Only] The time that this operation was requested. This
      value is in RFC3339 text format.
    kind: [Output Only] Type of the resource. Always compute#operation for
      Operation resources.
    name: [Output Only] Name of the resource.
    operationType: [Output Only] The type of operation, such as insert,
      update, or delete, and so on.
    progress: [Output Only] An optional progress indicator that ranges from 0
      to 100. There is no requirement that this be linear or support any
      granularity of operations. This should not be used to guess when the
      operation will be complete. This number should monotonically increase as
      the operation progresses.
    region: [Output Only] The URL of the region where the operation resides.
      Only available when performing regional operations.
    selfLink: [Output Only] Server-defined URL for the resource.
    startTime: [Output Only] The time that this operation was started by the
      server. This value is in RFC3339 text format.
    status: [Output Only] The status of the operation, which can be one of the
      following: PENDING, RUNNING, or DONE.
    statusMessage: [Output Only] An optional textual description of the
      current status of the operation.
    targetId: [Output Only] The unique target ID, which identifies a specific
      incarnation of the target resource.
    targetLink: [Output Only] The URL of the resource that the operation
      modifies. If creating a persistent disk snapshot, this points to the
      persistent disk that the snapshot was created from.
    user: [Output Only] User who requested the operation, for example:
      user@example.com.
    warnings: [Output Only] If warning messages are generated during
      processing of the operation, this field will be populated.
    zone: [Output Only] The URL of the zone where the operation resides. Only
      available when performing per-zone operations.
  """

  class StatusValueValuesEnum(_messages.Enum):
    """[Output Only] The status of the operation, which can be one of the
    following: PENDING, RUNNING, or DONE.

    Values:
      DONE: <no description>
      PENDING: <no description>
      RUNNING: <no description>
    """
    DONE = 0
    PENDING = 1
    RUNNING = 2

  class ErrorValue(_messages.Message):
    """[Output Only] If errors are generated during processing of the
    operation, this field will be populated.

    Messages:
      ErrorsValueListEntry: A ErrorsValueListEntry object.

    Fields:
      errors: [Output Only] The array of errors encountered while processing
        this operation.
    """

    class ErrorsValueListEntry(_messages.Message):
      """A ErrorsValueListEntry object.

      Fields:
        code: [Output Only] The error type identifier for this error.
        location: [Output Only] Indicates the field in the request that caused
          the error. This property is optional.
        message: [Output Only] An optional, human-readable error message.
      """

      code = _messages.StringField(1)
      location = _messages.StringField(2)
      message = _messages.StringField(3)

    errors = _messages.MessageField('ErrorsValueListEntry', 1, repeated=True)

  class WarningsValueListEntry(_messages.Message):
    """A WarningsValueListEntry object.

    Enums:
      CodeValueValuesEnum: [Output Only] A warning code, if applicable. For
        example, Compute Engine returns NO_RESULTS_ON_PAGE if there are no
        results in the response.

    Messages:
      DataValueListEntry: A DataValueListEntry object.

    Fields:
      code: [Output Only] A warning code, if applicable. For example, Compute
        Engine returns NO_RESULTS_ON_PAGE if there are no results in the
        response.
      data: [Output Only] Metadata about this warning in key: value format.
        For example: "data": [ { "key": "scope", "value": "zones/us-east1-d" }
      message: [Output Only] A human-readable description of the warning code.
    """

    class CodeValueValuesEnum(_messages.Enum):
      """[Output Only] A warning code, if applicable. For example, Compute
      Engine returns NO_RESULTS_ON_PAGE if there are no results in the
      response.

      Values:
        CLEANUP_FAILED: <no description>
        DEPRECATED_RESOURCE_USED: <no description>
        DISK_SIZE_LARGER_THAN_IMAGE_SIZE: <no description>
        FIELD_VALUE_OVERRIDEN: <no description>
        INJECTED_KERNELS_DEPRECATED: <no description>
        NEXT_HOP_ADDRESS_NOT_ASSIGNED: <no description>
        NEXT_HOP_CANNOT_IP_FORWARD: <no description>
        NEXT_HOP_INSTANCE_NOT_FOUND: <no description>
        NEXT_HOP_INSTANCE_NOT_ON_NETWORK: <no description>
        NEXT_HOP_NOT_RUNNING: <no description>
        NOT_CRITICAL_ERROR: <no description>
        NO_RESULTS_ON_PAGE: <no description>
        REQUIRED_TOS_AGREEMENT: <no description>
        RESOURCE_NOT_DELETED: <no description>
        SINGLE_INSTANCE_PROPERTY_TEMPLATE: <no description>
        UNREACHABLE: <no description>
      """
      CLEANUP_FAILED = 0
      DEPRECATED_RESOURCE_USED = 1
      DISK_SIZE_LARGER_THAN_IMAGE_SIZE = 2
      FIELD_VALUE_OVERRIDEN = 3
      INJECTED_KERNELS_DEPRECATED = 4
      NEXT_HOP_ADDRESS_NOT_ASSIGNED = 5
      NEXT_HOP_CANNOT_IP_FORWARD = 6
      NEXT_HOP_INSTANCE_NOT_FOUND = 7
      NEXT_HOP_INSTANCE_NOT_ON_NETWORK = 8
      NEXT_HOP_NOT_RUNNING = 9
      NOT_CRITICAL_ERROR = 10
      NO_RESULTS_ON_PAGE = 11
      REQUIRED_TOS_AGREEMENT = 12
      RESOURCE_NOT_DELETED = 13
      SINGLE_INSTANCE_PROPERTY_TEMPLATE = 14
      UNREACHABLE = 15

    class DataValueListEntry(_messages.Message):
      """A DataValueListEntry object.

      Fields:
        key: [Output Only] A key that provides more detail on the warning
          being returned. For example, for warnings where there are no results
          in a list request for a particular zone, this key might be scope and
          the key value might be the zone name. Other examples might be a key
          indicating a deprecated resource and a suggested replacement, or a
          warning about invalid network settings (for example, if an instance
          attempts to perform IP forwarding but is not enabled for IP
          forwarding).
        value: [Output Only] A warning data value corresponding to the key.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    code = _messages.EnumField('CodeValueValuesEnum', 1)
    data = _messages.MessageField('DataValueListEntry', 2, repeated=True)
    message = _messages.StringField(3)

  clientOperationId = _messages.StringField(1)
  creationTimestamp = _messages.StringField(2)
  description = _messages.StringField(3)
  endTime = _messages.StringField(4)
  error = _messages.MessageField('ErrorValue', 5)
  httpErrorMessage = _messages.StringField(6)
  httpErrorStatusCode = _messages.IntegerField(7, variant=_messages.Variant.INT32)
  id = _messages.IntegerField(8, variant=_messages.Variant.UINT64)
  insertTime = _messages.StringField(9)
  kind = _messages.StringField(10, default=u'clouduseraccounts#operation')
  name = _messages.StringField(11)
  operationType = _messages.StringField(12)
  progress = _messages.IntegerField(13, variant=_messages.Variant.INT32)
  region = _messages.StringField(14)
  selfLink = _messages.StringField(15)
  startTime = _messages.StringField(16)
  status = _messages.EnumField('StatusValueValuesEnum', 17)
  statusMessage = _messages.StringField(18)
  targetId = _messages.IntegerField(19, variant=_messages.Variant.UINT64)
  targetLink = _messages.StringField(20)
  user = _messages.StringField(21)
  warnings = _messages.MessageField('WarningsValueListEntry', 22, repeated=True)
  zone = _messages.StringField(23)


class OperationList(_messages.Message):
  """Contains a list of Operation resources.

  Fields:
    id: [Output Only] The unique identifier for the resource. This identifier
      is defined by the server.
    items: [Output Only] A list of Operation resources.
    kind: [Output Only] Type of resource. Always compute#operations for
      Operations resource.
    nextPageToken: [Output Only] This token allows you to get the next page of
      results for list requests. If the number of results is larger than
      maxResults, use the nextPageToken as a value for the query parameter
      pageToken in the next list request. Subsequent list requests will have
      their own nextPageToken to continue paging through the results.
    selfLink: [Output Only] Server-defined URL for this resource.
  """

  id = _messages.StringField(1)
  items = _messages.MessageField('Operation', 2, repeated=True)
  kind = _messages.StringField(3, default=u'clouduseraccounts#operationList')
  nextPageToken = _messages.StringField(4)
  selfLink = _messages.StringField(5)


class PublicKey(_messages.Message):
  """A public key for authenticating to guests.

  Fields:
    creationTimestamp: [Output Only] Creation timestamp in RFC3339 text
      format.
    description: An optional textual description of the resource; provided by
      the client when the resource is created.
    expirationTimestamp: Optional expiration timestamp. If provided, the
      timestamp must be in RFC3339 text format. If not provided, the public
      key never expires.
    fingerprint: [Output Only] The fingerprint of the key is defined by
      RFC4716 to be the MD5 digest of the public key.
    key: Public key text in SSH format, defined by RFC4253 section 6.6.
  """

  creationTimestamp = _messages.StringField(1)
  description = _messages.StringField(2)
  expirationTimestamp = _messages.StringField(3)
  fingerprint = _messages.StringField(4)
  key = _messages.StringField(5)


class StandardQueryParameters(_messages.Message):
  """Query parameters accepted by all methods.

  Enums:
    AltValueValuesEnum: Data format for the response.

  Fields:
    alt: Data format for the response.
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters. Overrides userIp if both are provided.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    userIp: IP address of the site where the request originates. Use this if
      you want to enforce per-user limits.
  """

  class AltValueValuesEnum(_messages.Enum):
    """Data format for the response.

    Values:
      json: Responses with Content-Type of application/json
    """
    json = 0

  alt = _messages.EnumField('AltValueValuesEnum', 1, default=u'json')
  fields = _messages.StringField(2)
  key = _messages.StringField(3)
  oauth_token = _messages.StringField(4)
  prettyPrint = _messages.BooleanField(5, default=True)
  quotaUser = _messages.StringField(6)
  trace = _messages.StringField(7)
  userIp = _messages.StringField(8)


class User(_messages.Message):
  """A User resource.

  Fields:
    creationTimestamp: [Output Only] Creation timestamp in RFC3339 text
      format.
    description: An optional textual description of the resource; provided by
      the client when the resource is created.
    groups: [Output Only] A list of URLs to Group resources who contain the
      user. Users are only members of groups in the same project.
    id: [Output Only] Unique identifier for the resource; defined by the
      server.
    kind: [Output Only] Type of the resource. Always clouduseraccounts#user
      for users.
    name: Name of the resource; provided by the client when the resource is
      created.
    owner: Email address of account's owner. This account will be validated to
      make sure it exists. The email can belong to any domain, but it must be
      tied to a Google account.
    publicKeys: [Output Only] Public keys that this user may use to login.
    selfLink: [Output Only] Server defined URL for the resource.
  """

  creationTimestamp = _messages.StringField(1)
  description = _messages.StringField(2)
  groups = _messages.StringField(3, repeated=True)
  id = _messages.IntegerField(4, variant=_messages.Variant.UINT64)
  kind = _messages.StringField(5, default=u'clouduseraccounts#user')
  name = _messages.StringField(6)
  owner = _messages.StringField(7)
  publicKeys = _messages.MessageField('PublicKey', 8, repeated=True)
  selfLink = _messages.StringField(9)


class UserList(_messages.Message):
  """A UserList object.

  Fields:
    id: [Output Only] Unique identifier for the resource; defined by the
      server.
    items: [Output Only] A list of User resources.
    kind: [Output Only] Type of resource. Always clouduseraccounts#userList
      for lists of users.
    nextPageToken: [Output Only] A token used to continue a truncated list
      request.
    selfLink: [Output Only] Server defined URL for this resource.
  """

  id = _messages.StringField(1)
  items = _messages.MessageField('User', 2, repeated=True)
  kind = _messages.StringField(3, default=u'clouduseraccounts#userList')
  nextPageToken = _messages.StringField(4)
  selfLink = _messages.StringField(5)


