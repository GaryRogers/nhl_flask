import os
import yaml

_config = None

def get(file: str = None) -> dict:
    global _config

    if _config == None:
        if file == None:
            file = 'config.yaml'

        if os.path.isfile(file):
            abs_path = os.path.abspath(file)
            with open(abs_path, 'r') as f:
                _config = yaml.safe_load(f.read())
                f.close()
        else:
            raise ValueError('{0} is not a file'.format(file))
        
    return _config