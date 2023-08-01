#!/bin/bash

#S3 버킷 생성
aws s3 mb s3://kofac-demo-<이름>

cd ~/environment/kofac

#S3로 mp3 파일 복사
aws s3 cp speech.mp3 s3://kofac-demo-<이름>/transcribe/input/