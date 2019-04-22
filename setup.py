from setuptools import setup, find_packages

setup(
    name='browser_forensics',
    version='1.2.2',
    license='MIT',
    description='Analyze the history file of browsers',

    author='Bodo Schönfeld',
    author_email='bodo.schoenfeld@niftycode.de',
    url='https://github.com/niftycode/browser_forensics',

    packages=find_packages(exclude=('tests', 'docs')),
    # package_dir={'': 'browser_forensics'},

    install_requires=['pytest'],
    tests_require=['pytest'],
)
