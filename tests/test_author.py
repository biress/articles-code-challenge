def test_author_initialization():
    from lib.models.author import Author
    author = Author(name="John Doe")
    assert author.name == "John Doe"
