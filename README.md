# teambition-api
Teambition Python API
原来的 teambtion api 基本处于不能用的状态

根据 https://open.teambition.com/help/docs/5d89d63c8acc9d00143ac723进行简单的更新

# 安装与升级

推荐使用 pip 进行安装:

    pip install teambition

升级版本：

    pip install -U teambition

# 基本用法

```python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from teambition import Teambition

app_id = 'Your app id'
app_secret = 'You app secret'
org_id = 'your org id'


tb = Teambition(app_id, app_secret,org_id)

# 通过 获取 access token
tb.oauth.fetch_access_token()

# 其它操作
```

##License

The MIT License (MIT)

Copyright (c) 2015 messense

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
