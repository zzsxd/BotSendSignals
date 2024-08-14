class TempUserData:
    def __init__(self):
        super(TempUserData, self).__init__()
        self.__user_data = {}

    def temp_data(self, user_id):
        if user_id not in self.__user_data.keys():
            self.__user_data.update({user_id: [None, None, None, [None, None], None]})
        return self.__user_data


class DbAct:
    def __init__(self, db):
        super(DbAct, self).__init__()
        self.__db = db


    def get_user_id_from_topic(self, topic_id):
        data = self.__db.db_read("SELECT user_id FROM users WHERE topic_review_id = ?", (topic_id, ))
        if len(data) > 0:
            return data[0][0]

    def add_user(self, user_id, first_name, last_name, nick_name):
        if not self.user_is_existed(user_id):
            self.__db.db_write('INSERT INTO users (user_id, first_name, last_name, nick_name, question_open, have_bonus) VALUES (?, ?, ?, ?, ?, ?)', (user_id, first_name, last_name, nick_name, False, False))


    def user_is_existed(self, user_id):
        data = self.__db.db_read('SELECT count(*) FROM users WHERE user_id = ?', (user_id, ))
        if len(data) > 0:
            if data[0][0] > 0:
                status = True
            else:
                status = False
            return status

    def update_review_id(self, user_id, topic_review_id):
        self.__db.db_write('UPDATE users SET topic_review_id = ? WHERE user_id = ?', (topic_review_id, user_id))