from database import Session
import tables


class UsersService:
    def __init__(self):
        self.session = Session()

    def get_list(self):
        users = self.session.query(tables.Users).all()
        self.session.close()
        return users
    
    def create(self, tg_id, username, name):
        users = self.get_list()
        if not tg_id in [user.tg_id for user in users]:
            user = tables.Users(
                tg_id=tg_id,
                username=username,
                name=name
            )
            self.session.add(user)
            self.session.commit()
            self.session.close()
            return True
        return False