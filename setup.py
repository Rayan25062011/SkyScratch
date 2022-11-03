from setuptools import setup

with open("README.md","r") as fh:
    long_description = fh.read()
    
setup(
    name="SkyScratch",
    version="1.2.0",
    description="This is VPN that will disguise 🥸 your identity and encrypt 🔒your network traffic 🚗 Also portable! 📱",
    py_modules=["SkyScratch"],
    package_dir={"":"SkyScratch"},
    classifiers=["Programming Language :: Python :: 3",
                 "Programming Language :: Python :: 3.1",
                 "Programming Language :: Python :: 3.2",
                 "Programming Language :: Python :: 3.3",
                 "Programming Language :: Python :: 3.4",
                 "Programming Language :: Python :: 3.5",
                 "Programming Language :: Python :: 3.6",
                 "Programming Language :: Python :: 3.7",
                 "License :: OSI Approved :: Apache-2.0 license",
                 "Operating System :: OS Independent"
                ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Rayan25062011/SkyScratch",
    author="Rayan25062011"
)

