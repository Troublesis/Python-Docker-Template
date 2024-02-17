import os

from setuptools import find_packages, setup

# # Default values if environment variables are not set
# default_name = "default_project_name"
# default_version = "0.0.1"

# Get environment variables
project_name = os.getenv("PROJECT_NAME")
project_version = os.getenv("PROJECT_VERSION")

setup(
    name=project_name,
    version=project_version,
    author="troublesis",
    author_email="bamboo5320@gmail.com",
    description="A Python docker demo project",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Troublesis",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
