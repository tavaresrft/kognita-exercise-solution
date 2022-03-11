from setuptools import setup, find_packages

setup(
    name='kognita_exercise_solution',
    version='1.0.0',
    packages=find_packages(),
    url='',
    license='',
    author='',
    author_email='',
    description='',
    install_requires=[
        "click==8.0.3",
        "smart-open[all]==5.0.0",
        "jsonlines==2.0.0",
        "pandas==1.4.1",
        "pandas-profiling==3.1.0",
    ],
    entry_points={
        'console_scripts': [
            "extract=salary_extractor_pubsub.main:main"
        ]
    }
)