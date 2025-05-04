from setuptools import setup, find_packages

setup(
    name="ds5100_final_project",
    version="0.1.0",
    description="Weighted‐die Game & Analyzer for DS5100 Final Project",
    author="Hang Yu",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas"
    ]
)
