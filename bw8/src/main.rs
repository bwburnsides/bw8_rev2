#![allow(dead_code)]
#![allow(unused_variables)]

mod control;
mod instructions;

use control::*;
use instructions::*;

const NORMAL_OPCODES: [&dyn Instruction; 20] = [
    &MoveRegister::new(RegisterLoad::A, LeftSelect::B),
    &MoveRegister::new(RegisterLoad::A, LeftSelect::C),
    &MoveRegister::new(RegisterLoad::A, LeftSelect::D),
    &MoveRegister::new(RegisterLoad::B, LeftSelect::A),
    &MoveRegister::new(RegisterLoad::B, LeftSelect::C),
    &MoveRegister::new(RegisterLoad::B, LeftSelect::D),
    &MoveRegister::new(RegisterLoad::C, LeftSelect::A),
    &MoveRegister::new(RegisterLoad::C, LeftSelect::B),
    &MoveRegister::new(RegisterLoad::C, LeftSelect::D),
    &MoveRegister::new(RegisterLoad::D, LeftSelect::A),
    &MoveRegister::new(RegisterLoad::D, LeftSelect::B),
    &MoveRegister::new(RegisterLoad::D, LeftSelect::C),
    &LoadRegisterImmediate::new(RegisterLoad::A),
    &LoadRegisterImmediate::new(RegisterLoad::B),
    &LoadRegisterImmediate::new(RegisterLoad::C),
    &LoadRegisterImmediate::new(RegisterLoad::D),
    &InputFromPort::new(RegisterLoad::A),
    &InputFromPort::new(RegisterLoad::B),
    &InputFromPort::new(RegisterLoad::C),
    &InputFromPort::new(RegisterLoad::D),
];

const EXTENDED_OPCODES: [&dyn Instruction; 2] = [
    &MoveRegister::new(RegisterLoad::Bank, LeftSelect::A),
    &MoveRegister::new(RegisterLoad::A, LeftSelect::Bank),
];

fn decode_state(state_address: u16) -> &'static dyn Instruction {
    let opcode = (state_address & 0b1111_1111) as u8;
    let is_extended = ((state_address >> 8) & 0b1) == 1;

    if is_extended {
        EXTENDED_OPCODES[opcode as usize]
    } else {
        NORMAL_OPCODES[opcode as usize]
    }
}

fn main() {
    // 1. Produce primary microprogram
    // 2. Produce interrupt microprograms
    // 3. Produce ALU Decoder
    // 4. Produce Jump Decoder
    // 5. Produce Logic Unit (Should be removed)

    // let microprogram: [u64; 512 * 8];

    // for state_address in 0..(2_u16).pow(9) {
    //     let instruction = decode_state(state_address);
    //     let microcode = instruction.encode_microcode();

    //     // Add microcode to microprogram
    // }

    // Write microprogram to control ROM
    println!("Hello, world!");
}
