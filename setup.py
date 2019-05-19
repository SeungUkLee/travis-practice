import os
import re

from setuptools import setup, find_packages


def read(f):
    return open(os.path.join(os.path.dirname(__file__), f)).read().strip()


def read_version():
    regexp = re.compile(r"^__version__\W*=\W*'([\d.abrc]+)'")
    init_py = os.path.join(os.path.dirname(__file__), 'addthree', '__init__.py')
    with open(init_py) as f:
        for line in f:
            match = regexp.match(line)
            if match is not None:
                return match.group(1)
        else:
            raise RuntimeError('Cannot find version in addthree/__init__.py')


setup(
    name='addthree',
    author='test',
    author_email='dltmddnr5' '@' 'naver.com',
    description='Practice deploying to PyPI',
    long_description='\n\n'.join((read('README.rst'), read('CHANGES.txt'))),
    long_description_content_type='text/markdown',
    license='MIT',
    version='0.1.0',
    url='https://github.com/SeungUkLee/travis-practice',
    packages=find_packages(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Topic :: Utilities',
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
    ],
)
