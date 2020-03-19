from src import utils
import time
import glob
import os
from ruamel.yaml import YAML


class Telegram:
    name = 'Telegram'

    def open(self):
        return utils.terminal_command('open', '-a', self.name)


class Firefox:
    name = 'Firefox'

    def open(self, url):
        return utils.terminal_command('open', url, '-a', self.name)


class Safari(Firefox):
    name = 'Safari'


class VSCode:

    name = 'Visual Studio Code'

    def __init__(self, wildcard=None):
        self.code = self.load(wildcard)
        self.position = 0
        time.sleep(1)

    def open(self, filename=None):
        cmd = ['open', '-a', self.name]
        if filename:
            utils.terminal_command('touch', filename)
            cmd.append(filename)
        return utils.terminal_command(*cmd)

    def write(self, length):
        spent = 0
        for c in self.code[self.position:self.position + length]:
            spent += utils.press_key(c)
        self.position += length
        return round(spent)

    @staticmethod
    def load(wildcard):
        result = ''
        if wildcard:
            for f in glob.glob(wildcard, recursive=True):
                path = os.path.join(os.path.realpath(f))
                if os.path.exists(path):
                    with open(path) as fp:
                        result += ''.join([l for l in fp.readlines()]) + '\n\n\n'
        return result


class Skype:

    name = 'Skype'

    def open(self):
        return utils.terminal_command('open', '-a', self.name)


class Faker:

    config_file = 'config.yaml'

    def __init__(self, terminal):
        yaml = YAML(typ='safe')
        self.config = yaml.load(open(os.path.abspath(self.config_file)))
        self.terminal = terminal

    def rotation(self):
        pass
