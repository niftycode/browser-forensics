from setuptools import setup, find_packages

setup(
    name='browser_forensics',
    version='1.2.1',
    license='MIT',
    description='Analyze the history file of browsers',

    author='Bodo Schönfeld',
    author_email='python@niftycode.de',
    url='https://github.com/niftycode/browser_forensics',

    packages=find_packages(where='src'),
    package_dir={'': 'src'},

    install_requires=['pytest'],
    tests_require=['pytest'],
)
