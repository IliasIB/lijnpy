# Repository Coverage

[Full report](https://htmlpreview.github.io/?https://github.com/IliasIB/lijnpy/blob/python-coverage-comment-action-data/htmlcov/index.html)

| Name                                          |    Stmts |     Miss |   Cover |   Missing |
|---------------------------------------------- | -------: | -------: | ------: | --------: |
| lijnpy/\_\_init\_\_.py                        |        2 |        0 |    100% |           |
| lijnpy/kods/\_\_init\_\_.py                   |        0 |        0 |    100% |           |
| lijnpy/kods/api/\_\_init\_\_.py               |        0 |        0 |    100% |           |
| lijnpy/kods/api/v1/\_\_init\_\_.py            |        5 |        0 |    100% |           |
| lijnpy/kods/api/v1/colors.py                  |       23 |        6 |     74% |19-21, 39-41 |
| lijnpy/kods/api/v1/entities.py                |       50 |       15 |     70% |24-26, 44-46, 66-68, 86-88, 106-108 |
| lijnpy/kods/api/v1/enums.py                   |       23 |        0 |    100% |           |
| lijnpy/kods/api/v1/models.py                  |      119 |        0 |    100% |           |
| lijnpy/kods/api/v1/municipalities.py          |       41 |       12 |     71% |25-27, 45-47, 65-67, 85-87 |
| lijnpy/kods/api/v1/stops.py                   |       68 |       21 |     69% |42-44, 66-68, 98-100, 124-126, 148-150, 184-186, 209-211 |
| lijnpy/kods/api/v1/transport\_regions.py      |       32 |        9 |     72% |22-24, 42-44, 62-64 |
| lijnpy/rest\_adapter.py                       |       45 |        7 |     84% |89-91, 112-113, 140, 157 |
| tests/\_\_init\_\_.py                         |        0 |        0 |    100% |           |
| tests/kods/api/v1/test\_colors.py             |       13 |        0 |    100% |           |
| tests/kods/api/v1/test\_entities.py           |       25 |        0 |    100% |           |
| tests/kods/api/v1/test\_municipalities.py     |       23 |        0 |    100% |           |
| tests/kods/api/v1/test\_stops.py              |       51 |        0 |    100% |           |
| tests/kods/api/v1/test\_transport\_regions.py |       17 |        0 |    100% |           |
| tests/test\_rest\_adapter.py                  |       19 |        0 |    100% |           |
| tests/utils.py                                |       18 |        3 |     83% |      8-10 |
|                                     **TOTAL** |  **574** |   **73** | **87%** |           |


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