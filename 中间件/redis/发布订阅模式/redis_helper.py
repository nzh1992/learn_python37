# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2021/4/18
Last Modified: 2021/4/18
Description: 
"""
import redis


class RedisHelper:
    def __init__(self):
        self.__conn = redis.Redis(host='127.0.0.1')
        self.chan_sub = 'fm92.4'
        self.chan_pub = 'fm92.4'

    def public(self, msg):
        self.__conn.publish(self.chan_pub, msg)

    def subscribe(self):
        pub = self.__conn.pubsub()
        pub.subscribe(self.chan_sub)
        pub.parse_response()
        return pub

