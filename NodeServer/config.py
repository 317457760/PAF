#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
################################################################################
#
# Copyright (c) 2014 Baidu.com, Inc. All Rights Reserved
#
################################################################################
"""
    Author  :   shensifan(shensifan2004@163.com)
    Date    :   2014/11/06 14:28:00
    Desc    :   node server配置文件
"""
################服务端配置###########################
import socket
class Server(object):
    #命名空间,用于区分部门或者分组
    NAMESPACE = "EE"
    #app名称
    APPLICATION = "PAF"
    #服务名称
    SERVICE = "node"
    #服务分组,服务内分组,用于区分IDC或者做set
    #GROUP = None
    #工作线程数量
    WORKER_COUNT = 20
    #队列长度,加入过载保护,当队列过长时丢包
    #QUEUE_SIZE = 10000000
    #队列超时时间,在队列中呆时间过长后丢包
    #QUEUE_TIME_OUT
    #服务端口
    LISTEN_IP = socket.gethostbyname(socket.gethostname())
    LISTEN_PORT = 9999
    #本地日志路径
    LOG_PATH = "./log"
    #远程日志服务器
    LOG_SERVER = None
    #日志级别
    #LOG_LEVEL = 0
    #node服务器地址,node不向自己注册
    NODE_SERVER = None

################客户端配置###########################
class Client(object):
    #回调线程数量
    CALLBACK_COUNT = 20
    #位置服务器地址,用于查询其它服务位置
    LOCATER_SERVER = ('127.0.0.1', 8001)

################公用配置##########################
class Public(object):
    #调用统计服务
    #STAT_SERVER = "EE.PAF.stat"
    #使用多进程工作，多进程间使用pipe通信
    USE_PIPE = False

################服务自身配置########################
class Private(object):
    PYTHON = "/usr/bin/python"
