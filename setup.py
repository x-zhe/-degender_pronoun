from setuptools import setup, find_packages
classifiers = ["Development Status :: 5 - Production/Stable",
                "Intended Audience :: Education",
                "Operating System :: OS Independent",
                "License :: OSI Approved :: MIT License",
                "Programming Language :: Python :: 3",
                ]

long_description = r"See https://github.com/xiangzheng2021/-degender_pronoun."

setup(
    name="degender_pronoun",
    version="0.1.4",
    description="Replace gender pronouns in a given text with gender-neutral pronouns.",
    long_description=long_description,
    url="",
    author="Xiang Zheng",
    author_email="xiangzheng2021@outlook.com",
    license="MIT",
    classifiers=classifiers,
    keywords="https://github.com/xiangzheng2021/-degender_pronoun",
    packages=find_packages(),
    py_modules=['degender_pronoun']
)