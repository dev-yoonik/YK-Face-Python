
![https://yoonik.me/wp-content/uploads/2019/08/cropped-LogoV4_TRANSPARENT.png](https://yoonik.me/wp-content/uploads/2019/08/cropped-LogoV4_TRANSPARENT.png)

# YooniK Face API: Python SDK & Sample

[![PyPi Version](https://img.shields.io/pypi/v/yk_face.svg)](https://pypi.org/project/yk-face/)
[![License](https://img.shields.io/pypi/l/yk_face.svg)](https://github.com/dev-yoonik/YK-Face-Python/blob/master/LICENSE)

This repository contains the Python SDK for the YooniK Face API, an offering within [YooniK Services](https://yoonik.me)

For more information please [contact us](mailto:info@yoonik.me).

## Getting started

Install the module using [pip](https://pypi.python.org/pypi/pip/):

```bash
pip install yk_face
```

Use it:

```python
import yk_face as YKF

KEY = 'subscription key'  # Replace with a valid Subscription Key here.
YKF.Key.set(KEY)

BASE_URL = 'YooniK Face API URL'  # Replace with a valid URL for YooniK Face API.
YKF.BaseUrl.set(BASE_URL)

img_file_path = 'image path'  # Replace with a valid image file path here.
detected_faces = YKF.face.process(img_file_path)
print(f'Detected faces: {detected_faces}')
```

### Installing from the source code

```bash
python setup.py install
```

## Running the sample

A sample python script is also provided. Please check the sample directory in this repository.



