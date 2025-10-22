class TextPrinter:
    def __init__(self, text):
        self._text = text

    def print_text(self):
        return self._text


class TextDecorator(TextPrinter):
    def __init__(self, printer):
        self._printer = printer


class UpperCaseDecorator(TextDecorator):
    def print_text(self):
        return self._printer.print_text().upper()


class BorderDecorator(TextDecorator):
    def print_text(self):
        text = self._printer.print_text()
        return text


class ExclamationDecorator(TextDecorator):
    def print_text(self):
        return self._printer.print_text() + "!!!"
