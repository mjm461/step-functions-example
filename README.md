# Step Functions Example
Example template project for developing a set of step functions to complete a task.
The "task" here is get a random prefix to a word, then return all the words that start
with that prefix and store them in an S3 bucket under that prefix.  For example, given
the prefix `word`, this service would store a file in s3 called `word` that contains
thw following words:  `word,words,wordbank,wordsmith,...,etc`

#### Services to accomplish this task
1.  Step function: An execution that is either given a prefix or creates a random one.
This wraps up all the logic for calling the WordService API and storing the response in
an S3 bucket.
2.  WordService API: Example Flask app that has a simple API, when given a prefix,
it returns all the words for that prefix.

## Development
The top level requirements.txt has every package that can be used for development.
It will include all requirements from sub projects. 
```bash
python3.7 -m venv .venv
source venv/bin/actviate
pip install -r requirements.txt
```

**Things to consider during development:**
1.  Clean the environment when upgrading packages that are installed from github,
for example (pyawsstarter) because these packages are cached in .venv and .eggs directories.
Run `make clean` and delete eggs in the .eggs directory before commiting.  From a clean 
git pull, this should not be an issue.  This also includes changes to the examplecommon directory.
2.  Each lambda project has its own setup.py, so each project is really just a subproject,
with its own setup.  This includes things like coverage and dependencies.
3.  **This is just an example**, so please excpect bugs.

## Unit Tests
Every step or package has its own set of unit tests, which most likely
uses the common package (if it is an AWS Lambda).  To run a unit test 
in a package, step1 for
example:
```bash
cd wordstep
make test
```

To run all the units tests, in the top level directory:
```bash
make test
```

## Common AWS Lambda functions
[Common AWS Lambda](https://github.com/mjm461/pyawsstarter) - Includes the base 
classes for for creating a new lambda.

## Creating a New Step (Lambda)
To creat a new step, use [pyscaffold](https://github.com/pyscaffold/pyscaffold/), 
in the top level of the project, in this case step-functions-temlate.  To create new step:

```bash
putup newstep
```

Add a version and common dependency to setup.cfg (if needed)
```
# newstep/setup.cfg

[options]
install_requires = pyawsstarter
dependency_links = git+https://github.com/mjm461/pyawsstarter.git@tox#egg=pyawsstarter
```
Add minimum coverage failure to .coveragerc (ex: 80%)
```
# newstep/.coveragerc

[report]
fail_under = 80
```

Create a new Handler class in ```newstep/newstep.py```, 
see example in [pyawsstarter](https://github.com/mjm461/pyawsstarter). Only create the class
as the handler will be created next as ```handler.py```

Create a handler.py (to be used by the AWS Lambda) if necessary
```python
# newstep/handler.py
from newstep import NewStep

lambda_handler = NewStep().get_handler()
```

Create a Makefile to build this new step
```bash
# newstep/Makefile

BUNDLE := newstep
include ../Makefile.include
```

## Development in an IDE
In this case I am using Pycharm, but to work on a step, make sure ```pip install pyawsstarter```
the common AWS Lambada package and newstep/src are selected as source.  To do this, right click
on one of these directories and select "Mark Direcotory As" -> "Sources Root"

## Deploying the project to Localstack
The `docker` directory contains a docker-compose.yml to get the environment up and running.  This
file spins up two services:
1.  Localstack - Includes everything needed to run the lambdas, s3, etc.
2.  WordService - Example REST API to show how lambdas can call external
services.

To run the example:

#### Test/Build the project
```base
make
```

The lambda functions will be created in the following directories:
```base
storestep/target/storestep-SNAPSHOT.zip
wordstep/target/wordstep-SNAPSHOT.zip
```

#### Run the docker services (including Localstack)
```bash
cd docker
docker-compose up
```

At this point the services required to deploy the lambdas will be ready for you
to upload the lambdas and the stepfunction that uses them.

#### Deploy the Lambdas/Step Function
```bash
./deploy-lambdas.sh
```
This does 3 things:
1.  Creates the S3 bucket that will be needed by the store lambda
2.  Uploads the zip files for the lambdas
3.  Creates the step function that wraps up the lambdas and includes the retry logic

#### Test it!
I like to use ```awslocal``` to do this.  It wraps up the commands used by awscli.  To install
this project ```pip install awscli-local```

Execute the state machine with a prefix, in this case word
```bash
$ awslocal stepfunctions start-execution --state-machine-arn arn:aws:states:us-west-2:000000000000:stateMachine:example-state-machine --input '{"prefix":"word"}'
```

See that the file has been created for word
```bash
$ awslocal s3 ls s3://dev-example-bucket/
2019-12-01 12:30:51        581 word
```

Execute the state machine with a random prefix, this just takes a different argument
to the state machine, in this case an empty JSON:  `{}`:
```bash
$ awslocal stepfunctions start-execution --state-machine-arn arn:aws:states:us-west-2:000000000000:stateMachine:example-state-machine --input '{}'
```

## Terraform Deployment
TODO: maybe in the future