from setuptools import setup, find_packages
classifiers = ["Development Status :: 5 - Production/Stable",
                "Intended Audience :: Education",
                "Operating System :: OS Independent",
                "License :: OSI Approved :: MIT License",
                "Programming Language :: Python :: 3",
                ]

with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="degender_pronoun",
    version="0.1.3",
    description="Replace gender pronouns in a given text with gender-neutral pronouns.",
    long_description=long_description,
    url="",
    author="Xiang Zheng",
    author_email="xiangzheng2021@outlook.com",
    license="MIT",
    classifiers=classifiers,
    keywords="",
    packages=find_packages(),
    py_modules=['degender_pronoun']
)