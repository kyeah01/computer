class Parser:
    def __init__(self, filePath) -> None:
        f = open(filePath, 'r')
        self.datas = f.readlines()
    
    def hasMoreCommands(self) -> bool:
        return len(self.datas) > 0
    
    def advance(self) -> None:
        self.command = self.datas.pop(0)

    def commandType(self) -> str:
        if '@' in self.command:
            return 'A_COMMAND'
        return 'C_COMMAND'

    def symbol(self) -> str:
        if self.commandType() == 'A_COMMAND':
            # return "{0:16b}".format(int(self.command[1:]))
            return int(self.command[1:])
        return self.command
    
    def dest(self) -> str:
        if "=" in self.command:
            return self.command.split('=')[0]
        return 'None'
    
    def comp(self) -> str:
        return self.command.split('=')[1].split(';')[0]
    
    def jump(self) -> str:
        if ';' in self.command:
            return self.command.split(';')[1]
        return 'None'
