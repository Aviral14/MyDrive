# MyDrive
An API built using Django Rest Framework to upload and access files stored on Firebase Cloud Storage


The API has functionality to-

1.register a user

2.login

3.logout

4.upload files

5.list files for a particular user

6.update filename for a file of a logged in user

7.delete a file of a logged in user



The API endpoints for the above features are-

1.register- http://localhost:8000/api/users/register/

2.login- http://localhost:8000/api/users/login/

3.logout- http://localhost:8000/api/users/logout/

4.upload- http://localhost:8000/api/dashboard/upload_files/

5.list- http://localhost:8000/api/dashboard/list_files/

6.update- http://localhost:8000/api/dashboard/update_files/'filename'/
  
7.delete- http://localhost:8000/api/dashboard/delete_files/'filename'/

  
  
The API uses a Token based Authentication Scheme.So on logging in the user will be provided a token which should be used while accessing API endpoints for list,upload,delete,update and logout features.


This Project has helper functions for firebase in the firebase_utilities folder which can even be used independently.
