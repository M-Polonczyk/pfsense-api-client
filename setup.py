"""pfSense REST API Client

### Getting Started<br>- [Authentication and Authorization](https://pfrest.org/AUTHENTICATION_AND_AUTHORIZATION/)<br>- [Working with Object IDs](https://pfrest.org/WORKING_WITH_OBJECT_IDS/)<br>- [Queries, Filters, and Sorting](https://pfrest.org/QUERIES_FILTERS_AND_SORTING/)<br>- [Common Control Parameters](https://pfrest.org/COMMON_CONTROL_PARAMETERS/)<br>- [Working with HATEOAS](https://pfrest.org/WORKING_WITH_HATEOAS/)<br>

Generated with OpenAPI Generator (https://openapi-generator.tech)
"""  # noqa: E501

from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "pfsense-api-client"
VERSION = "1.0.0"
PYTHON_REQUIRES = ">= 3.9"
REQUIRES = [
    "urllib3 >= 2.1.0, < 3.0.0",
    "python-dateutil >= 2.8.2",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="pfSense REST API Client",
    author="M-Polonczyk",
    author_email="m.polonczyk@outlook.com",
    url="https://github.com/M-Polonczyk/pfsense-api-client",
    keywords=["OpenAPI", "OpenAPI-Generator", "pfSense REST API Documentation", "pfSense REST API Client"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="Apache 2.0",
    long_description_content_type="text/markdown",
    long_description="""\
    ### Getting Started&lt;br&gt;- [Authentication and Authorization](https://pfrest.org/AUTHENTICATION_AND_AUTHORIZATION/)&lt;br&gt;- [Working with Object IDs](https://pfrest.org/WORKING_WITH_OBJECT_IDS/)&lt;br&gt;- [Queries, Filters, and Sorting](https://pfrest.org/QUERIES_FILTERS_AND_SORTING/)&lt;br&gt;- [Common Control Parameters](https://pfrest.org/COMMON_CONTROL_PARAMETERS/)&lt;br&gt;- [Working with HATEOAS](https://pfrest.org/WORKING_WITH_HATEOAS/)&lt;br&gt;
    """,  # noqa: E501
    package_data={"pfsense_api_client": ["py.typed"]},
)
