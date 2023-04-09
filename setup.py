
#!/usr/bin/env python3

from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent

setup(
    name="pegma",
    version="1.0.11",
    description="Package for Exploratory Ground Motion Analysis",
    long_description = (this_directory / "README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/dbpatankar/pegma",
    author="Digvijay Patankar",
    author_email="dbpatankar@gmail.com",
    license="GNU GPLv3",
    # package_dir={"": "src"},
    package_data={
        "pegma": ["defaultConfigs/*.rc"],
    },
    packages=[
        "pegma", "pegma.ui",
    ],
    install_requires=[
        "pyside6",
        "earthquakepy",
        "matplotlib",
        "numpy",
        "scipy",
    ],
    entry_points={
    'console_scripts': [
        'pegma = pegma.main:run_app',
    ],
    },
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
