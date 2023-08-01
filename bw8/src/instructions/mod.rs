pub trait Instruction {
    fn encode_microcode(&self) -> [ControlWord; 8];
}

pub struct NoOperation;
impl Instruction for NoOperation {}

pub struct ExtendOpcode;
impl Instruction for ExtendOpcode {}

pub struct Halt;
impl Instruction for Halt {}

pub struct ClearCarry;
impl Instruction for ClearCarry {}

pub struct SetCarry;
impl Instruction for SetCarry {}

pub struct DisableInterrupts;
impl Instruction for DisableInterrupts {}

pub struct EnableInterrupts;
impl Instruction for EnableInterrupts {}

pub struct EnableBankRegister;
impl Instruction for EnableBankRegister {}

pub struct DisableBankRegister;
impl Instruction for DisableBankRegister {}

pub struct MoveRegister;
impl Instruction for MoveRegister {}

impl MoveRegister {
    pub const fn new() -> Self {
        MoveRegister {}
    }
}
