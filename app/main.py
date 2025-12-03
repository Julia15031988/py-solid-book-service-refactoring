import json
import xml.etree.ElementTree as etree

class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    # --- Display methods ---
    def _display_console(self) -> None:
        print(self.content)

    def _display_reverse(self) -> None:
        print(self.content[::-1])

    DISPLAY_STRATEGIES = {
        "console": _display_console,
        "reverse": _display_reverse,
    }

    def display(self, display_type: str) -> None:
        strategy = self.DISPLAY_STRATEGIES.get(display_type)
        if not strategy:
            raise ValueError(f"Unknown display type: {display_type}")
        strategy(self)

    # --- Print methods ---
    def _print_console(self) -> None:
        print(f"Printing the book: {self.title}...")
        print(self.content)

    def _print_reverse(self) -> None:
        print(f"Printing the book in reverse: {self.title}...")
        print(self.content[::-1])

    PRINT_STRATEGIES = {
        "console": _print_console,
        "reverse": _print_reverse,
    }

    def print_book(self, print_type: str) -> None:
        strategy = self.PRINT_STRATEGIES.get(print_type)
        if not strategy:
            raise ValueError(f"Unknown print type: {print_type}")
        strategy(self)

    # --- Serialization ---
    def _serialize_json(self) -> str:
        return json.dumps({"title": self.title, "content": self.content})

    def _serialize_xml(self) -> str:
        root = etree.Element("book")
        etree.SubElement(root, "title").text = self.title
        etree.SubElement(root, "content").text = self.content
        return etree.tostring(root, encoding="unicode")

    SERIALIZE_STRATEGIES = {
        "json": _serialize_json,
        "xml": _serialize_xml,
    }

    def serialize(self, serialize_type: str) -> str:
        strategy = self.SERIALIZE_STRATEGIES.get(serialize_type)
        if not strategy:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
        return strategy(self)


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    actions = {
        "display": book.display,
        "print": book.print_book,
        "serialize": book.serialize,
    }

    for cmd, method_type in commands:
        action = actions.get(cmd)
        if not action:
            raise ValueError(f"Unknown command: {cmd}")

        result = action(method_type)
        if cmd == "serialize":
            return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
