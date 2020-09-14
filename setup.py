from setuptools import setup

with open('README.md', 'r') as fh:
    long_description=fh.read()

setup (
    name='helloworldsupreme',
    version='0.0.1',
    description='The most universal piece of code. Ever.',
    py_modules=['helloworldsupreme'],
    package_dir={'': 'src'},
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Operating System :: OS Independent'
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/StoopidSam/HelloWorldSupreme',
    author='StoopidSam',
    author_email='firwoodmedia@gmail.com'
)