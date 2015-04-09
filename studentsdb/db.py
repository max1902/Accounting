import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'https://mystudentdb.herokuapp.com/',
        'USER': 'students_db_user',
        'PASSWORD': '111111',
        'NAME': 'students_db',
	
    }
}
