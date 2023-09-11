from src.ports.pair_finder import PairFinder


class Cli:
    
    def __init__(self):
        self.pair_finder = PairFinder()
    
    def start(self):
        input_data = input()
        inputs = input_data.split()
        operation_result = int(inputs.pop())
        values = [int(valor) for valor in inputs[0].split(',')]
        print(self.pair_finder.execute(values, operation_result))
        
        
    