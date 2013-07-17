import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid',
    'SQLAlchemy',
    'transaction',
    'pyramid_tm',
    'pyramid_debugtoolbar',
    'zope.sqlalchemy',
    'waitress',
    'nokaut',
    'allegro',
    'formencode',
    'pyramid_simpleform'
    ]

links = ['https://github.com/pkrysiak/allegro_repo/archive/master.zip#egg=allegro',
         'https://github.com/pkrysiak/nokaut_repo/archive/master.zip#egg=nokaut']

setup(name='pyramid_app',
      version='0.0',
      description='pyramid_app',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      dependency_links = links,
      test_suite='pyramid_app',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = pyramid_app:main
      [console_scripts]
      initialize_pyramid_app_db = pyramid_app.scripts.initializedb:main
      """,
      )
