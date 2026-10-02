from setuptools import setup, find_packages

setup(
    name="kovi-sdk",  # Change this to "kovi" if the name is available on PyPI
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0"
    ],
    author="TechEval.ai",
    author_email="contact@techeval.ai",
    description="Official Python SDK for Kovi AI Interview Platform",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/apparao-aremanda/kovi-ai-interview-agent",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
