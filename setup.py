from setuptools import setup

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='mirthpy',
    version="1.0.0",    
    description='A python package to communicate with mirth connects client api.',
    url='https://github.com/feathersct/mirthpy',
    author='Clayton Feathers',
    author_email='claytonfeathers@live.com',
    license='BSD 2-clause',
    packages=['mirthpy'],
    install_requires=['requests'                 
                      ],
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Healthcare Industry',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: OS Independent',        
        'Programming Language :: Python :: 3'
    ],
)