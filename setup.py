from setuptools import setup


setup(
    name='Flask-Travis',
    version='0.0.2',
    url='https://github.com/cburmeister/flask-travis',
    license='MIT',
    author='Corey Burmeister',
    author_email='cburmeister@discogs.com',
    description='Easily fetch Travis CI environment variables when testing.',
    long_description=__doc__,
    py_modules=['flask_travis'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=['Flask'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
