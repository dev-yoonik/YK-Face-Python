from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="yk_face",
    version="0.1.0",
    description="Python SDK for the YooniK Face API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="YooniK",
    email="tech@yoonik.me",
    url="",
    packages=["yk_face"],
    install_requires=[
        'yk-face-api-model',
        'requests',
    ]
)