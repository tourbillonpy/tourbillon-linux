import sys

from setuptools import find_packages, setup

PY34_PLUS = sys.version_info[0] == 3 and sys.version_info[1] >= 4

exclude = ['tourbillon.linux.linux2'
           if PY34_PLUS else 'tourbillon.linux.linux']

install_requires = ['psutil==3.1.1']

if not PY34_PLUS:
    install_requires.append('trollius==2.0')


setup(
    name='tourbillon-linux',
    version='0.2',
    packages=find_packages(exclude=exclude),
    install_requires=install_requires,
    zip_safe=False,
    namespace_packages=['tourbillon']
)
