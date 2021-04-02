from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="yk_face",
    version="0.1.2",
    description="Python SDK for the YooniK Face API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="YooniK",
    author_email="tech@yoonik.me",
    url="https://github.com/dev-yoonik/YK-Face-Python",
    license='MIT',
    packages=["yk_face"],
    install_requires=[
        'yk-face-api-model',
        'requests',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)