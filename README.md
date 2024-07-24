# Repository Coverage

[Full report](https://htmlpreview.github.io/?https://github.com/IliasIB/lijnpy/blob/python-coverage-comment-action-data/htmlcov/index.html)

| Name                            |    Stmts |     Miss |   Cover |   Missing |
|-------------------------------- | -------: | -------: | ------: | --------: |
| lijnpy/\_\_init\_\_.py          |        4 |        0 |    100% |           |
| lijnpy/\_rest\_adapter.py       |       47 |       30 |     36% |47-50, 73-112, 124, 139, 156 |
| lijnpy/enums.py                 |       23 |        0 |    100% |           |
| lijnpy/kods\_client\_v1.py      |       61 |        2 |     97% |  138, 154 |
| lijnpy/models.py                |      137 |        6 |     96% |269-271, 367-369 |
| tests/test\_kods\_client\_v1.py |      111 |        0 |    100% |           |
|                       **TOTAL** |  **383** |   **38** | **90%** |           |


## Setup coverage badge

Below are examples of the badges you can use in your main branch `README` file.

### Direct image

[![Coverage badge](https://raw.githubusercontent.com/IliasIB/lijnpy/python-coverage-comment-action-data/badge.svg)](https://htmlpreview.github.io/?https://github.com/IliasIB/lijnpy/blob/python-coverage-comment-action-data/htmlcov/index.html)

This is the one to use if your repository is private or if you don't want to customize anything.

### [Shields.io](https://shields.io) Json Endpoint

[![Coverage badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/IliasIB/lijnpy/python-coverage-comment-action-data/endpoint.json)](https://htmlpreview.github.io/?https://github.com/IliasIB/lijnpy/blob/python-coverage-comment-action-data/htmlcov/index.html)

Using this one will allow you to [customize](https://shields.io/endpoint) the look of your badge.
It won't work with private repositories. It won't be refreshed more than once per five minutes.

### [Shields.io](https://shields.io) Dynamic Badge

[![Coverage badge](https://img.shields.io/badge/dynamic/json?color=brightgreen&label=coverage&query=%24.message&url=https%3A%2F%2Fraw.githubusercontent.com%2FIliasIB%2Flijnpy%2Fpython-coverage-comment-action-data%2Fendpoint.json)](https://htmlpreview.github.io/?https://github.com/IliasIB/lijnpy/blob/python-coverage-comment-action-data/htmlcov/index.html)

This one will always be the same color. It won't work for private repos. I'm not even sure why we included it.

## What is that?

This branch is part of the
[python-coverage-comment-action](https://github.com/marketplace/actions/python-coverage-comment)
GitHub Action. All the files in this branch are automatically generated and may be
overwritten at any moment.