import os
import yaml
import modules.logger

_secrets = None
_logger = modules.logger.get()

def get(file: str = None) -> dict:
    global _secrets

    if _secrets == None:
        if file == None:
            file = 'secrets.yaml'

        if os.path.isfile(file):
            logger = modules.logger.get()
            abs_path = os.path.abspath(file)
            logger.debug('reading secrets from {0}'.format(abs_path))
            with open(abs_path, 'r') as f:
                _secrets = yaml.safe_load(f.read())
            f.close()
        else:
            raise ValueError('{0} is not a file'.format(file))
        
    return _secrets