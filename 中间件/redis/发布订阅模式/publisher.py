# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2021/4/18
Last Modified: 2021/4/18
Description: 发布者
"""

from .redis_helper import RedisHelper


obj = RedisHelper()
obj.public('hello')

