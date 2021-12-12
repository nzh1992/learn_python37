# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2021/4/18
Last Modified: 2021/4/18
Description: Redis base use
"""
import redis


# build connection
def connect_to_redis():
    r = redis.Redis(host='127.0.0.1', port=6379)

    # test connection
    r.set('name', 'nzh')
    print(r.get('name').decode('utf-8'))

    return r


# use connection pool
def build_connection_by_poll():
    """
    多个redis实例共享一个连接池
    """
    pool = redis.ConnectionPool(host='127.0.0.1', port=6379)

    r = redis.Redis(connection_pool=pool)
    r.set('age', 28)

    print(r.get('age').decode('utf-8'))
    return r


# 管道
def use_pipeline(redis_obj):
    """
    使用管道，在一次请求中执行多个指令, 默认情况下，一次pipeline是原子性操作。

    Args:
        redis_obj: redis实例

    Returns:

    """
    pipe = redis_obj.pipeline(transaction=True)

    # 定义安全区
    redis_obj.set('name', 'aaa')
    redis_obj.set('address', 'shanghai')
    redis_obj.set('phone', '119')

    pipe.execute()


if __name__ == '__main__':
    r = build_connection_by_poll()
    use_pipeline(r)

    print(r.get('name'))
    print(r.get('address'))
    print(r.get('phone'))
