#!/bin/bash

if [[ $# -ge 1 ]]
then
    STAGE=$1
else
    STAGE=dev
fi

export STAGE
REGION=us-west-2

# awslocal stepfunctions start-execution --state-machine-arn arn:aws:states:us-west-2:000000000000:stateMachine:example-state-machine --input '{}'
awslocal stepfunctions create-state-machine \
    --region ${REGION} \
    --name example-state-machine  \
    --role-arn arn:aws:iam::000000000000:role/service-role/MyRole --definition file://example-state-machine.json

awslocal s3api create-bucket \
    --region ${REGION} \
    --bucket dev-example-bucket

# awslocal lambda invoke --function-name dev-wordstep --payload '{"key": "value"}' out
awslocal lambda create-function \
    --region ${REGION} \
    --function-name=${STAGE}-wordstep \
    --runtime=python3.7 --role=arn:aws:iam::000000000000:role/service-role/MyRole \
	  --handler=handler.lambda_handler \
	  --environment Variables='{LOCALSTACK_URL=http://docker.for.mac.localhost,MIN_CHARS="2",MAX_CHARS="3",WORD_SERVICE_BASE="http://docker.for.mac.localhost:5000"}' \
	  --zip-file fileb://wordstep/target/wordstep-SNAPSHOT.zip

# awslocal lambda invoke --function-name dev-storestep --payload '{"startswith": {"prefix": "a", "words": ["a", "aa"]}}' out
awslocal lambda create-function \
    --region ${REGION} \
    --function-name=${STAGE}-storestep \
    --runtime=python3.7 --role=arn:aws:iam::000000000000:role/service-role/MyRole \
	  --handler=handler.lambda_handler \
	  --environment Variables='{BUCKET_NAME=dev-example-bucket,LOCALSTACK_URL=http://docker.for.mac.localhost}' \
	  --zip-file fileb://storestep/target/storestep-SNAPSHOT.zip
