from setuptools import setup

setup(
    name = "usa",
    version = "0.1.0",
    description = "Prints USA flag",
    author = "AitzazImtiaz",
    url = "https://github.com/AitzazImtiaz/usa",
    packages = ["usa"],
    entry_points = {
        'console_scripts': [
            'usa = usa.__main__:main'
        ]
    },
)
