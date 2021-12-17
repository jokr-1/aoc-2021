
import math
hexdecoder = {"0": "0000", "1": "0001", "2": "0010", "3": "0011", "4": "0100", "5": "0101", "6": "0110", "7": "0111", "8": "1000", "9": "1001", "A": "1010", "B": "1011", "C": "1100", "D": "1101", "E": "1110", "F": "1111" }

class Parser:

    def __init__(self, data) -> None:
        self.data = data

    def consume(self, n: int):
        out, self.data = self.data[:n], self.data[n:]
        return out

    def consume_int(self, n):
        return int(self.consume(n),2)

    def parse_header(self):
        version = self.consume_int(3)
        packet_id = self.consume_int(3)
        return version, packet_id

    def parse_literal(self):
        literal = ""
        while self.data:
            group = self.consume_int(1)
            literal += self.consume(4)
            if group == 0:
                return int(literal,2)

    def parse_operator(self):
        subpackets = []
        length_type_id = self.consume_int(1)
        n_bits = 11 if length_type_id else 15
        length = self.consume_int(n_bits)
        if n_bits == 11:
            for _ in range(length):
                subpackets.append(self.parse())
        else:
            stop = len(self.data) - length
            while len(self.data) > stop:
                subpackets.append(self.parse())
        return subpackets

    def parse(self):
        version, packet_id = self.parse_header()
        if packet_id == 4:
            value = self.parse_literal()        
        else:
            value = self.parse_operator()
        return (version, packet_id, value) 

def calc_version(packet):
    version, _, value = packet
    if isinstance(value, list):
        return version + sum(calc_version(p) for p in value) 
    return version

def calc_packet(packet):
    _, t, value = packet
    if t == 0:
        return sum(calc_packet(p) for p in value)
    elif t==1:
        return math.prod(calc_packet(p) for p in value)
    elif t==2:
        return min(calc_packet(p) for p in value)
    elif t==3:
        return max(calc_packet(p) for p in value)
    elif t == 4:
        return value
    elif t == 5:
        return int(calc_packet(value[0]) > calc_packet(value[1]))
    elif t == 6:
        return int(calc_packet(value[0]) < calc_packet(value[1]))
    elif t == 7:
        return int(calc_packet(value[0]) == calc_packet(value[1]))

with open("input") as f:
    input = f.read().rstrip()
    input_binary = "".join(hexdecoder[c] for c in input)
    packets = Parser(data=input_binary).parse()
    print('Part 1:', calc_version(packets))
    print('Part 2:', calc_packet(packets))