from setuptools import setup, find_packages

"""
https://godatadriven.com/blog/a-practical-guide-to-using-setup-py/
https://pythonhosted.org/an_example_pypi_project/setuptools.html
$ python setup.py develop
$ python setup.py develop --uninstall
$ python setup.py test
TODO - find_packages
"""
setup(
    name="dataproc",
    version="0.0.1",
    description=("channel_intelligence_dataproc"),
    packages=find_packages(include=['dataproc', 'dataproc.*']),  # TODO fix
)
