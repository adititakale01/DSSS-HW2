from setuptools import setup, find_packages
import os

# to get the directory where the setup.py is located
this_directory = os.path.abspath(os.path.dirname(__file__))

# to read the README.md content from the root directory
with open(os.path.join(this_directory, 'README.md'), 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='math_quiz',
    version='0.1',
    packages=find_packages(),  # This will include the math_quiz package
    include_package_data=True,
    install_requires=[],  # Add dependencies here if needed
    entry_points={
        'console_scripts': [
            'math_quiz = math_quiz.math_quiz:mathQuiz',
        ],
    },
    author='Aditi Vishwas Takale',
    author_email='adititakale@fau.de',
    description='My Math Quiz Game',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/adititakale01/DSSS-HW2',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)