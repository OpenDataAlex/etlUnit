# How to contribute

Any and all contributions, bug reports, bug fixes, enhancement requests, and ideas are definitely welcome to the etlUnit project!

## Getting Started

* Create a new, Python 2.7+ virtualenv and install the requirements via pip: 

        $ pip install -r requirements.txt

* Make sure you have a [GitHub account](https://github.com/signup/free)
* Submit issues/suggestions to the [Github issue tracker](https://github.com/dbaAlex/etlUnit/issues)
  * For bugs, clearly describe the issue including steps to reproduce
  * For enhancement requests, be sure to indicate if you are willing to work on implementing the enhancement
    * Fork the repository on GitHub if you want to contribute code/docs

## Making Changes

* `etlUnit` uses [git-flow](http://nvie.com/posts/a-successful-git-branching-model/) as the git branching model
  * **All commits should be made to the develop branch** 
  * [Install git-flow](https://github.com/nvie/gitflow) and create a `feature` branch with the following command: 
        
            $ git flow feature start <name of your feature>

* Make commits of logical units with complete documentation.
* Check for unnecessary whitespace with `git diff --check` before committing.
* Make sure you have added the necessary tests for your changes. 
  * Test coverage is currently tracked via [coveralls.io](https://coveralls.io/r/dbaAlex/etlUnit?branch=develop)
  * Aim for 100% coverage on your code (Though I did not do this initially...)
    * If this is not possible, explain why in your commit message. This may be an indication that your code should be refactored.
* Run `python setup.py test` to make sure your tests pass
* Run `coverage run setup.py test --source=etlunit` if you have the `coverage` package installed to generate coverage data
* Check your coverage by running `coverage report`

## Submitting Changes

* Push your changes to the feature branch in your fork of the repository.
* Submit a pull request to the main repository

# Additional Resources

* [General GitHub documentation](http://help.github.com/)
* [GitHub pull request documentation](http://help.github.com/send-pull-requests/)
