import time
import boto3
import json

transcribe = boto3.client('transcribe')
s3 = boto3.resource('s3')

## 실험
job_name = "test"  ## Job 이름

bucket_name ='kofac-demo-<이름>' 
prefix = 'transcribe/input' ## S3 bucket 내 음성파일을 upload 한 폴더 명
media_filename = 'speech.mp3' 

MediaFileUri = "s3://{}/{}/{}".format(bucket_name, prefix, media_filename)
MediaFormat = media_filename.split('.')[1]

from botocore.exceptions import ClientError
s3_client = boto3.client('s3')
region_name=boto3.session.Session().region_name

try:
    transcribe.delete_transcription_job(TranscriptionJobName=job_name)
except:
    pass

## Amazon Transcribe로 STT job을 실행
transcribe.start_transcription_job(
    TranscriptionJobName=job_name,
    Media={'MediaFileUri': MediaFileUri},
    MediaFormat=MediaFormat,
    LanguageCode='ko-KR'
)

## Transcribe job 완료 확인
while True:
    status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
    if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
        print("===완료!===")
        break
    print("===진행중===")
    time.sleep(5)


