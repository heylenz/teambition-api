# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import sys
import inspect
try:
    import simplejson as json
except ImportError:
    import json

import requests

from teambition import api
from teambition.api.base import TeambitionAPI
from teambition.utils import JSONEncoder, JSONDecoder
from teambition.exceptions import TeambitionException


def _is_api_endpoint(obj):
    return isinstance(obj, TeambitionAPI)


class Teambition(object):
    """
    Teambition API 客户端
    """

    API_BASE_URL = 'https://open.teambition.com/'

    oauth = api.OAuth()
    projects = api.Projects()
    tasklists = api.Tasklists()
    taskgroups = api.TaskGroups()
    templates  = api.Templates()    
    taskflows = api.TaskFlows()    
    tasks = api.Tasks()
    users = api.Users()
    organizations = api.Organizations()
    departments = api.Departments()

    def __new__(cls, *args, **kwargs):
        self = super(Teambition, cls).__new__(cls)
        if sys.version_info[:2] == (2, 6):
            # Python 2.6 inspect.gemembers bug workaround
            # http://bugs.python.org/issue1785
            for _class in cls.__mro__:
                if issubclass(_class, Teambition):
                    for name, tb_api in _class.__dict__.items():
                        if isinstance(tb_api, TeambitionAPI):
                            api_cls = type(tb_api)
                            tb_api = api_cls(self)
                            setattr(self, name, tb_api)
        else:
            api_endpoints = inspect.getmembers(self, _is_api_endpoint)
            for name, tb_api in api_endpoints:
                api_cls = type(tb_api)
                tb_api = api_cls(self)
                setattr(self, name, tb_api)
        return self

    def __init__(self, app_id, app_secret, org_id=None):
        """
        初始化 Teambition API Client

        :param app_id: 申请应用时分配的 app_id
        :param app_secret: 申请应用时分配的 app_secret
        :param org_id: 可选，org_id
        """
        self.app_id = app_id
        self.app_secret = app_secret
        self.org_id = org_id
        self._access_token = None

    def _request(self, method, endpoint, **kwargs):
        if not endpoint.startswith(('http://', 'https://')):
            api_base_url = kwargs.pop('api_base_url', self.API_BASE_URL)
            url = '{base}{endpoint}'.format(
                base=api_base_url,
                endpoint=endpoint
            )
        else:
            url = endpoint

        if isinstance(kwargs.get('data', ''), dict):
            body = json.dumps(
                kwargs['data'],
                ensure_ascii=False,
                cls=JSONEncoder
            )
            body = body.encode('utf-8')
            kwargs['data'] = body

        if 'headers' not in kwargs:
            kwargs['headers'] = {}
        if 'Content-Type' not in kwargs['headers']:
            kwargs['headers']['Content-Type'] = 'application/json'
        if 'Authorization' not in kwargs['headers']:
            kwargs['headers']['Authorization'] = 'Bearer {0}'.format(
                self.access_token
            )

        if 'X-Tenant-Id' not in kwargs['headers']:
            kwargs['headers']['X-Tenant-Id'] = self.org_id

        if 'X-Tenant-Type' not in kwargs['headers']:
            kwargs['headers']['X-Tenant-Type'] = "organization"

        res = requests.request(
            method=method,
            url=url,
            **kwargs
        )
        # Error handling, reraise RequestException as TeambitionException
        try:
            res.raise_for_status()
        except requests.RequestException as reqe:
            code = -1
            message = None
            if reqe.response.text:
                try:
                    errinfo = json.loads(reqe.response.text)
                    code = errinfo['code']
                    message = errinfo['message']
                except ValueError:
                    pass
            raise TeambitionException(
                code=code,
                message=message,
                client=self,
                request=reqe.request,
                response=reqe.response
            )

        result = res.json(cls=JSONDecoder) if res.text else {}
        return result

    def get(self, endpoint, **kwargs):
        return self._request('get', endpoint, **kwargs)

    def post(self, endpoint, **kwargs):
        return self._request('post', endpoint, **kwargs)

    def put(self, endpoint, **kwargs):
        return self._request('put', endpoint, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self._request('delete', endpoint, **kwargs)

    @property
    def access_token(self):
        """
        获取 access_token

        :return: access_token
        """
        return self._access_token

    @access_token.setter
    def access_token(self, token):
        """
        设置 access_token

        :param token: access_token
        """
        self._access_token = token
