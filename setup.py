import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyraptorq",
    version="0.1.7",
    author="Maksim Kurbatov",
    author_email="cyrbatoff@gmail.com",
    description="RaptorQ RFC6330 C++ bindings for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages('.', exclude=['.idea', 'tests', 'examples']),
    package_data={'pyraptorq': ['distlib/**/*']},
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries",
    ],
    url="https://github.com/yungwine/pyraptorq",
    python_requires='>=3.9',
    py_modules=["pyraptorq"]
)
