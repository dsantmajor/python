from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as r:
    readme = r.read()

setup(
    name='pgbackup',
    version='0.1.0',
    description='Testing pgbackup',
    long_description=readme,
    author='dsantmajor',
    author_email='dontechlabs@gmail.com',
    install_requires=[],
    packages=find_packages('src'),
    package_dir={'':'src'}
)    