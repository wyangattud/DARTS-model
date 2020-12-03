from setuptools import setup, find_packages, Distribution
import os

# custom class to inform setuptools about self-comiled extensions in the distribution
# and hence enforce it to create platform wheel
class BinaryDistribution(Distribution):
    def has_ext_modules(foo):
        return True

with open('README.md', 'r') as fh:
    long_description = fh.read()

print ("Creating version info file... ")
with open(os.path.join('darts', 'build_info.txt'), 'w') as fp:
    import datetime
    import getpass
    import socket
    import subprocess

    build_date = datetime.datetime.now()
    fp.write(build_date.strftime("%d/%m/%Y %H:%M:%S\n"))

    username = getpass.getuser()
    hostname = socket.gethostname()
    fp.write("%s@%s\n" % (username, hostname))

    git_hash = subprocess.run(['git', 'describe', '--always', '--dirty'], stdout=subprocess.PIPE)
    fp.write(git_hash.stdout.decode('utf-8'))

setup(
    # Application name:
    name='darts',

    # Version number (initial):
    version='0.1.0',

    # Application author details:
    author='Mark Khait',
    author_email='m.khait@tudelft.nl',

    # Packages
    packages=find_packages(),


    # Now only include already built libraries
    package_data={'darts': ['*.pyd', '*.so', '*.dll', 'html/*.*', 'build_info.txt']},
    data_files = [('',['LICENSE'])],

    description='Delft Advanced Research Terra Simulator',
    long_description=long_description,

    # Details
    url='https://darts.citg.tudelft.nl/',

    #
    license='MIT',

    # Dependent packages (distributions)
    install_requires=['matplotlib','numpy', 'scipy', 'pandas', 'meshio==3.3.1', 'plotly', 'xlrd', 'pykrige', 'openpyxl'],

    classifiers=[
        'Programming Language :: Python :: 3',
	    'Programming Language :: C++',
        'License :: OSI Approved :: MIT License',
    ],
    distclass=BinaryDistribution,
)
print ("Embedded build info:")
with open(os.path.join('darts', 'build_info.txt'), 'r') as f:
    print(f.read())
print ("Removing build info file")
os.remove(os.path.join('darts', 'build_info.txt'))
