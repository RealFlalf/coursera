import json
import functools


def to_json(func_to_dec):
    @functools.wraps(func_to_dec)
    def wrapper(*args, **kwargs):
        return json.dumps(func_to_dec(*args, **kwargs))

    return wrapper


@to_json
def get_data(dict_):
    return dict_
