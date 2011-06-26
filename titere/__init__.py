from ConfigParser import SafeConfigParser
from components import UserComponent, FileComponent


class TitereConfigParser(SafeConfigParser):
    " Configuration parser."

    def readfp(self, fp):
        " Redefine read."
        SafeConfigParser.readfp(self, fp)

        self.comps = []

        components = [UserComponent, FileComponent]

        # Search for titere structure.
        for section in self.sections():

            # Get type and name of this section.
            type_, name = section.split(':')

            for comp  in components:
                if type_ == comp.Meta.type:
                    self.comps.append(
                        (type_, name, comp(**dict(self.items(section)))))


class Titere(object):
    "Base class that reads a file and apply the config."

    def __init__(self, fp):
        " Reads a file for configuration."

        # Read configuration
        self.config = TitereConfigParser()
        self.config.readfp(fp)

    def apply(self):
        " Apply all the configuration."

        # Create users.
        for type, name, comp in self.config.comps:
            import fabric.operations
            fabric.operations.run = fabric.operations.local
            comp.apply()
