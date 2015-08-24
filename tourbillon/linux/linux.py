import asyncio
import psutil
import logging


logger = logging.getLogger(__name__)


@asyncio.coroutine
def get_cpu_usage(agent):
    yield from agent.run_event.wait()
    config = agent.pluginconfig['linux']
    logger.info('starting "get_cpu_usage" task for "%s"', config['hostname'])
    db_config = config['database']
    try:
        logger.debug('try to create the database...')
        yield from agent.async_create_database(db_config['name'])
        yield from agent.async_create_retention_policy('{}_rp'.format(db_config['name']),
                                                       db_config['duration'],
                                                       db_config['replication'],
                                                       db_config['name'])
        logger.info('database "%s" created successfully', 'linux')
    except:
        pass

    while agent.run_event.is_set():
        yield from asyncio.sleep()
        cpu_percent = psutil.cpu_percent(interval=None)
        points = [{
            'measurement': 'cpu_usage',
            'tags': {
                'host': config['hostname'],
            },
            'fields': {
                'value': cpu_percent
            }
        }]
        logger.debug('{}: cpu_usage={}%'.format(
                     config['hostname'],
                     cpu_percent))
        yield from agent.async_push(points, db_config['name'])
    logger.info('get_cpu_usage terminated')


@asyncio.coroutine
def get_memory_usage(agent):
    yield from agent.run_event.wait()
    config = agent.pluginconfig['linux']
    logger.info('starting "get_memory_usage" task for "%s"', config['hostname'])
    db_config = config['database']
    try:
        logger.debug('try to create the database...')
        yield from agent.async_create_database(db_config['name'])
        yield from agent.async_create_retention_policy('{}_rp'.format(db_config['name']),
                                                       db_config['duration'],
                                                       db_config['replication'],
                                                       db_config['name'])
        logger.info('database "%s" created successfully', db_config['name'])
    except:
        pass

    while agent.run_event.is_set():
        yield from asyncio.sleep(2)
        memory = psutil.virtual_memory()
        swap = psutil.swap_memory()

        points = [{
            'measurement': 'memory_usage',
            'tags': {
                'host': config['hostname'],
            },
            'fields': {
                'v_available': memory.available,
                'v_percent': memory.percent,
                'v_used': memory.used,
                'v_free': memory.free,
                's_used': swap.used,
                's_free': swap.free,
                's_percent': swap.percent
            }
        }]
        logger.debug('{}: memory_usage: memory={}%, swap={}%'.format(
                     config['hostname'],
                     memory.percent,
                     swap.percent))
        yield from agent.async_push(points, db_config['name'])
    logger.info('get_memory_usage terminated')


@asyncio.coroutine
def get_disks_stats(agent):
    yield from agent.run_event.wait()
    config = agent.pluginconfig['linux']
    db_config = config['database']
    logger.info('starting "get_disks_stats" task for "%s"', config['hostname'])
    try:
        logger.debug('try to create the database...')
        yield from agent.async_create_database(db_config['name'])
        yield from agent.async_create_retention_policy(
            '%s_rp' % db_config['name'],
            db_config['duration'],
            db_config['replication'],
            db_config['name'])
        logger.info('database "%s" created successfully', db_config['name'])
    except:
        pass


    prev_stats = psutil.disk_io_counters(perdisk=True)

    while agent.run_event.is_set():
        yield from asyncio.sleep(config['frequency'])
        curr_stats = psutil.disk_io_counters(perdisk=True)
        points = []
        for disk in curr_stats:
            curr = curr_stats[disk]
            prev = prev_stats[disk]
            points.append({
                'measurement': 'disk_io_stats',
                'tags': {
                    'host': config['hostname'],
                    'disk': disk
                },
                'fields': {
                    'read_count': curr.read_count - prev.read_count,
                    'write_count': curr.write_count - prev.write_count,
                    'read_bytes': curr.read_bytes - prev.read_bytes,
                    'write_bytes': curr.write_bytes - prev.write_bytes,
                    'read_time': curr.read_time - prev.read_time,
                    'write_time': curr.write_time - prev.write_time,
                }
            })
        yield from agent.async_push(points, db_config['name'])
        prev_stats = curr_stats
    logger.info('get_disks_stats terminated')


@asyncio.coroutine
def get_disks_iostatus(agent):
    yield from agent.run_event.wait()
    config = agent.pluginconfig['linux']
    db_config = config['database']
    logger.info('starting "get_disks_status" task for "%s"', config['hostname'])
    try:
        logger.debug('try to create the database...')
        yield from agent.async_create_database(db_config['name'])
        yield from agent.async_create_retention_policy(
            '%s_rp' % db_config['name'],
            db_config['duration'],
            db_config['replication'],
            db_config['name'])
        logger.info('database "%s" created successfully', db_config['name'])
    except:
        pass

    while agent.run_event.is_set():
        yield from asyncio.sleep(config['frequency'])
        status = psutil.disk_io_counters(perdisk=True)
        points = []
        for disk in curr_stats:
            curr = status[disk]
            points.append({
                'measurement': 'disk_status',
                'tags': {
                    'host': config['hostname'],
                    'disk': disk
                },
                'fields': {
                    'read_count': curr.read_count,
                    'write_count': curr.write_count,
                    'read_bytes': curr.read_bytes,
                    'write_bytes': curr.write_bytes,
                    'read_time': curr.read_time,
                    'write_time': curr.write_time,
                }
            })
        yield from agent.async_push(points, db_config['name'])
    logger.info('get_disks_stats terminated')
