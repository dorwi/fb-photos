from setuptools import setup, find_packages


# Note: format `dependency~=MAJOR.MINOR` ensures that only MAJOR version is locked.
install_requires = [
    "facebook-sdk==3.1.0",
]

dev_requires = [
    "black==19.10b0",
    "flake8>=3.3",
    "pip-tools==4.3.0",
]

setup(
    name="fb-photos",
    version="0.0.1",
    url="git@github.com:dorwi/fb-photos.git",
    author="dorwi",
    author_email="vidor.kanalas@gmail.com",
    description="Download fb photos",
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=install_requires,
    python_requires=">=3.8.0",
    setup_requires=["pytest-runner"],
    tests_require=dev_requires,
    extras_require={"dev": dev_requires},
)