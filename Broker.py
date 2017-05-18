import logging
import asyncio
import os
from mqtt.broker import Broker
from mqtt.version import get_version
from docopt import docopt
from mqtt.utils import read_yaml_config

logger = logging.getLogger(__name__)


def main(*args, **kwargs):

    formatter = "[%(asctime)s] :: %(message)s"
    level = logging.INFO
    logging.basicConfig(level=level, format=formatter)
    config = read_yaml_config(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'default_broker.yaml'))
    loop = asyncio.get_event_loop()
    broker = Broker(config)
    try:
        loop.run_until_complete(broker.start())
        loop.run_forever()
    except KeyboardInterrupt:
        loop.run_until_complete(broker.shutdown())
    finally:
        loop.close()


if __name__ == "__main__":
    main()