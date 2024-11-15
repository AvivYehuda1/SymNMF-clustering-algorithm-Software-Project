from setuptools import setup, Extension
import numpy

module = Extension('symnmf',
                   sources=['symnmfmodule.c', 'symnmf.c'],
                   include_dirs=[numpy.get_include()])

setup(name='symnmf',
      version='1.0',
      description='Symmetric Non-negative Matrix Factorization',
      ext_modules=[module])
