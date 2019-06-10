from setuptools import setup, find_packages
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="canScan",
    version="0.0.2",
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=['canopen>=0.9.0'],
    author="Nick Black",
    author_email="nickblack@linux.com",
    description="CANopen discovery tool/scanner",
    keywords="CAN CANopen scanner",
    license='Apache License, Version 2.0',
    url='https://github.com/dankamongmen/canscan',
    zip_safe=True,
    platforms=["any"],
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    test_suite="nose.collector",
    tests_require=["nose"],
    # see https://pypi.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python',
    ],
)
