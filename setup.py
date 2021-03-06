import sys

if sys.version_info < (3, 5, 0):
    sys.stderr.write("ERROR: You need Python 3.5 or later to use Irisett.\n")
    exit(1)

from setuptools import setup


long_description = '''
Irisett -- A small API driven monitoring engine
================================================

Irisett is a small, API driven monitoring engine. It is a simple but
complete monitoring engine that uses nagios monitor binaries to perform
service checks. Irisett does not come with a web interface. It is intended
to be integrated with other systems and interfaces and is thus primarily
accessed using a HTTP API. A basic command line client for communicating
with the server is also provided.
'''.lstrip()

packages = [
    'irisett',
    'irisett.monitor',
    'irisett.notify',
    'irisett.webapi',
    'irisett.webmgmt',
]

package_data = {
    'irisett.webmgmt': ['static/*', 'templates/*']
}

install_requires = [
    'aiodns',
    'aiohttp',
    'aiohttp-jinja2',
    'aiomysql',
    'aiosmtplib',
    'Jinja2',
    'PyMySQL',
    'requests',
]

setup(
    name='irisett',
    version='1.1.0',
    description='Irisett monitoring engine',
    long_description=long_description,
    author='beebyte AB',
    author_email='simon@beebyte.se',
    url='http://www.github.com/beebyte/irisett/',
    license='MIT',
    packages=packages,
    package_data=package_data,
    scripts=['scripts/irisett', 'scripts/irisett-cli'],
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: System :: Monitoring',
        'Topic :: System :: Networking :: Monitoring',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],
)
