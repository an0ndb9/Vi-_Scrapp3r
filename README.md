# Vi_Scrapp3r
Simple scrapper for getting student ID card photos from our college portal. This tool must need a valid GR number to get passport size photo of any student !


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies.

```bash
pip install -r requirements.txt
```

## Usage

```python
python vi_scrapp3r.py <GR_Number>

Example:

python vi_scrapp3r.py 21820144

![test](../media/images/Usage.png)
```

## Additional Info:
This project is not intended for any malicious purpose ! While browsing through our college portal I found out the AWS storage where all photos are stored by simple naming conventions and can be scrapped. 


## License
[MIT](https://choosealicense.com/licenses/mit/)