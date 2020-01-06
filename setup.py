import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="zero-divisor-graph",
    version="1.0.0",
    description="a library for working with zero divisor graphs of commutative semigroups",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Paulcappaert/zero-divisor-graph",
    author="Paul Cappaert",
    author_email="paul.cappaert@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=["numpy"],
)
