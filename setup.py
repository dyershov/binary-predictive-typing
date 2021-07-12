#!/usr/bin/env python

import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

package_dir={'': 'src'}
packages = setuptools.find_packages(where='src')

install_requires = [
    'pysimplegui',
    'fast_autocomplete[levenshtein]'
]

setuptools.setup(name='multiple_choice_predictive_typing',
                 version='0.1',
                 author='Dmitry Yershov',
                 author_email='dmitry.s.yershov@gmail.com',
                 description='Multiple choice predictive typing',
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 url="https://github.com/dyershov/multiple-choice-predictive-typing",
                 package_dir=package_dir,
                 packages=packages,
                 scripts=['scripts/mcpt'],
                 package_data={'mcpt': ['data/*']},
                 install_requires=install_requires
                 )
