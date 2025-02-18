def R_type_inst(rs1,rs2,rd):
    funct_7 = {"add": "0000000","sub" :"0100000","slt": "0000000","srl": "0000000","or": "0000000","and": "0000000"}
    funct_3 = {"add": "000","sub" :"000","slt": "010","srl": "101","or": "110","and": "111"}
    opcode = "0110011"


def I_type_inst(imm,rs1,rd):
    funct3 = {"lw": "010","addi": "000","jalr" :"000"}
    opcode = {"lw": "0000011","addi": "0010011","jalr" :"1100111"}

def S_type_inst(rs1,rs2,imm4,imm5):
    opcode = "0100011"
    funct3  = "010"

def B_type_inst(rs1,rs2,imm4,imm10):
    funct3 = {"beq": "000","bne": "001", "blt": "100"}
    opcode = "1100011"

def J_type_inst(rd,imm):
    opcode = "1101111"
def register2binary(reg_name):
    registerer_map = {
        "x0": "00000", "zero": "00000","x1": "00001", "ra": "00001","x2": "00010", "sp": "00010","x3": "00011", "gp": "00011","x4": "00100", "tp": "00100","x5": "00101", "t0": "00101","x6": "00110", "t1": "00110","x7": "00111", "t2": "00111",
        "x8": "01000", "s0": "01000", "fp": "01000","x9": "01001", "s1": "01001","x10": "01010", "a0": "01010","x11": "01011", "a1": "01011","x12": "01100", "a2": "01100","x13": "01101", "a3": "01101","x14": "01110", "a4": "01110",
        "x15": "01111", "a5": "01111","x16": "10000", "a6": "10000","x17": "10001", "a7": "10001","x18": "10010", "s2": "10010","x19": "10011", "s3": "10011","x20": "10100", "s4": "10100","x21": "10101", "s5": "10101",
        "x22": "10110", "s6": "10110","x23": "10111", "s7": "10111","x24": "11000", "s8": "11000","x25": "11001", "s9": "11001","x26": "11010", "s10": "11010","x27": "11011", "s11": "11011","x28": "11100", "t3": "11100",
        "x29": "11101", "t4": "11101","x30": "11110", "t5": "11110","x31": "11111", "t6": "11111"
    }
    return registerer_map.get(reg_name, "Invalid register")


def read_and_tokenize(file_path):

    inst_list = []  # Stores tokenized lines


    with open(file_path, "r") as file:
        lines = file.readlines()
        label_list = {}
        pc = 0
        for line in lines:

            line = line.strip()  
            if(line == ""):
                pass
            words = line.split()
            n = len(words[0])
            if(((words[0])[n-1]) == ":"):
                label_list[words] = pc
                words.pop(0)
            pc +=4
    R_type = ["add", "sub", "slt", "srl", "or", "and"]
    I_type = ["lw", "addi", "jalr"]
    S_type = ["sw"]
    B_type = ["beq", "bne", "blt"]
    J_type = ["jal"]

    inst = words[0]
    if inst in R_type:
        R_type_inst()
    elif inst in I_type:
        pass
    elif inst in S_type:
        pass
    elif inst in B_type:
        pass
    elif inst in J_type:
        pass


        
