#encoding:utf-8
import shutil
import os
from distutils.core import setup, Extension
module = Extension("{{ class_name }}", sources=["{{ class_name }}.c"])
setup(ext_modules=[module],script_args=["build_ext",'-i',"clean","--all"])