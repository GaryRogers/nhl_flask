import logging
import logging.config
import modules.config

_logger = None
_config = modules.config.get()

if _config['logging']:
    logging.config.dictConfig(_config['logging'])
else:
    logging.basicConfig(level=logging.INFO)

def get():
    global _logger

    if _logger == None:
        _logger = logging.getLogger(__name__)
        _logger.debug('Initialized Logger')
    
    return _logger