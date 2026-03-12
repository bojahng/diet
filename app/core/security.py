from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt

pwd_context = CryptContext(schemes=[" bcrypt],
