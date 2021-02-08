# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from optionaldict import optionaldict

from teambition.api.base import TeambitionAPI


class Templates(TeambitionAPI):
    endpoint = 'api/template'

    def get(self, templateId, projectId, name=None, type=None):
        """
        https://open.teambition.com/help/docs/5e3a2585328b9a001bb8255f
   
        """

        params = optionaldict(projectId=projectId, name=name, type=type)
        endpoint = '{}/query'.format(self.endpoint)
        return self._get(endpoint, params=params)

    def info(self, templateId):
        """该接口用于获取任务类型信息。

        Args:
            templateId ([type]): [description]

        Returns:
            [type]: [description]
        """
        params = optionaldict(templateId=templateId)
        return self._get('{}/info'.format(self.endpoint), params=params)

    def exists(self, projectId, name):
        """该接口用于判断任务类型是否存在。
        https://open.teambition.com/help/docs/5eb5431441b191001bcda962
   
        """
        params = optionaldict(projectId=projectId, name=name)

        return self._get('{}/exists'.format(self.endpoint), params=params)
