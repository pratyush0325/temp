def register2binary(reg_name):
    registerer_map = {
        "x0": "00000", "zero": "00000","x1": "00001", "ra": "00001","x2": "00010", "sp": "00010","x3": "00011", "gp": "00011","x4": "00100", "tp": "00100","x5": "00101", "t0": "00101","x6": "00110", "t1": "00110","x7": "00111", "t2": "00111",
        "x8": "01000", "s0": "01000", "fp": "01000","x9": "01001", "s1": "01001","x10": "01010", "a0": "01010","x11": "01011", "a1": "01011","x12": "01100", "a2": "01100","x13": "01101", "a3": "01101","x14": "01110", "a4": "01110",
        "x15": "01111", "a5": "01111","x16": "10000", "a6": "10000","x17": "10001", "a7": "10001","x18": "10010", "s2": "10010","x19": "10011", "s3": "10011","x20": "10100", "s4": "10100","x21": "10101", "s5": "10101",
        "x22": "10110", "s6": "10110","x23": "10111", "s7": "10111","x24": "11000", "s8": "11000","x25": "11001", "s9": "11001","x26": "11010", "s10": "11010","x27": "11011", "s11": "11011","x28": "11100", "t3": "11100",
        "x29": "11101", "t4": "11101","x30": "11110", "t5": "11110","x31": "11111", "t6": "11111"
    }
    return registerer_map.get(reg_name, "Invalid register")

def R_type_inst(rs1,rs2,rd,inst):
    funct_7 = {"add": "0000000","sub" :"0100000","slt": "0000000","srl": "0000000","or": "0000000","and": "0000000"}
    funct_3 = {"add": "000","sub" :"000","slt": "010","srl": "101","or": "110","and": "111"}
    opcode = "0110011"
    f7 = funct_7["inst"]
    f3 = funct_3["inst"]
    target=f7+register2binary(rs2)+register2binary(rs1)+f3+register2binary(rd)+opcode
    with open("output_file", "a") as out_file: 
        out_file.write(target+"\n")


def I_type_inst(imm,rs1,rd):
    funct_3 = {"lw": "010","addi": "000","jalr" :"000"}
    opcode = {"lw": "0000011","addi": "0010011","jalr" :"1100111"}
    f3 = funct_3["inst"]
    target=imm_to_bin(imm,12)+rs1+f3+rd+opcode
    with open("output_file", "a") as out_file: 
        out_file.write(target+"\n")

def S_type_inst(rs1,rs2,imm):
    opcode = "0100011"
    funct_3 = "010"
    f3 = funct_3["inst"]
    imm=imm_to_bin(imm,12)
    imm5=imm[-12:-5]
    imm7=imm[-5:]
    target=imm5+rs2+rs1+f3+imm7+opcode
    with open("output_file", "a") as out_file: 
        out_file.write(target+"\n")

def B_type_inst(rs1,rs2,imm,label,pc,inst):
    funct3 = {"beq":"000", "bne":"001", "blt":"100", "bge":"101", "bltu":"110", "bgeu":"111"}
    opcode = "1100011"
    if(imm.isnumeric() or (imm[0]=="-" and imm[1:].isnumeric()) or imm is labels):
            if (imm.isnumeric() or (imm[0]=="-" and imm[1:].isnumeric())):
                offset=int(imm)*4
                imm_13bit = imm_to_bin(int(imm),13)
            else:
                offset = labels[imm] - pc
                imm_13bit=imm_to_bin(offset,13)

            final = imm_13bit[-13] + imm_13bit[-11] + imm_13bit[-10:-5] + rs2 + rs1+ funct3[inst] + imm_13bit[-5:-1] + imm_13bit[-12] + opcode
    else:
        if(imm not in labels):
            print("Error on line:",int(pc/4)+1,"->No such label")
            break
    
def J_type_inst(rd,imm):
    opcode = "1101111"
    
    imm=imm_to_bin(imm,20)
    target=imm[-20]+imm[-10:]+imm[-11]+imm[-19:-11]+rd+opcode
    with open("output_file", "a") as out_file: 
        out_file.write(target+"\n")

def read_and_tokenize(file_path):

    inst_list = []  # Stores tokenized lines


    with open(file_path, "r") as file:
        lines = file.readlines()
        label_list = {}
        pc = 0
        for line in lines:

            line = line.strip()  
            if(line == ""):
                continue
            temp = line.split(" ")
            
            words = temp[1].split(",")
            words.insert(0,temp[0])
          
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
    if len(words) ==3:
        if("(" in words[2]):
            temp = words[2].split("(")
            temp[1].replace(")","")
            words.pop()
            words[2] = temp[1]
            words[3] = temp[0]
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

def imm_to_bin(num,length):


    if(num>=0):   

        bin_str = bin(num)                                   
        bin_str = bin_str[2:]                             
        bin_str = '0'*(length-len(bin_str)) + bin_str  

    elif(num<0):                                               
        bin_str = bin((abs(num)^((2**length)-1)) + 1)        
        bin_str = bin_str[2:]                             
        bin_str = '1'*(length-len(bin_str)) + bin_str
 
    return bin_str
