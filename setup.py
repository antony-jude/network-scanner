#!/usr/bin/env python3
"""
Network Scanner - Lightweight vulnerability scanner
A simple tool for port scanning and security assessment
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="network-scanner",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A lightweight network vulnerability scanner for authorized security testing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/network-scanner",
    py_modules=["scanner"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Information Technology",
        "Topic :: System :: Networking",
        "Topic :: Security",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "network-scanner=scanner:main",
        ],
    },
)
