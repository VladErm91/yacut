from flask import flash, redirect, render_template, url_for

from . import app, db
from .forms import URLForm
from .models import URLMap
from .utils import get_unique_short_id


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
