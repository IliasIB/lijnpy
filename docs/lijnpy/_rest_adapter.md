# RestAdapter

[Lijnpy Index](../README.md#lijnpy-index) / [Lijnpy](./index.md#lijnpy) / RestAdapter

> Auto-generated documentation for [lijnpy._rest_adapter](../../lijnpy/_rest_adapter.py) module.

- [RestAdapter](#restadapter)
  - [DeLijnAPIException](#delijnapiexception)
  - [RestAdapter](#restadapter-1)
    - [RestAdapter()._do](#restadapter()_do)
    - [RestAdapter().delete](#restadapter()delete)
    - [RestAdapter().get](#restadapter()get)
    - [RestAdapter().post](#restadapter()post)
  - [Result](#result)

## DeLijnAPIException

[Show source in _rest_adapter.py:23](../../lijnpy/_rest_adapter.py#L23)

#### Signature

```python
class DeLijnAPIException(Exception): ...
```



## RestAdapter

[Show source in _rest_adapter.py:26](../../lijnpy/_rest_adapter.py#L26)

#### Signature

```python
class RestAdapter:
    def __init__(
        self,
        hostname: str = "api.delijn.be",
        api_key: str = "",
        ver: str = "v1",
        ssl_verify: bool = True,
        logger: Logger | None = None,
    ): ...
```

### RestAdapter()._do

[Show source in _rest_adapter.py:50](../../lijnpy/_rest_adapter.py#L50)

Perform an HTTP request to the API and return a Result object

#### Arguments

- `http_method` *str* - The HTTP method to use (GET, POST, DELETE)
- `endpoint` *str* - The endpoint on the API to request
ep_params (dict | None, optional): Parameters to give to the endpoint. Defaults to None.
data (dict | None, optional): Data to pass through to the endpoint. Defaults to None.

#### Raises

- [DeLijnAPIException](#delijnapiexception) - If the request fails or the response is not in the 200-299 range

#### Returns

- [Result](#result) - The result of the request

#### Signature

```python
def _do(
    self,
    http_method: str,
    endpoint: str,
    ep_params: dict | None = None,
    data: dict | None = None,
) -> Result: ...
```

#### See also

- [Result](#result)

### RestAdapter().delete

[Show source in _rest_adapter.py:144](../../lijnpy/_rest_adapter.py#L144)

Perform a DELETE request to the API

#### Arguments

- `endpoint` *str* - The endpoint on the API to DELETE
ep_params (dict | None, optional): Parameters to give to the endpoint. Defaults to None.
data (dict | None, optional): Data to pass through to the endpoint. Defaults to None.

#### Returns

- [Result](#result) - The result of the DELETE request

#### Signature

```python
def delete(
    self, endpoint: str, ep_params: dict | None = None, data: dict | None = None
) -> Result: ...
```

#### See also

- [Result](#result)

### RestAdapter().get

[Show source in _rest_adapter.py:115](../../lijnpy/_rest_adapter.py#L115)

Perform a GET request to the API

#### Arguments

- `endpoint` *str* - The endpoint on the API to GET
ep_params (dict | None, optional): Parameters to give to the endpoint. Defaults to None.

#### Returns

- [Result](#result) - The result of the GET request

#### Signature

```python
def get(self, endpoint: str, ep_params: dict | None = None) -> Result: ...
```

#### See also

- [Result](#result)

### RestAdapter().post

[Show source in _rest_adapter.py:127](../../lijnpy/_rest_adapter.py#L127)

Perform a POST request to the API

#### Arguments

- `endpoint` *str* - The endpoint on the API to POST
ep_params (dict | None, optional): Parameters to give to the endpoint. Defaults to None.
data (dict | None, optional): Data to pass through to the endpoint. Defaults to None.

#### Returns

- [Result](#result) - The result of the POST request

#### Signature

```python
def post(
    self, endpoint: str, ep_params: dict | None = None, data: dict | None = None
) -> Result: ...
```

#### See also

- [Result](#result)



## Result

[Show source in _rest_adapter.py:9](../../lijnpy/_rest_adapter.py#L9)

The result of a request to the De Lijn API

#### Attributes

- `status_code` *int* - The status code of the request
- `message` *str, optional* - The message of the request. Defaults to "".
data (dict[str, Any] | None, optional): The data of the request. Defaults to None.

#### Signature

```python
class Result(BaseModel): ...
```