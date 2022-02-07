from setuptools import setup, find_packages
from pathlib import Path

root = Path(__file__).parent.resolve()

description = (
    "A basic yet customisable django app for integration of DataTables.net plugin into"
    "Django 3 projects in the server-side mode."
)
# Get the long description from the README file
long_description = (root / "README.rst").read_text(encoding="utf-8")
url = "https://github.com/hanicinecm/django-datatables-serverside/"
bug_reports = "https://github.com/hanicinecm/django-datatables-serverside/issues"

setup(
    name="django-datatables-serverside",
    version="1.0.0",
    description=description,
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url=url,
    author="Martin Hanicinec",
    author_email="hanicinecm@gmail.com",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Django",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: OS Independent",
    ],
    keywords="django datatables serverside ajax",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.7",
    install_requires=[],
    extras_require={
        "dev": ["django<4", "pytest-cov", "black", "ipython"],
    },
    project_urls={"Bug Reports": bug_reports},
)
