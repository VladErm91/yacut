from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import (URL, DataRequired,
                                Length, Optional,
                                Regexp, ValidationError)
from .models import URLMap
from settings import ALLOWED_SYMBOLS


class URLForm(FlaskForm):
    """Форма генерации коротких ссылок"""

    original_link = URLField(
        'Ваша длинная ссылка',
        validators=[DataRequired(message='Обязательное поле'), URL(
            require_tld=True, message='Некорректный URL')]
    )
    custom_id = StringField(
        'Ваша короткая ссылка',
        validators=[Length(1, 16), Optional(), Regexp(
            ALLOWED_SYMBOLS,
            message='Можно использовать только [A-Za-z0-9]')]
    )
    submit = SubmitField('Создать')

    def validate_custom_id(self, field):
        """Проверка уникальности поля."""
        if field.data and URLMap.query.filter_by(short=field.data).first():
            raise ValidationError(
                'Предложенный вариант короткой ссылки уже существует.')
