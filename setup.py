from setuptools import setup, find_packages

setup(name = "gim",
version = '0.1.0',
python_requires = '>=3',
install_requires = ['cmd2>=0.8.2'],
description = 'Item management utility for roleplaying/adventure game',
url = 'https://www.github.com/morph8hprom/gim',
author = 'Devon Blackburn',
author_email = 'morph8hprom@gmail.com',
license = 'GPL 3.0',
packages = find_packages('src'), package_dir = {'' : 'src'},
include_package_data = True,
package_data = {
'' : ['*.txt'],
'' : ['*.json'],
}
)
