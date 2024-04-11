#####################################
#            Created by             #
#                SBR                #
#####################################
import os
import sqlite3


#####################################


class DB:
    def __init__(self, path, lock):
        super(DB, self).__init__()
        self.__lock = lock
        self.__db_path = path
        self.__cursor = None
        self.__db = None
        self.init()

    def init(self):
        if not os.path.exists(self.__db_path):
            self.__db = sqlite3.connect(self.__db_path, check_same_thread=False)
            self.__cursor = self.__db.cursor()
            self.__cursor.execute('''
            CREATE TABLE users(
            row_id INTEGER primary key autoincrement not null,
            user_id INTEGER,
            topic_question_id INTEGER,
            topic_review_id INTEGER,
            photo_review INTEGER,
            first_name TEXT,
            last_name TEXT,
            nick_name TEXT,
            phone_number TEXT,
            have_bonus BOOL,
            question_open BOOL,
            UNIQUE(user_id)
            )
            ''')
            self.__cursor.execute('''
            CREATE TABLE actions(
            row_id INTEGER primary key autoincrement not null,
            time INTEGER,
            nick_tg INTEGER,
            request_type INTEGER
            )
            ''')
            self.__db.commit()
        else:
            self.__db = sqlite3.connect(self.__db_path, check_same_thread=False)
            self.__cursor = self.__db.cursor()

    def db_write(self, queri, args):
        self.set_lock()
        self.__cursor.execute(queri, args)
        self.__db.commit()
        self.realise_lock()

    def db_read(self, queri, args):
        self.set_lock()
        self.__cursor.execute(queri, args)
        self.realise_lock()
        return self.__cursor.fetchall()

    def set_lock(self):
        self.__lock.acquire(True)

    def realise_lock(self):
        self.__lock.release()
