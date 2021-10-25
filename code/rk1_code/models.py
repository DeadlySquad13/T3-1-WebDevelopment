class ProgrammingLanguage:
    """Язык программирования. """
    def __init__(self, id: int, title: str):
        self.id = id
        self.title = title

 
class Ide:
    """Средство разработки. """
    def __init__(self, id: int, title: str, price: int, programming_language_id: int):
        self.id = id
        self.title = title
        self.price = price
        self.programming_language_id = programming_language_id

    def to_string_formatted(self) -> str:
        return f'Title: {self.title}, price: {self.price if self.price != 0 else f"{self.price} (free)"}'
 

class ProgrammingLanguageIde:
    """ Средства разработки для языка. """
    def __init__(self, programming_language_id: int, ide_id: int):
        self.programming_language_id = programming_language_id
        self.ide_id = ide_id
