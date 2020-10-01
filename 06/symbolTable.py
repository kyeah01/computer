class SymbolTable:
    def __init__(self):
        self.symbolTable = {}
    
    def addEntry(self, symbol, address) -> None:
        self.symbolTable[symbol] = address
    
    def contains(self, symbol) -> bool:
        return symbol in self.symbolTable.keys()

    def getAddress(self, symbol) -> int:
        return self.symbolTable.get(symbol)
