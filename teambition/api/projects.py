# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from datetime import datetime

import pytz
from optionaldict import optionaldict

from teambition.api.base import TeambitionAPI


class Projects(TeambitionAPI):
    endpoint = 'api/project'

    def get(self, name=None, userId=None, creatorId=None, isArchived=None, projectIds=None, pageToken=None, pageSize=None):
        """
        查询项目

        该接口用于按给定条件查询项目，当传入多个条件的参数时，需要全部满足条件才会返回。

        详情请参考
        https://open.teambition.com/help/docs/5e13ed08edac6e001bd848d4


        """
        params = optionaldict(
            name=name,
            userId=userId,
            creatorId=creatorId,
            isArchived=isArchived,
            projectIds=projectIds,
            pageToken=pageToken,
            pageSize=pageSize
        )

        return self._get('{}/query'.format(self.endpoint), params=params)

    def create(self, operatorId, name=None, description=None, cover=None,
               type="workflow", visibility="private"):
        """
        新建项目

        详情请参考
        http://docs.teambition.com/wiki/projects#projects-create

        :param name: 项目名称
        :param description: 可选，项目描述
        :param logo: 可选，项目 logo
        :param category: 可选，项目类别
        :param divider_index: 可选，dividers 中得 index，仅对拥有者有效
        :param organization_id: 可选，组织 ID，创建组织项目时需要提供此参数
        :return: 新建的项目信息
        """
        data = optionaldict(
            operatorId=operatorId,
            name=name,
            description=description,
            cover=cover,
            type=type,
            visibility=visibility
        )
        return self._post('{}/create'.format(self.endpoint),  data=data)

    def delete(self, operatorId, projectId):
        """
        删除项目

        详情请参考
        https://open.teambition.com/help/docs/5e13ed07edac6e001bd848d3

        """
        params = optionaldict(operatorId=operatorId,  projectId=projectId)
        return self._delete('{}/delete'.format(self.endpoint), params=params)

    def update(self, operatorId, name=None, description=None, cover=None,
               visibility="private"):
        """
        更新项目

        详情请参考
        https://open.teambition.com/help/docs/5e13ed06edac6e001bd848d2


        """
        data = optionaldict(
            operatorId=operatorId,
            name=name,
            description=description,
            cover=cover,
            visibility=visibility
        )
        return self._post('{}/update'.format(self.endpoint),  data=data)

    def add_members(self, operatorId, projectId,  members):
        """
        添加项目成员

        详情请参考
        https://open.teambition.com/help/docs/5e13ed08edac6e001bd848d5

        """
        body = optionaldict(
            operatorId=operatorId,
            projectId=projectId,
            members=members
        )
        return self._post('{}/member/add'.format(self.endpoint),  data=body)

    create_members = add_members  # Alias for add_members

    def remove_member(self, operatorId, projectId,  userIds):
        """
        删除项目成员

        详情请参考
        https://open.teambition.com/help/docs/5e13ed09edac6e001bd848d7


        """
        body = optionaldict(
            operatorId=operatorId,
            projectId=projectId,
            userIds=userIds
        )
        return self._post('{}/member/delete'.format(self.endpoint),  data=body)

    def get_members(self, projectId, pageToken=None, pageSize=None):
        """
        获取项目成员

        详情请参考
        http://docs.teambition.com/wiki/projects#projects-get-members

        :param id: 项目 ID
        :param user_id: 可选，成员 ID
        :return: 返回的 JSON 数据包
        """
        params = optionaldict(
            projectId=projectId,
            pageToken=pageToken,
            pageSize=pageSize
        )

        return self._get('{}/member/list'.format(self.endpoint), params=params)

    def member_exist(self, projectId, userId):
        """
        获取项目推荐成员列表

        详情请参考
        https://open.teambition.com/help/docs/5e13ed09edac6e001bd848d8


        """

        params = optionaldict(
            operatorId=projectId,
            userId=userId
        )

        return self._get('{}/member/exist'.format(self.endpoint), params=params)

    def update_member_role(self, operatorId, projectId, userId, role):
        """
        更新项目成员角色

        详情请参考
        https://open.teambition.com/help/docs/5e13ed0bedac6e001bd848d9

        """
        body = optionaldict(
            operatorId=operatorId,
            projectId=projectId,
            userId=userId,
            role=role
        )

        return self._post('{}/member/updateRole'.format(self.endpoint),  data=body)
