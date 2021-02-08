# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import requests
import jwt
import datetime
from furl import furl
from teambition.api.base import TeambitionAPI


class OAuth(TeambitionAPI):

    def fetch_access_token(self, delta_time=600):
        token = jwt.encode({'_appId': self._client.app_id, "iat": datetime.datetime.utcnow(), "exp": datetime.datetime.utcnow(
        ) + datetime.timedelta(seconds=delta_time)}, self._client.app_secret, algorithm='HS256').decode('utf-8')
        self._client._access_token = token
        return token

    get_access_token = fetch_access_token  # Alias

    def check(self, access_token=None):
        pass
