class Author:
    def __init__(self, id=None, name=""):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"<Author id={self.id}, name={self.name}>"
