from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='pymemoq',
      version='0.2.dev6',
      description='Python module to facilitate accessing the memoQ API.',
      long_description=long_description,
      long_description_content_type='text/x-rst',
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.8",
          "Topic :: Software Development :: Libraries",
          "Topic :: Software Development :: Localization",
      ],
      url='https://github.com/leonidessaguisagjr/pymemoq',
      author='Leonides T. Saguisag Jr.',
      author_email='leonidessaguisagjr@gmail.com',
      license='MIT',
      packages=['memoq'],
      install_requires=['zeep'],
      include_package_data=True,
      zip_safe=False,
      )
