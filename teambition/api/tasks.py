# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from optionaldict import optionaldict

from teambition.api.base import TeambitionAPI


class Tasks(TeambitionAPI):
    endpoint = 'api/task'

    def get(self, taskId=None, parentTaskId=None, userId=None, organizationId=None, condition=None, idDone=None,
              projectId=None, pageToken=None, pageSize=None):
        """
        获取任务

        详情请参考
        https://open.teambition.com/help/docs/5e3a2581328b9a001bb82556


        :return: 返回的 JSON 数据包
        """
        params = optionaldict(
            taskId=taskId,
            parentTaskId=parentTaskId,
            userId=userId,
            organizationId=organizationId,
            condition=condition,
            idDone=idDone,
            projectId=projectId,
            pageToken=pageToken,
            pageSize=pageSize

        )
        return self._get(
            '{}/query'.format(self.endpoint),
            params=params
        )

    def create(self, operatorId, projectId, templateId, tasklistId,
               taskgroupId, content, statusId, executorId=None, startDate=None,
               dueDate=None, note=None, priority=None, visible=None,
               parentTaskId=None, participants=None, customfields=None
               ):
        """
        创建任务

        详情请参考
        http://docs.teambition.com/wiki/tasks#tasks-create

        """
        data = optionaldict(
            operatorId=operatorId,
            projectId=projectId,
            templateId=templateId,
            tasklistId=tasklistId,
            taskgroupId=taskgroupId,
            content=content,
            statusId=statusId,
            executorId=executorId,
            startDate=startDate,
            dueDate=dueDate,
            note=note,
            priority=priority,
            visible=visible,
            parentTaskId=parentTaskId,
            participants=participants,
            customfields=customfields
        )
        return self._post(
            'api/task/create',
            data=data
        )

    def delete(self, operatorId, ids=None, projectId=None, tasklistId=None,  taskgroupId=None):
        """
        删除任务

        详情请参考
        https://open.teambition.com/help/docs/5e3a2581328b9a001bb82557

        """
        body = optionaldict(operatorId=operatorId, ids=ids, projectId=projectId,

                            tasklistId=tasklistId, taskgroupId=taskgroupId)
        return self._delete('{}/delete'.format(self.endpoint), body=body)

    def update(self, operatorId, taskId, projectId=None, templateId=None, tasklistId=None,
               taskgroupId=None, content=None, statusId=None, executorId=None, startDate=None,
               dueDate=None, note=None, priority=None, visible=None,
               parentTaskId=None, participants=None, customfields=None, tagIds=None
               ):
        """
        更新任务

        详情请参考
        http://docs.teambition.com/wiki/tasks#tasks-update

        """
        data = optionaldict(
            operatorId=operatorId,
            taskId=taskId,
            projectId=projectId,
            templateId=templateId,
            tasklistId=tasklistId,
            taskgroupId=taskgroupId,
            content=content,
            statusId=statusId,
            executorId=executorId,
            startDate=startDate,
            dueDate=dueDate,
            note=note,
            priority=priority,
            visible=visible,
            parentTaskId=parentTaskId,
            participants=participants,
            customfields=customfields,
            tagIds=tagIds
        )
        return self._post(
            '{}/update'.format(self.endpoint),
            data=data)

    def get_dependencies(self, taskId, toId, pageSize=None, pageToken=None):
        params = optionaldict(
            taskId, toId=toId, pageSize=pageSize, pageToken=pageToken)
        return self._get('{}/dependencies'.format(self.endpoint), params=params)

    def get_links(self, taskId, pageSize=None, pageToken=None):
        body = optionaldict(
            taskId, pageSize=pageSize, pageToken=pageToken)

        return self._post('{}/links/query'.format(self.endpoint), data=body)

    def delete_links(self, operatorId, taskId, linkId, linkType):
        body = optionaldict(operatorId=operatorId,
                            taskId=taskId, linkId=linkId, linkType=linkType)
        return self._post('{}/links/delete'.format(self.endpoint), data=body)

    def add_links(self, creatorId, taskId, linkId, linkType):
        body = optionaldict(creatorId=creatorId,
                            taskId=taskId, linkId=linkId, linkType=linkType)
        return self._post('{}/links/add'.format(self.endpoint), data=body)
    
    def add_comment(self, creatorId, taskId, comment):
        """创建任务评论

        该接口用于创建任务评论。
        https://open.teambition.com/help/docs/5f33928c519fd100160f50c9

        Args:
            creatorId ([type]): [description]
            taskId ([type]): [description]
            comment ([type]): [description]

        Returns:
            [type]: [description]
        """
        body = optionaldict(creatorId=creatorId,
                            taskId=taskId, comment=comment)
        return self._post('{}/comment/create'.format(self.endpoint), data=body)
