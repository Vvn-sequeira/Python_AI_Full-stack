from passlib.context import CryptContext
from jose import jwt 
from datetime import datetime , timedelta


SECRET_KEY='DJFALJD'
ALOGRITHM='HS256'

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

