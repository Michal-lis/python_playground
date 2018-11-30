class Memento:
    def __init__(self, article):
        self.article = article

    def get_saved_article(self):
        return self.article


class Originator:
    def __init__(self):
        self.article = None

    def set(self, new_article):
        print("From Originator: Current version of article:\n" + new_article)
        self.article = new_article

    def store_in_memento(self):
        print("From Originator: Saving to Memento")
        return Memento(self.article)

    def restore_from_memento(self, memento):
        article = memento.get_saved_article()
        print("From Originator: Previous Article Saved in Memento:\n" + article)
        return article


class CareTaker:
    def __init__(self):
        self.saved_articles = []

    def add_memento(self, memento):
        self.saved_articles.append(memento)

    def get_memento(self, index):
        return self.saved_articles[index]


o = Originator()
ct = CareTaker()
o.set("Barbara Krupa")
ct.add_memento(o.store_in_memento())
o.set("Barbara Krupa druga albo i trzeci chuj wie")
ct.add_memento(o.store_in_memento())
o.set("Barbara Krupa druga albo i czwarta")
ct.add_memento(o.store_in_memento())
o.restore_from_memento(ct.get_memento(0))
