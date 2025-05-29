def test_magazine_initialization():
    from lib.models.magazine import Magazine
    mag = Magazine(name="Nature", category="Science")
    assert mag.name == "Nature"
