# pyraptorq


[![PyPI version](https://badge.fury.io/py/pyraptorq.svg)](https://badge.fury.io/py/pyraptorq) 
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyraptorq)](https://pypi.org/project/pyraptorq/)
![](https://pepy.tech/badge/pyraptorq) 
[![Downloads](https://static.pepy.tech/badge/pyraptorq)](https://pepy.tech/project/pyraptorq) 

Python bindings with RaptorQ implementation.

## Examples

You can find usage example in the [/examples](/examples) folder.

## Supported platforms

* Linux (x86_64)
* MacOS (arm64)
* should be more in future

## How to install

### From pypi, if your system is supported

```bash
pip install pyraptorq
```

### From source 



* Compile shared library as described in [cpp-raptorq/README.md](https://github.com/yungwine/cpp-raptorq?tab=readme-ov-file#compile-from-sources)
* Create instance of `RaptorQCppEngine` with path to shared library as argument and provide it to `Decoder` and `Encoder`.

```python
from pyraptorq import Encoder, Decoder, RaptorQCppEngine


engine = RaptorQCppEngine('path_to_lib')
encoder = Encoder(b'data', 2, engine)
decoder = Decoder(2, 2, 4, engine)
```
