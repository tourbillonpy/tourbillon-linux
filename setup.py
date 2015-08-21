from setuptools import setup, find_packages
setup(
    name='tourbillon-linux',
    version='0.1',
    packages=find_packages(),
    install_requires=['psutil==3.1.1'],
    zip_safe=False,
    namespace_packages=['tourbillon']
)
