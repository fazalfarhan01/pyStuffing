import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyStuffing",  # Replace with your own username
    version="0.0.3",
    author="Mohamed Farhan Fazal",
    author_email="fazal.farhan@gmail.com",
    description="A Python package for performing Bit Stuffing and Byte Stuffing operations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fazalfarhan01/Networking-CPT-Files/",
    project_urls={
        "Bug Tracker": "https://github.com/fazalfarhan01/Networking-CPT-Files/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    python_requires=">=3.6",
    install_requires=[
        "colorama>=0.4.4",
    ],
)
