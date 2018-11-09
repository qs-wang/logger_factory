from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.rst')) as f:
    long_description = f.read()

setup(name='logger_factory',
      version='0.1',
      description='Provides a simple way of create the logger',
      url='https://github.com/qs-wang/logger_factory',
      author='Q.S. Wang',
      author_email='wangqs_eclipse@yahoo.com',
      license='MIT',
      packages=['logger_factory'],
      long_description=long_description,
      long_description_content_type='text/x-rst',
      zip_safe=False)