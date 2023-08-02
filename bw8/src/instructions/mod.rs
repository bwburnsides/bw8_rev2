use crate::control::*;

static FETCH: MicroOperation = MicroOperation::new(
    false,
    AluFunction::NoOperation,
    AddressType::Memory,
    PointerSelect::ProgramCounter,
    PointerLoad::ProgramCounter,
    RegisterLoad::Instruction,
    LeftSelect::Zero,
    RightSelect::Temporary,
    RegisterWriteBackMode::MemoryData,
    PointerLoadMode::NoLoad,
    PointerWriteBackMode::AguMode,
    OffsetMode::One,
    JumpCondition::Never,
);

fn base_microcode() -> [MicroOperation; 8] {
    let mut microcode: [MicroOperation; 8] = [MicroOperation::default(); 8];
    microcode[0] = FETCH;
    microcode
}

pub trait Instruction {
    fn encode_operations(&self) -> [MicroOperation; 8];
}

pub struct NoOperation;

impl NoOperation {
    pub const fn new() -> Self {
        NoOperation {}
    }
}

impl Instruction for NoOperation {
    fn encode_operations(&self) -> [MicroOperation; 8] {
        let mut microcode = base_microcode();

        microcode[1] = MicroOperation::builder()
            .pointer_select(PointerSelect::ProgramCounter)
            .offset_mode(OffsetMode::One)
            .pointer_load(PointerLoad::ProgramCounter)
            .pointer_load_mode(PointerLoadMode::FullWord)
            .reset_sequencer(true)
            .build();

        microcode
    }
}

pub struct MoveRegister {
    destination_register: RegisterLoad,
    source_register: LeftSelect,
}

impl MoveRegister {
    pub const fn new(destination_register: RegisterLoad, source_register: LeftSelect) -> Self {
        Self {
            source_register,
            destination_register,
        }
    }
}

impl Instruction for MoveRegister {
    fn encode_operations(&self) -> [MicroOperation; 8] {
        let mut microcode = base_microcode();

        microcode[1] = MicroOperation::builder()
            .pointer_select(PointerSelect::ProgramCounter)
            .offset_mode(OffsetMode::One)
            .pointer_load(PointerLoad::ProgramCounter)
            .left_select(self.source_register)
            .alu_function(AluFunction::LeftPassThrough)
            .register_load(self.destination_register)
            .reset_sequencer(true)
            .build();

        microcode
    }
}

pub struct LoadRegisterImmediate {
    destination_register: RegisterLoad,
}

impl LoadRegisterImmediate {
    pub const fn new(destination_register: RegisterLoad) -> Self {
        Self {
            destination_register,
        }
    }
}

impl Instruction for LoadRegisterImmediate {
    fn encode_operations(&self) -> [MicroOperation; 8] {
        let mut microcode = base_microcode();

        microcode[1] = MicroOperation::builder()
            .register_writeback_mode(RegisterWriteBackMode::MemoryData)
            .register_load(self.destination_register)
            .pointer_select(PointerSelect::ProgramCounter)
            .offset_mode(OffsetMode::One)
            .pointer_load(PointerLoad::ProgramCounter)
            .pointer_load_mode(PointerLoadMode::FullWord)
            .reset_sequencer(true)
            .build();

        microcode
    }
}

pub struct InputFromPort {
    destination_register: RegisterLoad,
}

impl InputFromPort {
    pub const fn new(destination_register: RegisterLoad) -> Self {
        Self {
            destination_register,
        }
    }
}

impl Instruction for InputFromPort {
    fn encode_operations(&self) -> [MicroOperation; 8] {
        let mut microcode = base_microcode();

        microcode[1] = MicroOperation::builder()
            .register_writeback_mode(RegisterWriteBackMode::MemoryData)
            .pointer_writeback_mode(PointerWriteBackMode::AluResult)
            .pointer_load(PointerLoad::Temporary)
            .pointer_load_mode(PointerLoadMode::LowByte)
            .build();

        microcode[2] = MicroOperation::builder()
            .left_select(LeftSelect::Zero)
            .alu_function(AluFunction::LeftPassThrough)
            .register_writeback_mode(RegisterWriteBackMode::AluResult)
            .pointer_writeback_mode(PointerWriteBackMode::AluResult)
            .pointer_select(PointerSelect::Temporary)
            .pointer_load_mode(PointerLoadMode::HighByte)
            .build();

        microcode[3] = MicroOperation::builder()
            .pointer_select(PointerSelect::Temporary)
            .offset_mode(OffsetMode::Disable)
            .build();

        microcode[4] = MicroOperation::builder()
            .register_writeback_mode(RegisterWriteBackMode::MemoryData)
            .register_load(self.destination_register)
            .pointer_select(PointerSelect::ProgramCounter)
            .pointer_load(PointerLoad::ProgramCounter)
            .pointer_load_mode(PointerLoadMode::FullWord)
            .offset_mode(OffsetMode::One)
            .reset_sequencer(true)
            .build();

        microcode
    }
}
