class Article:
    def __init__(self, id=None, title="", author_id=None, magazine_id=None):
        self.id = id
        self.title = title
        self.author_id = author_id
        self.magazine_id = magazine_id

    def __repr__(self):
        return f"<Article id={self.id}, title={self.title}>"
