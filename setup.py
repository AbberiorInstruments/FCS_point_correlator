from setuptools import setup, find_packages

setup(name='focuspoint',
	version='0.1',
	author='Dominic Waithe',
	install_requires=['numpy','scipy','lmfit','pypng','matplotlib','cython'],
	include_package_data=True,
	packages = ['focuspoint'],
	entry_points={
        'console_scripts': [
            'sample=sample:main',
        ],
    },


	)
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy

setup(
    include_dirs=[numpy.get_include()] ,cmdclass = {'build_ext': build_ext},
    ext_modules = [Extension("fib4", ["fib4.pyx"])]
)