#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', 'requests>=2.25', 'colorama>=0.4']

test_requirements = ['pytest>=3', ]

setup(
    author="Oren Izmirli",
    author_email='dev@izmirli.org',
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
    description="Testing given URLs HTTP respond status code.",
    entry_points={
        'console_scripts': [
            'uptimer=uptimer.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='uptimer',
    name='uptimer',
    packages=find_packages(include=['uptimer', 'uptimer.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/izmirli/uptimer',
    version='0.1.0',
    zip_safe=False,
)
