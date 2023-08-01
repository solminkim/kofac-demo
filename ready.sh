#!/bin/bash

sudo yum -y update
sudo yum -y install python3

#pip가 Python 활성 버전에 대해 설치되었는지 확인
python3 -m pip --version

#AWS SDK for Python(boto3) 설치
#boto3를 사용해 AWS의 서비스들을 Python 코드를 통해 사용하실 수 있습니다.
sudo python3 -m pip install boto3

#boto3 설치 확인
python3 -m pip show boto3