class Singleton:
    def __init__(self):
        self.first_instance = None

    def singleton(self):
        pass

    def get_instance(self):
        if self.first_instance == None:
            self.singleton()  # lazy instantiation
        return self.first_instance
