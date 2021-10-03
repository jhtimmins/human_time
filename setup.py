#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="human_time",
    version="0.0.1",
    description="Makes Datetimes human-readable",
    long_description=long_description,
    author="James Timmins",
    author_email="jameshtimmins@gmail.com",
    url="https://github.com/jhtimmins/human_time",
    install_requires=[],
    packages=setuptools.find_packages(where="src"),
    entry_points={},
    py_modules=["human_time"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    python_requires=">=3.6",
)
