def test_home(app):
    app.get_html('/', status=200)
    app.get_html('/languages/Omagua', status=200)


def test_cognateset(app):
    app.get_html('/cognatesets/13949', status=200)


def test_sentences_with_non_numeric_ids(app):
    # Tupinamba sentence IDs include non-numeric ones like "Tupinamba-4f111131".
    app.get_html('/sentences?language=Tupinamba', status=200)
