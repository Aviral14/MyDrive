import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
import os


def initialize(bucket_name):
	try:
		credential_path = 'service_account_key.json'
		os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
		default_app = firebase_admin.initialize_app()
		if not bucket_name:
			bucket_name='drf-project-b3027.appspot.com'
		return storage.bucket(name=bucket_name)
	
	except:
		if not bucket_name:
			bucket_name='drf-project-b3027.appspot.com'
		return storage.bucket(name=bucket_name)

def upload_files(source_file_path, destination_blob_name,bucket_name=None):
	bucket=initialize(bucket_name)
	blob=bucket.blob(destination_blob_name)
	blob.upload_from_filename(source_file_path)
	print('File %s Successfully Uploaded to Cloud Storage'%(destination_blob_name,))


def list_files(prefix, delimiter=None,bucket_name=None):
	bucket=initialize(bucket_name)
	blobs=bucket.list_blobs(prefix=prefix, delimiter=delimiter)

	list=[]	
	for blob in blobs:
        	list.append(blob.name)
	print(list)

	if delimiter:
        	print('Prefixes:')
        	for prefix in blobs.prefixes:
            		print(prefix)


def download_files(source_blob_name, destination_file_name,bucket_name=None):
	bucket=initialize(bucket_name)
	blob=bucket.blob(source_blob_name)
	blob.download_to_filename(destination_file_name)

	print('Successfully Downloaded file %s from Cloud Storage as %s'%(source_blob_name,destination_file_name))


def update_files(blob_name, new_name,bucket_name=None):
	bucket=initialize(bucket_name)
	blob=bucket.blob(blob_name)
	new_blob=bucket.rename_blob(blob,new_name)
	print('File %s has been renamed to %s'%(blob_name, new_blob.name))


def delete_files(blob_name,bucket_name=None):
	bucket=initialize(bucket_name)
	blob = bucket.blob(blob_name)
	blob.delete()
	
	print('File %s has been Successfully deleted.'%(blob_name,))





