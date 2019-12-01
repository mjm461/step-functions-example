#!/bin/bash

if [[ $# -ge 1 ]]
then
    STAGE=$1
else
    STAGE=dev
fi

export STAGE
REGION=us-west-2

# awslocal stepfunctions create-state-machine \
#     --region ${REGION} \
#     --name example-state-machine  \
#     --role-arn arn:aws:iam::000000000000:role/service-role/MyRole --definition file://example-state-machine.json

awslocal s3api create-bucket \
    --region ${REGION} \
    --bucket ${STAGE}-example-bucket

# awslocal lambda invoke --function-name dev-entrystep --payload '{"key": "value"}' out
awslocal lambda create-function \
    --region ${REGION} \
    --function-name=${STAGE}-entrystep \
    --runtime=python3.7 --role=arn:aws:iam::000000000000:role/service-role/MyRole \
	  --handler=handler.lambda_handler \
	  --environment Variables='{LOCALSTACK_URL=http://docker.for.mac.localhost,MIN_CHARS="2",MAX_CHARS="3",WORD_SERVICE_BASE="http://docker.for.mac.localhost:5000"}' \
	  --zip-file fileb://wordstep/target/wordstep-SNAPSHOT.zip
