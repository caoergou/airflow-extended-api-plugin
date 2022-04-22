from os import path as opath

from setuptools import setup

HERE = opath.dirname(__file__)
VERSION_FILE = opath.join(HERE, 'extended_api', 'VERSION')
README_FILE = opath.join(HERE, 'README.md')

with open(VERSION_FILE) as f:
    version = f.read().strip()

with open(README_FILE, "r") as f:
    long_description = f.read()

setup(
    name="airflow_extended_api",
    version=version,
    include_package_data=True,
    entry_points={
        "airflow.plugins": [
            "extended_api_plugin = extended_api.airflow_extended_api:ExtendedAPIPlugin"
        ]
    },
    zip_safe=False,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/caoergou/airflow-extended-api-plugin",
    author="Eric Cao",
    author_email="itsericsmail@gmail.com",
    description="Yet another Airflow plugin using CLI command as REST-ful API.",
    install_requires=["apache-airflow", "flask-swagger-ui"],
    license="Apache License, Version 2.0",
    python_requires=">=3.4",
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        'Intended Audience :: Developers',
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ]
)
