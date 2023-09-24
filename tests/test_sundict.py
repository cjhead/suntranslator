from translator.translate import Translator


def test_create_sun_dict():
    translator = Translator()
    assert isinstance(translator.sun_symbols, dict)
