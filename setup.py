"""
`grouper` is a package for performing fast groupby-apply operations.
"""

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="grouper",
    version="0.2.0",
    author="Shreyas Joshi",
    author_email="sjoshistrats@gmail.com",
    description="A package for applying efficient groupby operations.",
    keywords=["grouper", "grouping", "groupby", "fast"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sjoshistrats/grouper",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha"
    ],
    package_dir={"": "python"},
    packages=setuptools.find_packages(where="python"),
    python_requires=">=3.6",
    install_requires=["numpy", "pandas"]
)
