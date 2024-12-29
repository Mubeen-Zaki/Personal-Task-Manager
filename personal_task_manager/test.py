from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"])

password = pwd_context.hash("test")
print(password)