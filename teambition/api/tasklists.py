# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from optionaldict import optionaldict

from teambition.api.base import TeambitionAPI


class Tasklists(TeambitionAPI):
    endpoint = 'api/tasklist'

    def create(self, operatorId, projectId, tasklists):
        """
        新建任务分组

        详情请参考
        https://open.teambition.com/help/docs/5e3a2582328b9a001bb82558

        """
        data = optionaldict(
            operatorId=operatorId,
            projectId=projectId,
            tasklists=tasklists
        )
        return self._post(
            '{}/create',
            data=data
        )

    def get(self, tasklistId=None, projectId=None, taskgroupId=None):
        """
        获取任务分组列表

        详情请参考
        https://open.teambition.com/help/docs/5e3a2582328b9a001bb82559


        """
        params = optionaldict(tasklistId=tasklistId,
                              projectId=projectId, taskgroupId=taskgroupId)

        endpoint = '{}/query'.format(self.endpoint)

        return self._get(endpoint, params=params)

    def delete(self, tasklistId):
        """
        删除任务分组

        详情请参考
        http://docs.teambition.com/wiki/tasklists#tasklists-delete


        """
        params = optionaldict(tasklistId=tasklistId)
        return self._delete('{}/delete'.format(self.endpoint), params=params)
