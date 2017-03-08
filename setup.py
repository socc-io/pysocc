from distutils.core import setup

py_modules = [i for i in open('requirements.txt','r').read().split()]

setup(
	name='pysocc',
	version='1.0',
	description='SOCC Python Flask API Server Application',
	author='SOCC',
	author_email='',
	url='https://github.com/socc-io/pysocc.git',
	py_modules=py_modules
)
