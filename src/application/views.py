"""
views.py

URL route handlers

Note that any handler params must match the URL route params.
For example the *say_hello* handler, handling the URL route '/hello/<username>',
  must be passed *username* as the argument.

"""
from google.appengine.api import users
from google.appengine.runtime.apiproxy_errors import CapabilityDisabledError

from flask import request, render_template, flash, url_for, redirect

from flask_cache import Cache

from application import app
from decorators import login_required, admin_required
from forms import ExampleForm
from models import Sign


# Flask-Cache (configured to use App Engine Memcache API)
cache = Cache(app)


def index():
    return redirect(url_for('list_homes'))

def list_homes():
    """List all homes"""
    return render_template('list_homes.html')

def show_home(home_id, date):
    s = Sign.all().filter('home =',home_id).filter("date =", date).get()
    return render_template('home.html', home_id=home_id, date=date, sign=s) 

def show_graph(home_id, date):
    atype = request.args.get('type')
    maxy = request.args.get('max')
    return render_template('graph2.html', maxy=maxy, atype=atype) 

@login_required
def edit_example(example_id):
    example = ExampleModel.get_by_id(example_id)
    form = ExampleForm(obj=example)
    if request.method == "POST":
        if form.validate_on_submit():
            example.example_name = form.data.get('example_name')
            example.example_description = form.data.get('example_description')
            example.put()
            flash(u'Example %s successfully saved.' % example_id, 'success')
            return redirect(url_for('list_examples'))
    return render_template('edit_example.html', example=example, form=form)


@admin_required
def admin_only():
    """This view requires an admin account"""
    return 'Super-seekrit admin page.'


@cache.cached(timeout=60)
def cached_examples():
    """This view should be cached for 60 sec"""
    examples = ExampleModel.query()
    return render_template('list_examples_cached.html', examples=examples)


def warmup():
    """App Engine warmup handler
    See http://code.google.com/appengine/docs/python/config/appconfig.html#Warming_Requests

    """
    return ''

