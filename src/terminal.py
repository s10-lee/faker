import sys


class BaseTerminal:

    # Debug mode
    DEBUG = True

    # <CR><LF> - carriage return & line feed (newline)
    CRLF = '\r\n'

    # Color first digit
    #   1 - apply style, remove color
    #   2 - no styles
    #   3 - apply color
    #   4 - apply color to background, color white
    #   5, 6, 7... same as 1

    DEFAULT_PREFIX = 'normal'
    COLOR_PREFIX = {
        'normal': 3,
        'invert': 4
    }

    DEFAULT_COLOR = 'gray'

    COLORS = {
        'none':     0,
        'red':      1,
        'green':    2,
        'yellow':   3,
        'blue':     4,
        'purple':   5,
        'cyan':     6,
        'gray':     7,
        'white':    8,
    }

    DEFAULT_STYLE = 'none'

    STYLE = {
        'bold':         1,
        'muted':        2,
        'italic':       3,
        'underline':    4,
        'blink':        5,
        'none':         6,
        'background':   7,
        'transparent':  8
    }

    STYLE_TAGS = {
        '<b>':      '1',
        '<i>':      '3',
        '<u>':      '4',
        '<blink>':  '5',
        '<bg>':     '7',
    }

    LEFT_PADDING = ' ' * 3

    # Prompt
    PROMPT = LEFT_PADDING + '> '

    #########################################
    #                                       #
    #               Private                 #
    #                                       #
    #########################################
    @classmethod
    def _color(cls, name: str):
        if name not in cls.COLORS:
            name = cls.DEFAULT_COLOR
        return cls.COLORS.get(name)

    @classmethod
    def _style(cls, name: str):
        if name not in cls.STYLE:
            name = cls.DEFAULT_STYLE
        return cls.STYLE.get(name)

    @classmethod
    def _prefix(cls, name: str):
        if name not in cls.COLOR_PREFIX:
            name = cls.DEFAULT_PREFIX
        return cls.COLOR_PREFIX.get(name)

    @staticmethod
    def _wrap(text, style: int = 1, prefix: int = 3, color: int = 1):
        # print(f'{style};{prefix}{color}')
        return f'\033[{style};{prefix}{color}m{text}\033[0m'

    @classmethod
    def _parse(cls, text: str):
        for color, code in cls.COLORS:
            text = text.replace(f'<{color}>', f"\033[6;3{code}m").replace(f'</{color}>', '\033[0m')
        text = text.replace('<nl>', cls.CRLF)
        return text

    @classmethod
    def _add_default(cls, value):
        result = None

        if isinstance(value, bool):
            result = 'no'
            if value:
                result = 'yes'

        elif isinstance(value, int) or isinstance(value, float) or isinstance(value, str):
            result = value

        if result is not None:
            return cls.bold('[') + cls.yellow(result, bold=True) + cls.bold(']')

        return ''

    #########################################
    #                                       #
    #               Public                  #
    #                                       #
    #########################################
    @classmethod
    def debug(cls, text, style=1, prefix=3, color=1):
        return cls._wrap(text, style=style, prefix=prefix, color=color)

    @classmethod
    def wrap_text(cls, text, style=None, prefix=None, color=None):
        return cls._wrap(text, prefix=cls._prefix(prefix), color=cls._color(color), style=cls._style(style))

    @classmethod
    def bold(cls, text, color=None, prefix=None):
        return cls.wrap_text(text, prefix=prefix, color=color, style='bold')

    @classmethod
    def underline(cls, text, color=None, prefix=None):
        return cls.wrap_text(text, prefix=prefix, color=color, style='underline')

    @classmethod
    def italic(cls, text, color=None):
        return cls.wrap_text(text, color=color, style='italic')

    @classmethod
    def background(cls, text, color=None):
        return cls.wrap_text(text, color=color, style='background')

    @classmethod
    def yellow(cls, text, bold=None):
        return cls.wrap_text(text, color='yellow', style='bold' if bold else None)

    @classmethod
    def white(cls, text):
        return cls.wrap_text(text, color='white')

    @classmethod
    def write(cls, *args, sep=' ', end=None, color=None, bold=False, underline=False, italic=False, blink=False, bg=None):

        # Fix to merge styles
        # Problem with color in applied styles
        #
        # TODO: Refactor this, it`s awful !

        kw = {'bold': bold, 'underline': underline, 'italic': italic, 'blink': blink}

        first_style = None
        styles = {k: v for k, v in kw.items() if v}

        if styles:
            first_style = styles.popitem()[0]

        prefix = 'normal'
        if bg:
            prefix = 'invert'

        for a in args:

            # Apply first style
            result = cls.wrap_text(a, prefix=prefix, color=color, style=first_style)

            # And all the others
            for s, apply in styles.items():
                result = cls.wrap_text(result, style=s)

            # BG Color
            if bg:
                result = cls.background(result, color=bg)

            sys.stdout.write(cls.LEFT_PADDING + result + sep)

        if end is None:
            end = cls.CRLF
        sys.stdout.write(end)

    @classmethod
    def error(cls, text):
        cls.write(text, bold=True, color='red')

    @classmethod
    def input(cls, prompt=None):
        if not prompt:
            prompt = cls.PROMPT
        return input(prompt).strip()

    @classmethod
    def read(cls, text, var_type=str, required=False, default=None, greater=None, prompt=None, **kwargs):

        # TODO: Move to another method
        # temporary fix for color
        kwargs['color'] = kwargs.get('color', 'green')

        if text:
            cls.write(text + ' ' + cls._add_default(default), **kwargs)

        while True:
            line = cls.input(prompt)

            # Required
            if required and not line:
                cls.error('Cannot be blank !')
                continue

            # Integer
            if var_type is int:

                if line:

                    if not line.isnumeric():
                        cls.error('Not integer !')
                        continue

                    if greater and int(line) < int(greater):
                        cls.error(f'Must be greater than {greater} !')
                        continue

                    line = int(line)

                else:
                    line = 0
                    if default:
                        line = default

            # Boolean
            if var_type is bool:
                if not len(line):
                    line = bool(default)
                elif line.lower().startswith('y'):
                    line = True
                else:
                    line = False

            # Loop end
            break

        return line


class Terminal(BaseTerminal):

    def __init__(self, **kwargs):

        self.arguments = {}
        self.names = kwargs

        next_key = None
        next_val = 0

        for a in tuple(sys.argv)[1:]:

            if a.startswith('-'):
                alias = a.strip('-')
                next_key = self.get_name(alias)
                next_val = 0
                self.arguments[next_key] = True

            elif next_key:
                if next_val > 0:
                    self.arguments[next_key] = [self.arguments[next_key]] + [a]
                else:
                    self.arguments[next_key] = a
                    next_val += 1

    def get_arg(self, name, default=None):
        return self.arguments.get(name, default)

    def get_name(self, key):
        for k, v in self.names.items():
            if key in v:
                return k
        return key
