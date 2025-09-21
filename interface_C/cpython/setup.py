from setuptools import setup, Extension

# Define the C extension
module = Extension('extensions', sources=['extensions_c_sources/extension.c'])

# Call setup to build the package
setup(
    name='extensions-c',
    version='1.0.0',
    description='demonstration extensions c avec cpython',
    ext_modules=[module],  # Include the C extension
)
