from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def hash_password(user_password):
    return pwd_context.hash(user_password)

def verify_user_password(received_password, user_password):
    return pwd_context.verify(received_password, user_password)