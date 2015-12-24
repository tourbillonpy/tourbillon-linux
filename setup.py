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
    description='A tourbillon plugin for collecting metrics from linux.',
    version='0.4',
    packages=find_packages(exclude=exclude),
    install_requires=install_requires,
    zip_safe=False,
    namespace_packages=['tourbillon'],
    author='The Tourbillon Team',
    author_email='tourbillonpy@gmail.com',
    url='https://github.com/tourbillonpy/tourbillon-linux',
    license='ASF',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: System :: Monitoring',
    ],
    keywords='monitoring metrics agent influxdb linux',
)
