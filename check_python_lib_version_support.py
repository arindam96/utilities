'''
AUTHOR: Arindam Chatterjee
DATED: 3rd May, 2024

INPUT: List of python packages which are available for installation via pip
OUTPUT: Supported python versions for each package
'''
import json
import pprint
from urllib import request

PATTERN: str = 'Programming Language :: Python :: ' # constant pattern

# Put your input here
package_list = ['snowflake-connector-python', 'chromadb', 'streamlit', 'langchain', 'langchain-community', 'tiktoken', 'openai']


def get_supported_python_version(package_name: str) -> list[str]:
    '''
    Given a pip supported python package name, returns a list containing all the python versions it supports
    '''
    with request.urlopen(f'https://pypi.org/pypi/{package_name}/json') as response:
        data = json.loads(response.read())

    list_of_items: list[str] = data['info']['classifiers']
    list_of_python_versions: list[str] = []
    for item in list_of_items:
        if PATTERN in item:
            list_of_python_versions.append(item.replace(PATTERN, ''))
            # pprint.pprint(item.replace(PATTERN, ''))
    return list_of_python_versions


def print_supported_python_version(package_list: list[str]):
    '''
    Given a list of python libs, pretty prints out the supported python versions for each in separate lines
    '''

    # Dictionary Sort package_list
    package_list.sort()

    # find out max str length across all packages
    width = max([len(package) for package in package_list])
    # print(f"Max Width: {width}")

    print("\nPrinting Package Supported Python versions ...")
    print('-' * 100)
    print(f"{'PACKAGE':{width}} : SUPPORTED_VERSION")
    print('-' * 100)
    for package in package_list:
        list_of_python_versions = get_supported_python_version(package)
        list_of_python_versions.sort()
        print(
            f"{package:{width}} : {str(list_of_python_versions).replace('[','').replace(']','')}")
    print('-' * 100)


print_supported_python_version(package_list)
