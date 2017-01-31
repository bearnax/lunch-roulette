try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': "Don't worry, I'll pick lunch for you.",
    'author': 'William Thomas Brodnax',
    'url': 'nope, not yet',
    'download_url': 'you must be dreaming',
    'author_email': 'wbrodnax@gmail.com',
    'version': '0.2',
    'install_requires': ['pytest'],
    'packages': ['lunch_roulette'],
    'scripts': [],
    'name': 'lunch-roulette'
}

setup(**config)
