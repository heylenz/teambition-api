# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from optionaldict import optionaldict

from teambition.api.base import TeambitionAPI


class Organizations(TeambitionAPI):
    endpoint = 'api/org'

    def get(self, orgId):
        """
        获取企业信息

        详情请参考
        https://open.teambition.com/help/docs/5e13ed01edac6e001bd848c8

        :param orgId: 组织 ID
        :return: 提供 id 返回特定组织信息，否则返回用户相关组织列表
        """
        params = optionaldict(
            orgId=orgId,
        )

        return self._get('{}/info'.format(self.endpoint), params=params)

    def get_members(self, userIds=None, pageToken=None, pageSize=None, filter=None):
        """
        获取企业成员列表

        详情请参考
        https://open.teambition.com/help/docs/5e13ed03edac6e001bd848cb
        https://open.teambition.com/help/docs/5eb5430f41b191001bcda959

        """
        params = optionaldict(
            userIds=userIds,
            orgId=self._client.org_id,
            pageToken=pageToken,
            pageSize=pageSize,
            filter=filter
        )

        if not userIds:
            return self._get("{}/member/list".format(self.endpoint), params=params)
        else:
            return self._post('{}/member/batchGet'.format(self.endswith()), params=params)

    def add_members(self, operatorId, members):
        """
        添加企业成员

        详情请参考
        https://open.teambition.com/help/docs/5e13ed03edac6e001bd848ca

        :param id: 组织 ID
        :param email: 邮箱或邮箱列表
        :return: 返回的 JSON 数据包
        """
        body = optionaldict(operatorId=operatorId,

                            orgId=self._client.org_id,  members=members)

        return self._post('{}/member/add'.format(self.endpoint), data=body)

    create_members = add_members  # Alias for add_members

    def remove_member(self, operatorId, userId):
        """
        删除企业成员

        详情请参考
        https://open.teambition.com/help/docs/5e13ed04edac6e001bd848cd


        """
        body = optionaldict(operatorId=operatorId, userId=userId)
        return self._post("{}/member/delete".format(self.endpoint), data=body)

    def get_members_count(self):
        """
        获取企业成员数量

        详情请参考
        https://open.teambition.com/help/docs/5eb5431041b191001bcda95a

        :param orgId: 组织 ID
        :return: 返回的 JSON 数据包
        """
        params = optionaldict(
            orgId=self._client.org_id
        )

        return self._get("{}/member/count".format(self.endpoint), params=params)

    def get_admin_members(self):
        """
        获取企业的管理员（含拥有者）

        详情请参考
        https://open.teambition.com/help/docs/5e13ed04edac6e001bd848cc

        """
        pass

    def get_owners_members(self):
        """
        获取企业拥有者

        详情请参考
        https://open.teambition.com/help/docs/5eb5431041b191001bcda95b

        :param id: 组织 ID
        :param user_id: 组织成员 ID
        :param role_type: 角色类型, 可选值 member, admin, owner
        """
        pass

    def query_members(self, query, pageSize=None, pageToken=None):
        params = optionaldict(orgId=self._client.org_id,
                              query=query, pageSize=pageSize, pageToken=pageToken)

        return self._get('{}/member/search'.format(self.endpoint), params=params)
