from google.cloud import storage
from os import remove


def create_bucket():
    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket('kuza_audio')
        bucket.storage_class = 'STANDARD'
        storage_client.create_bucket(bucket, location='ASIA-NORTHEAST3')
    except Exception as e:
        print(e)
        return 'Fatal:구글 클라우드 스토리지 버킷 생성에 실패하였습니다.'
    return None


def upload_audio_file():
    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket('kuza_audio')
        blob = bucket.blob('audio_file')
        blob.upload_from_filename('./audio.mp3')
    except Exception as e:
        print(e)
        return 'Fatal:오디오 파일 업로드에 실패하였습니다.'
    return None


def delete_audio_file():
    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket('kuza_audio')
        blob = bucket.blob('audio_file')
        blob.delete()
        remove('./audio.mp3')
    except Exception as e:
        print(e)
        return 'Error:오디오 파일 삭제에 실패하였습니다.'
    return None
