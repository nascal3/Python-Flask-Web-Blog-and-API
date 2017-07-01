import uuid

from src.common.database import Database


class User(object):
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    @classmethod
    def get_by_email(cls, email):
        data = Database.DATABASE.find_one(collection='users', query={'email':email})
        if data is not None:
            return cls(**data)

    @classmethod
    def get_by_id(cls, _id):
        data = Database.DATABASE.find_one(collection='users', query={'_id': _id})
        if data is not None:
            return cls(**data)
    @staticmethod
    def login_valid(email, password):
        user = User.get_by_email(email=email)
        if user is not None:
            return user.password == password
        return False

    @classmethod
    def register(cls, email, password):
        user = cls.get_by_email(email=email)
        if user is None:
           new_user = cls(email, password)
           new_user.save_to_mongo()
           return True
        else:
           return False


    def login(self):
        pass

    def get_blogs(self):
        pass

    def json(self):
        pass

    def save_to_mongo(self):
        Database.DATABASE.insert(collection='post', data=self.json())