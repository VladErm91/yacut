import string
import random

from .models import URLMap


def get_unique_short_id(length=6):
    """
    Алгоритм формирования коротких идентификаторов переменной длины.
    """
    symb = string.ascii_letters + string.digits
    new_id = ''.join(random.choices(symb, k=length))
    if URLMap.query.filter_by(short=new_id).first():
        return get_unique_short_id()
    return new_id