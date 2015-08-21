import asyncio
import psutil
import logging


logger = logging.getLogger(__name__)


@asyncio.coroutine
def get_cpu_usage(agent):
    yield from agent.run_event.wait()
    config = agent.pluginconfig['linux']
    logger.info('starting "get_cpu_usage" task for "%s"', config['hostname'])
    try:
        logger.debug('try to create the database...')
        yield from agent.async_create_database('linux')
        yield from agent.async_create_retention_policy('linux_rp',
                                                       '365d',
                                                       '1',
                                                       'linux')
        logger.info('database "%s" created successfully', 'linux')
    except:
        pass

    while agent.run_event.is_set():
        yield from asyncio.sleep(2)
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
        yield from agent.async_push(points, 'linux')
    logger.info('get_cpu_usage terminated')


@asyncio.coroutine
def get_memory_usage(agent):
    yield from agent.run_event.wait()
    config = agent.pluginconfig['linux']
    logger.info('starting "get_memory_usage" task for "%s"', config['hostname'])
    try:
        logger.debug('try to create the database...')
        yield from agent.async_create_database('linux')
        yield from agent.async_create_retention_policy('linux_rp',
                                                       '365d',
                                                       '1',
                                                       'linux')
        logger.info('database "%s" created successfully', 'linux')
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
        yield from agent.async_push(points, 'linux')
    logger.info('get_memory_usage terminated')
