# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.pipeline import ClientRawResponse

from .. import models


class UsersOperations(object):
    """UsersOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config

    def get_presence(
            self, user_id, select=None, expand=None, custom_headers=None, raw=False, **operation_config):
        """Get presence from users.

        :param user_id: key: user-id of user
        :type user_id: str
        :param select: Select properties to be returned
        :type select: list[str]
        :param expand: Expand related entities
        :type expand: list[str]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Microsoftgraphpresence or ClientRawResponse if raw=true
        :rtype: ~users.models.Microsoftgraphpresence or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`OdataerrorException<users.models.OdataerrorException>`
        """
        # Construct URL
        url = self.get_presence.metadata['url']
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if select is not None:
            query_parameters['$select'] = self._serialize.query("select", select, '[str]', div=',', unique=True)
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query("expand", expand, '[str]', div=',', unique=True)

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.OdataerrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('Microsoftgraphpresence', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_presence.metadata = {'url': '/users/{user-id}/presence'}

    def update_presence(
            self, body, user_id, custom_headers=None, raw=False, **operation_config):
        """Update the navigation property presence in users.

        :param body: New navigation property values
        :type body: ~users.models.Microsoftgraphpresence
        :param user_id: key: user-id of user
        :type user_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`OdataerrorException<users.models.OdataerrorException>`
        """
        # Construct URL
        url = self.update_presence.metadata['url']
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(body, 'Microsoftgraphpresence')

        # Construct and send request
        request = self._client.patch(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [204]:
            raise models.OdataerrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    update_presence.metadata = {'url': '/users/{user-id}/presence'}
