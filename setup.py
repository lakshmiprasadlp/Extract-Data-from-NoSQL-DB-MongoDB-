from setuptools import setup, find_packages

setup(
    name='lp_pymango',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'pandas>=1.0.0',
        'pymongo>=3.11.0',
        'urllib'
    ],
    entry_points={
        'console_scripts': [
            'myproject=myproject.cli:main',
        ],
    },
    author='lakshmipreasdlp',
    author_email='soetemp2300.com',
    description='A short description of your project',
    long_description='A longer description of your project',
    long_description_content_type='text/markdown',
    url='https://github.com/lakshmiprasadlp/Extract-Data-from-NoSQL-DB-MongoDB-',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
