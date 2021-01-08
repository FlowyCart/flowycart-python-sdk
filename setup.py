from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Python SDK for the FlowyCart API'
LONG_DESCRIPTION = 'My first Python package with a slightly longer description'

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name='flowycart',
    version=VERSION,
    author='Carlos Lugones',
    author_email='contact@lugodev.com',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    license='MIT',
    install_requires=['requests'],
    keywords=['FlowyCart', 'api', 'payments'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'
    ],
    project_urls={
        'Documentation': 'https://docs.flowycart.com',
        'Source': 'https://github.com/Flowycart/flowycart-python-sdk',
        'Tracker': 'https://github.com/Flowycart/flowycart-python-sdk/issues'
    }
)
