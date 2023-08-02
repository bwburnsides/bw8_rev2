#[derive(Clone, Copy)]
pub enum AddressType {
    Memory,
    Io,
}

#[derive(Clone, Copy)]
pub enum PrivilegeLevel {
    Kernel,
    User,
}

#[derive(Clone, Copy)]
pub enum InterruptMode {
    Normal,
    MaskableInterrupt,
    BusRequest,
    NonMaskableInterrupt,
}

#[derive(Clone, Copy)]
pub enum RegisterLoad {
    A,
    B,
    C,
    D,
    Offset,
    Bank,
    Temporary,
    Instruction,
}

#[derive(Clone, Copy)]
pub enum LeftSelect {
    A,
    B,
    C,
    D,
    Temporary,
    Bank,
    Zero,
}

#[derive(Clone, Copy)]
pub enum RightSelect {
    A,
    B,
    C,
    D,
    Temporary,
}

#[derive(Clone, Copy)]
pub enum RegisterWriteBackMode {
    MemoryData,
    AluResult,
}

#[derive(Clone, Copy)]
pub enum AluResultMode {
    Status,
    Calculated,
}

#[derive(Clone, Copy)]
pub enum AluFunction {
    NoOperation,
    LeftPassThrough,
}

#[derive(Clone, Copy)]
pub enum ShiftMode {
    PassThrough,
    LeftShift,
    LogicalLeftShift,
    ArithmeticRightShift,
}

#[derive(Clone, Copy)]
pub enum LogicMode {
    Clear,
    Set,
    Left,
    Right,
    NotLeft,
    NotRight,
    LeftOrRight,
    NotLeftOrRight,
    LeftOrNotRight,
    NotLeftOrNotRight,
    LeftAndRight,
    NotLeftAndRight,
    LeftAndNotRight,
    NotLeftAndNotRight,
    LeftXorRight,
    AllNotLeftXorRight,
}

#[derive(Clone, Copy)]
pub enum AdderMode {
    Zer0,
    One,
    CarryFlag,
}

#[derive(Clone, Copy)]
pub enum CarryFlagMode {
    Zero,
    AdderCarry,
    RightShiftCarry,
    LeftShiftCarry,
}

#[derive(Clone, Copy)]
pub enum PointerLoad {
    ProgramCounter,
    Stack,
    X,
    Y,
    Temporary,
}

#[derive(Clone, Copy)]
pub enum PointerSelect {
    ProgramCounter,
    Stack,
    X,
    Y,
    Temporary,
    Irq,
    Nmi,
    Swi,
}

#[derive(Clone, Copy)]
pub enum PointerLoadMode {
    NoLoad,
    LowByte,
    HighByte,
    FullWord,
}

#[derive(Clone, Copy)]
pub enum PointerWriteBackMode {
    AluResult,
    AguMode,
}

#[derive(Clone, Copy)]
pub enum OffsetMode {
    Disable,
    Enable,
    One,
    NegativeOne,
}

#[derive(Clone, Copy)]
pub enum JumpCondition {
    Never,
    Equal,
    NotEqual,
    LessThan,
    GreaterOrEqual,
    SignedLessThan,
    SignedGreaterOrEqual,
    Always,
}

#[derive(Clone, Copy)]
pub struct MicroOperation {
    reset_sequencer: bool,
    alu_function: AluFunction,
    address_type: AddressType,
    pointer_select: PointerSelect,
    pointer_load: PointerLoad,
    register_load: RegisterLoad,
    left_select: LeftSelect,
    right_select: RightSelect,
    register_writeback_mode: RegisterWriteBackMode,
    pointer_load_mode: PointerLoadMode,
    pointer_writeback_mode: PointerWriteBackMode,
    offset_mode: OffsetMode,
    jump_condition: JumpCondition,
}

impl MicroOperation {
    pub const fn new(
        reset_sequencer: bool,
        alu_function: AluFunction,
        address_type: AddressType,
        pointer_select: PointerSelect,
        pointer_load: PointerLoad,
        register_load: RegisterLoad,
        left_select: LeftSelect,
        right_select: RightSelect,
        register_writeback_mode: RegisterWriteBackMode,
        pointer_load_mode: PointerLoadMode,
        pointer_writeback_mode: PointerWriteBackMode,
        offset_mode: OffsetMode,
        jump_condition: JumpCondition,
    ) -> Self {
        Self {
            reset_sequencer,
            alu_function,
            address_type,
            pointer_select,
            pointer_load,
            register_load,
            left_select,
            right_select,
            register_writeback_mode,
            pointer_load_mode,
            pointer_writeback_mode,
            offset_mode,
            jump_condition,
        }
    }

    pub fn builder() -> MicroOperationBuilder {
        MicroOperationBuilder::default()
    }

    pub const fn default() -> Self {
        MicroOperation {
            reset_sequencer: false,
            alu_function: AluFunction::NoOperation,
            address_type: AddressType::Memory,
            pointer_select: PointerSelect::ProgramCounter,
            pointer_load: PointerLoad::Temporary,
            register_load: RegisterLoad::Temporary,
            left_select: LeftSelect::Temporary,
            right_select: RightSelect::Temporary,
            register_writeback_mode: RegisterWriteBackMode::AluResult,
            pointer_load_mode: PointerLoadMode::NoLoad,
            pointer_writeback_mode: PointerWriteBackMode::AguMode,
            offset_mode: OffsetMode::Disable,
            jump_condition: JumpCondition::Never,
        }
    }
}

#[derive(Default)]
pub struct MicroOperationBuilder {
    reset_sequencer: Option<bool>,
    alu_function: Option<AluFunction>,
    address_type: Option<AddressType>,
    pointer_select: Option<PointerSelect>,
    pointer_load: Option<PointerLoad>,
    register_load: Option<RegisterLoad>,
    left_select: Option<LeftSelect>,
    right_select: Option<RightSelect>,
    register_writeback_mode: Option<RegisterWriteBackMode>,
    pointer_load_mode: Option<PointerLoadMode>,
    pointer_writeback_mode: Option<PointerWriteBackMode>,
    offset_mode: Option<OffsetMode>,
    jump_condition: Option<JumpCondition>,
}

impl MicroOperationBuilder {
    pub const fn build(self) -> MicroOperation {
        MicroOperation::default()
    }

    pub const fn reset_sequencer(mut self, value: bool) -> Self {
        self.reset_sequencer = Some(value);
        self
    }

    pub const fn alu_function(mut self, value: AluFunction) -> Self {
        self.alu_function = Some(value);
        self
    }

    pub const fn address_type(mut self, value: AddressType) -> Self {
        self.address_type = Some(value);
        self
    }

    pub const fn pointer_select(mut self, value: PointerSelect) -> Self {
        self.pointer_select = Some(value);
        self
    }

    pub const fn pointer_load(mut self, value: PointerLoad) -> Self {
        self.pointer_load = Some(value);
        self
    }

    pub const fn register_load(mut self, value: RegisterLoad) -> Self {
        self.register_load = Some(value);
        self
    }

    pub const fn left_select(mut self, value: LeftSelect) -> Self {
        self.left_select = Some(value);
        self
    }

    pub const fn right_select(mut self, value: RightSelect) -> Self {
        self.right_select = Some(value);
        self
    }

    pub const fn register_writeback_mode(mut self, value: RegisterWriteBackMode) -> Self {
        self.register_writeback_mode = Some(value);
        self
    }

    pub const fn pointer_load_mode(mut self, value: PointerLoadMode) -> Self {
        self.pointer_load_mode = Some(value);
        self
    }

    pub const fn pointer_writeback_mode(mut self, value: PointerWriteBackMode) -> Self {
        self.pointer_writeback_mode = Some(value);
        self
    }

    pub const fn offset_mode(mut self, value: OffsetMode) -> Self {
        self.offset_mode = Some(value);
        self
    }

    pub const fn jump_condition(mut self, value: JumpCondition) -> Self {
        self.jump_condition = Some(value);
        self
    }
}
