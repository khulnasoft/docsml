import hashlib

from docsml import MarkdownGenerator


def test_import2md() -> None:
    generator = MarkdownGenerator()
    markdown = generator.import2md(MarkdownGenerator.import2md)
    # Remove whitespaces: fix changes between py version 3.6 3.7 in signature method
    md_hash = hashlib.md5(markdown.replace(" ", "").encode("utf-8")).hexdigest()
    assert md_hash == "aa6ccef8205fa54d0782edc54cab5ee7"


def test_class2md() -> None:
    generator = MarkdownGenerator()
    markdown = generator.class2md(MarkdownGenerator)
    # Remove whitespaces: fix changes between py version 3.6 3.7 in signature method
    md_hash = hashlib.md5(markdown.replace(" ", "").encode("utf-8")).hexdigest()
    assert md_hash == "2fa86b7a83fb9e7a469d73452c9cb735"


def test_module2md() -> None:
    generator = MarkdownGenerator()
    from docsml import generation

    markdown = generator.module2md(generation)
    # Remove whitespaces: fix changes between py version 3.6 3.7 in signature method
    md_hash = hashlib.md5(markdown.replace(" ", "").encode("utf-8")).hexdigest()
    assert md_hash == "075a4793b133047ce8777e4a101a48ff"


def test_func2md() -> None:
    generator = MarkdownGenerator()
    markdown = generator.func2md(MarkdownGenerator.func2md)
    # Remove whitespaces: fix changes between py version 3.6 3.7 in signature method
    md_hash = hashlib.md5(markdown.replace(" ", "").encode("utf-8")).hexdigest()
    assert md_hash == "8df53af1f20a497e9e6951004e1ee25a"
