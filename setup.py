from setuptools import setup

setup(
    name = "usa",
    version = "0.1.0",
    description = "Prints USA flag",
    author = "AitzazImtiaz",
    url = "https://github.com/Terminal-Patriotism/USA-flag-terminal",
    packages = ["usa"],
    entry_points = {
        'console_scripts': [
            'usa = usa.__main__'
        ]
    },
)
