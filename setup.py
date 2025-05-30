from setuptools import setup, find_packages
from sammcitrixcloud.version import __version__

if __name__ == "__main__":
    setup(
        name='sammcitrixcloud',
        version=__version__,
        packages=find_packages(include=['sammcitrixcloud', 'sammcitrixcloud.*']),
        scripts=[],
        data_files=[],
        install_requires=[ 'python-odata' ]
    )
