import boto3

polly_client = boto3.Session(profile_name='default',
region_name='ap-northeast-2').client('polly')

response = polly_client.synthesize_speech(VoiceId='Seoyeon',
                OutputFormat='mp3', 
                Text = '안녕하세요. 오늘 세션 어떠셨나요? 오늘 세션이 조금이나마 도움이 되셨으면 좋겠습니다. 감사합니다.',
                Engine = 'neural')

file = open('speech.mp3', 'wb')
file.write(response['AudioStream'].read())
file.close()