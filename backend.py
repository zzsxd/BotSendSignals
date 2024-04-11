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

    def save_photo(self, byte_row, name):
        with open(name, 'wb') as photo:
            photo.write(byte_row)

    def get_user_id_from_topic(self, topic_id):
        data = self.__db.db_read("SELECT user_id FROM users WHERE topic_review_id = ?", (topic_id, ))
        if len(data) > 0:
            return data[0][0]

    def add_user(self, user_id, first_name, last_name, nick_name):
        if not self.user_is_existed(user_id):
            self.__db.db_write('INSERT INTO users (user_id, first_name, last_name, nick_name, question_open, have_bonus) VALUES (?, ?, ?, ?, ?, ?)', (user_id, first_name, last_name, nick_name, False, False))

    def update_question_status(self, user_id, status):
        self.__db.db_write('UPDATE users SET question_open = ? WHERE user_id = ?', (status, user_id))

    def get_question_status(self, topic_id):
        data = self.__db.db_read('SELECT question_open FROM users WHERE topic_question_id = ?', (topic_id,))
        if len(data) > 0:
            if data[0][0] == 1:
                ans = True
            else:
                ans = False
            return ans

    def get_question_status_user_id(self, user_id):
        data = self.__db.db_read('SELECT question_open FROM users WHERE user_id = ?', (user_id,))
        if len(data) > 0:
            if data[0][0] == 1:
                ans = True
            else:
                ans = False
            return ans

    def user_is_existed(self, user_id):
        data = self.__db.db_read('SELECT count(*) FROM users WHERE user_id = ?', (user_id, ))
        if len(data) > 0:
            if data[0][0] > 0:
                status = True
            else:
                status = False
            return status

    def bonus_already_get(self, user_id):
        data = self.__db.db_read('SELECT have_bonus FROM users WHERE user_id = ?', (user_id, ))
        print(data)
        if len(data) > 0:
            if data[0][0] == 1:
                status = True
            else:
                status = False
            return status

    def update_quest_id(self, user_id, topic_question_id):
        self.__db.db_write('UPDATE users SET topic_question_id = ? WHERE user_id = ?', (topic_question_id, user_id))

    def update_review_id(self, user_id, topic_review_id):
        self.__db.db_write('UPDATE users SET topic_review_id = ? WHERE user_id = ?', (topic_review_id, user_id))

    def get_quest_id(self, user_id):
        data = self.__db.db_read('SELECT topic_question_id FROM users WHERE user_id = ?', (user_id, ))
        if len(data) > 0:
            return data[0][0]

    def get_review_id(self, user_id):
        data = self.__db.db_read('SELECT topic_review_id FROM users WHERE user_id = ?', (user_id, ))
        if len(data) > 0:
            return data[0][0]

    def get_phone_numer_from_topic(self, topic_id):
        data = self.__db.db_read('SELECT phone_number FROM users WHERE topic_review_id = ?', (topic_id, ))
        if len(data) > 0:
            return data[0][0]

    def get_question_id(self, topic_id):
        data = self.__db.db_read('SELECT user_id FROM users WHERE topic_question_id = ?', (topic_id, ))
        if len(data) > 0:
            return data[0][0]

    def user_id_from_question_id(self, user_id):
        data = self.__db.db_read('SELECT topic_question_id FROM users WHERE user_id = ?', (user_id, ))
        if len(data) > 0:
            return data[0][0]