flask-travis
===========

Easily fetch TravisCI environment variables when testing.

## Install

```python
pip install Flask-Travis
```

## Usage

Import and initialize:

```python
from flask.ext.import Travis

app = Flask(__name__)

travis = Travis(app)
```

Or better yet, use Flask's application factory pattern:

```python
travis.init_app(app)
```
