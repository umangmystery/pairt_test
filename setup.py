import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='custom_log_regression',
    version='0.0.1',
    author='Umang Mistry',
    author_email='some_email@hotmail.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/umangmystery/pairt_test',
    license='MIT',
    packages=['custom_log_regression'],
    install_requires=['scikit-learn'],
)