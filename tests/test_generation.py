import hashlib

from docsml import MarkdownGenerator


def test_import2md() -> None:
    generator = MarkdownGenerator()
    markdown = generator.import2md(MarkdownGenerator.import2md)
    # Remove whitespaces: fix changes between py version 3.6 3.7 in signature method
    md_hash = hashlib.md5(markdown.replace(" ", "").encode("utf-8")).hexdigest()
    assert md_hash == "0c975ff6219a5eb16d7ca6bb66fdefdb"


def test_class2md() -> None:
    generator = MarkdownGenerator()
    markdown = generator.class2md(MarkdownGenerator)
    # Remove whitespaces: fix changes between py version 3.6 3.7 in signature method
    md_hash = hashlib.md5(markdown.replace(" ", "").encode("utf-8")).hexdigest()
    assert md_hash == "08417dac9c303454037e324a33855c75"


def test_module2md() -> None:
    generator = MarkdownGenerator()
    from docsml import generation

    markdown = generator.module2md(generation)
    # Remove whitespaces: fix changes between py version 3.6 3.7 in signature method
    md_hash = hashlib.md5(markdown.replace(" ", "").encode("utf-8")).hexdigest()
    assert md_hash == "463ef2aa337dbb85e9e978dc131b1721"


def test_func2md() -> None:
    generator = MarkdownGenerator()
    markdown = generator.func2md(MarkdownGenerator.func2md)
    # Remove whitespaces: fix changes between py version 3.6 3.7 in signature method
    md_hash = hashlib.md5(markdown.replace(" ", "").encode("utf-8")).hexdigest()
    assert md_hash == "5d75b095249eb96d9707c756a61ea7e0"
