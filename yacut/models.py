from datetime import datetime

from flask import url_for

from . import db


class URLMap(db.Model):
    """Модель проекта."""

    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(256), nullable=False)
    short = db.Column(db.String(16), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        """Метод-сериализатор."""

        return dict(
            url=self.original,
            short_link=url_for(
                'url_link',
                short=self.short,
                _external=True
            )
        )

    def from_dict(self, data):
        """Метод-десериализатор."""

        self.original = data['url']
        self.short = data['custom_id']