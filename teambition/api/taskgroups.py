# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from optionaldict import optionaldict

from teambition.api.base import TeambitionAPI


class TaskGroups(TeambitionAPI):
    endpoint = 'api/taskgroup'

    def create(self, operatorId, projectId, taskgroups):
        """
        该接口用于创建任务分组。

        详情请参考
        https://open.teambition.com/help/docs/5e3a2583328b9a001bb8255b


        """
        data = optionaldict(
            operatorId=operatorId,
            projectId=projectId,
            taskgroups=taskgroups
        )
        return self._post(
            '{}/create'.format(self.endpoint),
            data=data
        )

    def update(self, operatorId, taskgroupId=None, name=None, description=None, tasklistIds=None):
        """
        更新任务分组

        详情请参考
        https://open.teambition.com/help/docs/5e3a2584328b9a001bb8255c

        """
        data = optionaldict(
            operatorId=operatorId,
            taskgroupId=taskgroupId,
            name=name,
            description=description,
            tasklistIds=tasklistIds

        )
        return self._post(
            '{}/update'.format(self.endpoint),
            data=data
        )

    def get(self, taskgroupId=None, projectId=None):
        """查询任务分组

        https://open.teambition.com/help/docs/5e3a2584328b9a001bb8255d
        """

        params = optionaldict(taskgroupId=taskgroupId,
                              projectId=projectId)

        endpoint = '{}/query'.format(self.endpoint)

        return self._get(endpoint, params=params)

    def delete(self, taskgroupId):
        """
        删除任务分组

        详情请参考
        http://docs.teambition.com/wiki/tasklists#tasklists-delete

        :param id: 任务分组 ID
        :return: 返回的 JSON 数据包
        """
        params = optionaldict(taskgroupId=taskgroupId)
        return self._delete('{0}/delete'.format(self._endpoint), params=params)
