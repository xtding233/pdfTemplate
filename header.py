from strenum import StrEnum
class Header(StrEnum):
    name = 'name'
    type = 'type'
    x1 = 'x1'
    y1 = 'y1'
    x2 = 'x2'
    y2 = 'y2'
    font = 'font'
    size = 'size'
    bold = 'bold'
    italic = 'italic'
    underline = 'underline'
    foreground = 'foreground'
    background = 'background'
    align = 'align'
    text = 'text'
    priority = 'priority'
    multiline = 'multiline'
    rotation = 'rotation'


TEMPLATE_HEADER = [Header.name, Header.type, Header.x1, Header.y1, Header.x2, Header.y2,
                   Header.font, Header.size, Header.bold, Header.italic, Header.underline,
                   Header.foreground, Header.background,
                   Header.align, Header.text, Header.priority, Header.multiline, Header.rotation]

