import trollius as asyncio
from trollius import From
import psutil
import logging


logger = logging.getLogger(__name__)


@asyncio.coroutine
def get_cpu_usage(agent):
    yield  From(agent.run_event.wait())
    config = agent.config['linux']
    logger.info('starting "get_cpu_usage" task for "%s"', config['hostname'])
    db_config = config['database']
    yield From(agent.async_create_database(**db_config))

    while agent.run_event.is_set():
        yield From(asyncio.sleep(config['cpu_usage_frequency']))
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
        yield From(agent.async_push(points, db_config['name']))
    logger.info('get_cpu_usage terminated')
