from setuptools import setup

with open("README.md", "r") as file:
    long_description = file.read()

AUTHOR_NAME = 'QUYEN'
SRC_REPO = 'src'
LIST_OF_REQUIREMENTS = ['streamlit']

setup(
    name=SRC_REPO,
    version='0.0.1',
    author=AUTHOR_NAME,
    author_email='jrnguyen14@gmail.com',
    description='A small example package for movies recommendation system',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/nguyenquyen1910/Movie-Recommendation-System.git',
    packages=[SRC_REPO],
    python_requires = '>=3.11',
    install_requires=LIST_OF_REQUIREMENTS
)