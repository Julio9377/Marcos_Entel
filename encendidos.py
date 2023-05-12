# -*- coding:utf-8 -*-

import ssl
import time,sys
from openstack import connection
from threading import Thread

ssl._create_default_https_context = ssl._create_unverified_context

def handler(event, context):
    projectId = context.getUserData('projectId', '').strip()
    region = context.getUserData('region', '').strip()
    domain= context.getUserData('domain', '').strip()
    ak = context.getAccessKey().strip()
    sk = context.getSecretKey().strip()
    ecsname = context.getUserData('ecsname', '').strip().split(',')
    logger = context.getLogger()
    if not projectId:
        raise Exception("'projectId' not configured")

    if not region:
        raise Exception("'region' not configured")

    if not domain:
        logger.info("domain not configured, use default value:myhuaweicloud.com")
        domain='myhuaweicloud.com'

    if not ak or not sk:
        ak = context.getUserData('ak', '').strip()
        sk = context.getUserData('sk', '').strip()
        if not ak or not sk:
            raise Exception("ak/sk empty")
       
    _start_ecs(logger, projectId, domain, region, ak, sk, ecsname)


def _start_ecs(logger, projectId, domain, region, ak, sk, ecsname):
    conn = connection.Connection(project_id=projectId, domain=domain, region=region, ak=ak, sk=sk)
    threads = []
    servers = conn.compute.servers()
    
    for server in servers:    
       if "ACTIVE" == server.status:
            logger.info("Skip start server '%s' for status is active(status: %s)." % (server.name, server.status))
            continue   
       if server.name in ecsname:
            _start_server(conn, server, logger) 
            continue


    if not threads:
        logger.info("No servers to be started.")
        return

    logger.info("'%d' server(s) will be started.", len(threads))

    for t in threads:
        t.join()

def _start_server(conn, server, logger):
    logger.info("Start server '%s'..." % (server.name))
    conn.compute.start_server(server)

    cost = 0
    interval = 5
    wait = 600
    while cost < wait:
        temp = conn.compute.find_server(server.id)
        if temp and "ACTIVE" != temp.status:
            time.sleep(interval)
            cost += interval
        else:
            break

    #conn.compute.wait_for_server(server, status="SHUTOFF", interval=5, wait=600)
    if cost >= wait:
        logger.warn("Wait for start server '%s' timeout." % (server.name))
        return 2

    logger.info("Start server '%s' success." % (server.name))
    return 0
