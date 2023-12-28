from flask import jsonify, request

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .validator import query_validator


@app.route('/api/id/', methods=['POST'])
def short_url():
    """Создание новой короткой ссылки."""
    data = request.get_json()
    query_validator(data)
    url = URLMap()
    url.from_dict(data)
    db.session.add(url)
    db.session.commit()
    return jsonify(url.to_dict()), 201


@app.route('/api/id/<string:short>/', methods=['GET'])
def get_original_url(short):
    """Получение оригинальной ссылки если она существует."""
    original_url = URLMap.query.filter_by(short=short).first()
    if not original_url:
        raise InvalidAPIUsage('Указанный id не найден', 404)
    return jsonify({'url': original_url.original}), 200