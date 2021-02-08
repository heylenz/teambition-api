# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from optionaldict import optionaldict

from teambition.api.base import TeambitionAPI


class Users(TeambitionAPI):
    endpoint = 'api/user'

    def get(self, email):
        """

        查询用户信息

        详情请参考
        https://open.teambition.com/help/docs/5eb5430d41b191001bcda952

        :return: 返回的 JSON 数据包
        """
        params = optionaldict(
            email=email,
        )

        return self._get('{}/query'.format(self.endpoint), params=params)

    def update(self, userId=None, avatarUrl=None, birthday=None, location=None,
               name=None, phone=None, title=None):
        """
        更新用户信息

        详情请参考
        https://open.teambition.com/help/docs/5eb5430d41b191001bcda953

        """
        body = optionaldict(
            userId=userId,
            avatarUrl=avatarUrl,
            title=title,
            birthday=birthday,
            location=location,
            phone=phone,
            name=name
        )
        return self._post('{}/update'.format(self.endpoint), data=body)
