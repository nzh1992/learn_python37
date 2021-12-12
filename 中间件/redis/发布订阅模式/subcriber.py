# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2021/4/18
Last Modified: 2021/4/18
Description: 订阅者
"""

from .redis_helper import RedisHelper


obj = RedisHelper()
redis_sub = obj.subscribe()

print("waiting...")

while True:
    msg = redis_sub.parse_response()
    print(msg)
