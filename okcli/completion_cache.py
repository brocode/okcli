import hashlib
from os import path

def completion_filename(user, host):
    return hashlib.md5(("%s%s" % (user, host)).encode('utf-8')).hexdigest()

def completion_cache_dir(config):
    return path.join(path.dirname(config.filename), '.okcli_cache')

def completion_cache_file(user, host, config):
    return path.join(completion_cache_dir(config), completion_filename(user, host))

def existing_completion_cache_file(user, host, config):
    maybe_file = completion_cache_file(user, host, config)
    if path.isfile(maybe_file):
        return maybe_file
    else:
        return None
