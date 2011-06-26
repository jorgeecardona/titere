from fabric.operations import run


class Component(object):
    class Meta(object):
        pass

    def __init__(self, **kwargs):
        pass


class FileComponent(Component):

    class Meta(object):
        type = 'file'
        types = 'files'

    def __init__(self, path, content=None):
        super(FileComponent, self).__init__(path=path, content=content)

        self.path = path
        self.content = content

    def apply(self):
        " Apply configuration."
        if self.content is not None:
            fd = open(self.path, 'w')
            fd.write(self.content)
            fd.close()


class UserComponent(Component):

    class Meta(object):
        type = 'user'
        types = 'users'

    def __init__(self, username, system=False, home=None, no_home=False,
                 shell=None, _depends=[]):
        self.username = username
        self.system = True
        self.home = home
        self.no_home = no_home
        self.shell = shell

    def apply(self):

        args = ['adduser']

        if self.system:
            args.append('--system')

        if self.home is not None:
            args.extend(['--home', str(self.home)])

        if self.no_home:
            args.append('--no-create-home')

        if self.shell is not None:
            args.extend(['--shell', str(self.shell)])

        # Run command
        run(' '.join(args))
