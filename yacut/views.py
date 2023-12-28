import string
import random

from flask import flash, redirect, render_template, url_for

from . import app, db
from .forms import URLForm
from .models import URLMap


def get_unique_short_id(length=6):
    """
    Алгоритм формирования коротких идентификаторов переменной длины.
    """
    symb = string.ascii_letters + string.digits
    existing_urls = URLMap.query.all()
    existing_ids = {url.short for url in existing_urls}
    while True:
        new_id = ''.join(random.choices(symb, k=length))
        if new_id not in existing_ids:
            return new_id


@app.route('/<string:short>')
def url_link(short):
    converted_url = URLMap.query.filter_by(short=short).first_or_404()
    return redirect(converted_url.original)


@app.route('/', methods=['GET', 'POST'])
def add_url():
    form = URLForm()
    if form.validate_on_submit():
        short = form.custom_id.data or get_unique_short_id()
        url = URLMap(
            original=form.original_link.data,
            short=short
        )
        db.session.add(url)
        db.session.commit()
        flash(url_for('url_link', short=short, _external=True))
    return render_template('main.html', form=form)
