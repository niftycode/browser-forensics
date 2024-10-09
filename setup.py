from setuptools import setup, find_packages

setup(
    name='browser_forensics',
    version='1.3.0',
    license='MIT',
    description='Analyze the history file of browsers',

    author='Bodo Schönfeld',
    author_email='bodo.schoenfeld@niftycode.de',
    url='https://github.com/niftycode/browser-forensics',

    packages=find_packages(exclude=('tests', 'docs')),

    install_requires=['pytest'],
    tests_require=['pytest'],
)
