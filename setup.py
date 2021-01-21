from distutils.core import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='is_valid_date',
    packages=['is_valid_date'],
    version='0.1.0',
    license='MIT',
    description='Check if a date is valid',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Roger Vilà',
    author_email='rogervila@me.com',
    url='https://github.com/rogervila/python_is_valid_date',
    download_url='https://github.com/rogervila/python_is_valid_date/archive/0.1.0.tar.gz',
    keywords=['valid date', 'check date', 'validate date'],
    install_requires=[],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
    ],
)
