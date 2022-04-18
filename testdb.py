import datetime


class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.test = None
        self.file = None
        self.load()

    def load(self):
        self.file = open(self.filename, "r")
        self.test = {}

        for line in self.file:
            username, password, email, created = line.strip().split(";")
            self.test[username] = (password, email, created)

        self.file.close()

    def get_user(self, username):
        if username in self.test:
            return self.test[username]
        else:
            return -1

    def add_user(self, username, password, email):
        if username.strip() not in self.test:
            self.test[username.strip()] = (password.strip(), email.strip(), DataBase.get_date(self))
            self.save()
            return 1
        else:
            print("Email exists already!")
            return -1

    def validate(self, username, password):
        if self.get_user(username) != -1:
            return self.test[username][1] == password
        else:
            return False

    def save(self):
        with open(self.filename, "w") as f:
            for user in self.test:
                f.write(user + ";" + self.test[user][0] + ";" + self.test[user][1] + ";" + self.test[user][2] + "\n")

    def get_date(self):
        return str(datetime.datetime.now()).split(" ")[0]
