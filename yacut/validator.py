from re import match

from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .views import get_unique_short_id
from settings import MAX_SHORT_LINK_LENGHT, ALLOWED_SYMBOLS, URL_SYMBOLS


def query_validator(data):
    """Валидатор запроса"""
    #Валидация url
    if data is None:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')
    if not match(
            URL_SYMBOLS, data['url']):
        raise InvalidAPIUsage('Указан недопустимый URL')
    #Валидация custom_id
    if not data.get('custom_id'):
        data['custom_id'] = get_unique_short_id()
        return 201
    if URLMap.query.filter_by(short=data['custom_id']).first():
        raise InvalidAPIUsage('Предложенный вариант короткой ссылки уже существует.')
    if not match(ALLOWED_SYMBOLS,
                 data['custom_id']) or len(data['custom_id']) > MAX_SHORT_LINK_LENGHT:
        raise InvalidAPIUsage(
            'Указано недопустимое имя для короткой ссылки'
        )