# json_schema2adoc
## Requirements
- Python3
- pip

## Running

- Create virtual environment and source it (if required):
```
json-schema2adoc$ mkdir .env
json-schema2adoc$ python3 -m venv .env
json-schema2adoc$ source .env/bin/activate
```
- Install api_from_schema
```
$ pip install git+https://github.com/AAFC-BICoE/json-schema2adoc.git[@branch|@tag]
```


## Usage
The ```generate_api_doc``` entry point can be called directly once the package is installed:
```$ generate_api_doc path/to/schema.json destination/directory/```

To use schemaAdocGeneratorV2.py as a module, import the api_from_schema package from a python interpreter or another module:
```
import api_from_schema.schemaAdocGeneratorV2
```

## Developing

### To contribute to the json-schema2adoc codebase, do the following:
- Clone the repo
```
$ git clone https://github/AAFC-BICoE/json-schema2adoc.git
```
- Switch to the json-schema2adoc directory
```
$ cd json-schema2adoc
```
- Create virtual environment and source it:
```
json-schema2adoc$ mkdir .env
json-schema2adoc$ python3 -m venv .env
json-schema2adoc$ source .env/bin/activate
```

### To simply install an editable version of the package:
- Create and start your virtual environment (if required) 
```
$ mkdir .env
$ python3 -m venv .env
$ source .env/bin/activate
```
- Install editable version of api_from_schema package;
```
$ pip install -e $ pip install git+https://github.com/AAFC-BICoE/json-schema2adoc.git[@branch|@tag]
```

**Note:** For more information on the use of `pip install` see *https://pip.pypa.io/en/stable/reference/pip_install/*.
