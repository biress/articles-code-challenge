def test_article_initialization():
    from lib.models.article import Article
    article = Article(title="Test Title", author_id=1, magazine_id=2)
    assert article.title == "Test Title"
