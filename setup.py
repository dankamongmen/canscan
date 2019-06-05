from setuptools import setup, find_packages

setup(
    name="canScan",
    version="0.0.1",
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
    classifiers=[
        'Development Status :: 3 - Alpha',
    ],
)
