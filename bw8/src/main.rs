#![allow(dead_code)]
#![allow(unused_variables)]

mod instructions;
use instructions::*;

const NORMAL_OPCODES: [&dyn Instruction; 2] = [&NoOperation {}, NoOperation {}];
const EXTENDED_OPCODES: [&dyn Instruction; 2] = [&MoveRegister {}, &MoveRegister {}];

fn decode_state(state_address: u32) -> &'static dyn Instruction {
    let opcode = ((state_address >> 3) & 0b1111_1111) as u8;
    let is_extended = ((state_address >> 11) & 0b1) == 1;

    if is_extended {
        EXTENDED_OPCODES[opcode as usize]
    } else {
        NORMAL_OPCODES[opcode as usize]
    }
}

fn main() {
    for state_address in 0..(2_u32).pow(12) {
        let instruction = decode_state(state_address);
        let microcode = instruction.encode_microcode();
    }

    println!("Hello, world!");
}
