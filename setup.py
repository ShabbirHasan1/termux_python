import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='termux_python-mguillau42',
    version='0.0.1',
    author='mguillau42',
    description='termux python bindings',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mguillau42/termux_python',
    packages=setuptools.find_packages(),
    classifiers= [
       'Programming Language :: Python :: 3',
       'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
       'Operating System :: OS Independent',
   ],
)
