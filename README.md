
![](images/carcass_logo.png)

carcass is a Python command line tool to generate python package scaffolding based on best practices

## Getting Started

To use `carcass` you can run it directly.  Since `carcass` is mainly considered a command line tool, once installed, you run it directly:

```bash
# Default generated package path is the current users directory `~/`
carcass

# Provide an alternate path location 
carcass -P ~/my_packages/path
carcass --path ~/my_packages/path
```

Once you run carcass you will be prompted to provide answers to the following questions:

```bash
Enter your package name: mytestpackage
Enter your first and last name: Josh Rickard
Enter your GitHub user name: MSAdministrator
Enter your email address: josh.rickard@letsautomate.it
```

Additionally, you have additional package options that you can select all, some, or none of them using your `space` key.

Currently, `carcass` supports the following additional package options.  I will continue to add additional options as needed/wanted:

```
Please select all package options which you want carcass to generate

 * Logger
   Exceptions
   Microsoft Graph OAuth2

```

### Package Template Structure

`carcass` generates packages based on your provided inputs as well as selected options during creation.

Below is the structure outline for a template python package generated by `carcass` with all options selected:

```bash
package_name
    README.md
    CONTRIBUTING.md
    LICENSE.md
    setup.py
    logger.yml
    .gitignore
    package_name
        __init__.py
        package_name.py
        connector.py
        utils
            __init__.py
            exceptions.py
            logger.py
```

### Installation

In order to use carcass you can install it via `pip` or clone this repository.

```bash
pip install carcass
```

```bash
git clone git@github.com:MSAdministrator/carcass.git
cd carcass
pip install -r requirements.txt
```

### Development

To get a development env running, you can clone this repository

Say what the step will be

```bash
pip install --user pipenv
git clone git@github.com:MSAdministrator/carcass.git
cd carcass
```

Next, install and setup a virtual environment:

```bash
pip install virtualenv
virtualenv venv
pip install -r requirements.txt
carcass
```

## Running the tests

To run unit tests, you will need to clone this repository:

```bash
pip install --user pipenv
git clone git@github.com:MSAdministrator/carcass.git
cd carcass
```

Next, you run tests using the following command:

```bash
python -m pytest 
```

### Break down into end to end tests

Tests within this package test to ensure that the correct files are being created as requested as well as some tests check the contents of the template files:


```
# testing the creation of a README.md template

def test_creation_of_readme_template_exists(carcass_fixture):
    '''
    Testing the creation of README.md template file
    '''
    carcass = carcass_fixture.create_package(pytest.configuration['package_path'], pytest.package)
    assert os.path.exists(os.path.join(str(pytest.configuration['package_path']), 'README.md'))
```

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. 

## Authors

* Josh Rickard - *Initial work* - [MSAdministrator](https://github.com/MSAdministrator)

See also the list of [contributors](https://github.com/MSAdministrator/carcass/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details