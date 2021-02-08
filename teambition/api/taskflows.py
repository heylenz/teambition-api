# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from optionaldict import optionaldict

from teambition.api.base import TeambitionAPI


class TaskFlows(TeambitionAPI):
    endpoint = 'api/taskflow'

    def get(self, taskflowId):
        """该接口用于查询工作流的信息。
        https://open.teambition.com/help/docs/5e3a2585328b9a001bb82560
        Args:
            taskgroupId (string, optional): 任务分组 ID.
            projectId (string, optional): 项目 ID

        Returns:
            [json]:  返回的 JSON 数据包
        """

        params = optionaldict(taskflowId=taskflowId)

        endpoint = '{}/query'.format(self.endpoint)

        return self._get(endpoint, params=params)
