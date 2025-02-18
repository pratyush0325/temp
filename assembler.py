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


        