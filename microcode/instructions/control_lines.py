import enum
from typing import NewType, Literal, Self, Generator, TypeGuard, reveal_type
from dataclasses import dataclass
from instructions.opcodes import OpcodeType, NormalOpcode, ExtendedOpcode

RegisterLoadEnable = NewType("RegisterLoadEnable", bool)
UseBankRegister = NewType("UseBankRegister", bool)
SaveFlags = NewType("SaveFlags", bool)
AssertSystemBus = NewType("AssertSystemBus", bool)
StateAddress = NewType("StateAddress", int)


def state_range() -> Generator[StateAddress, None, None]:
    for address in range(2**14):
        yield StateAddress(address)


InstructionStep = NewType(
    "InstructionStep",
    int,
)


@enum.unique
class AddressType(enum.IntEnum):
    Memory = 0b0
    Io = 0b1


@enum.unique
class MemoryAccessType(enum.IntEnum):
    Code = 0b0
    Data = 0b1


# Is this needed? Provided by internal flag.
# Will need a control line to manage that flag.
@enum.unique
class PrivilegeLevel(enum.IntEnum):
    Kernel = 0b0
    User = 0b1


@enum.unique
class InterruptMode(enum.IntEnum):
    Normal = 0b00
    MaskableInterrupt = 0b01
    NonMaskableInterrupt = 0b10
    MemoryAcknowledge = 0b11


@enum.unique
class RegisterLoad(enum.IntEnum):
    A = 0b000
    B = 0b001
    C = 0b010
    D = 0b011
    Offset = 0b100
    Bank = 0b101
    Temporary = 0b110
    Instruction = 0b111


@enum.unique
class LeftSelect(enum.IntEnum):
    A = 0b000
    B = 0b001
    C = 0b010
    D = 0b011
    Temporary = 0b100
    Zero = 0b101
    # 0b110
    # 0b111


@enum.unique
class RightSelect(enum.IntEnum):
    A = 0b000
    B = 0b001
    C = 0b010
    D = 0b011
    Temporary = 0b100
    # 0b101
    # 0b110
    # 0b111


@enum.unique
class RegisterWriteBackSelect(enum.IntEnum):
    MemoryDataRegister = 0b0
    AluResult = 0b1


@enum.unique
class AluFunction(enum.Enum):
    NoOperation = 0x00
    LeftPassThrough = 0x01


@enum.unique
class ShiftSelect(enum.Enum):
    ShiftLeft = 0b00
    LogicalShiftRight = 0b01
    ArithmeticShiftRight = 0b10
    PassThrough = 0b11


@enum.unique
class LogicSelect(enum.IntEnum):
    Clear = 0b0000
    Set = 0b1111
    Left = 0b1010
    Right = 0b1100
    NotLeft = 0b0101
    NotRight = 0b0011
    LeftOrRight = 0b1110
    NotLeftOrRight = 0b1101
    LeftOrNotRight = 0b1011
    NotLeftOrNotRight = 0b0111
    LeftAndRight = 0b1000
    NotLeftAndRight = 0b0100
    LeftAndNotRight = 0b0010
    NotLeftAndNotRight = 0b0001
    LeftXorRight = 0b0110
    AllNotLeftXorRight = 0b1001


@enum.unique
class AdderSelect(enum.IntEnum):
    Zero = 0b00
    One = 0b01
    CarryFlag = 0b10


@enum.unique
class CarrySelect(enum.IntEnum):
    Zero = 0b00
    AdderCarry = 0b01
    RightShiftCarry = 0b10
    LeftShiftCarry = 0b11


@enum.unique
class ResultSelect(enum.IntEnum):
    Status = 0b0
    AluResult = 0b1


@enum.unique
class PointerLoad(enum.IntEnum):
    ProgramCounter = 0b000
    Stack = 0b001
    X = 0b010
    Y = 0b011
    Temporary = 0b100
    # 0b101
    # 0b110
    # 0b111


@enum.unique
class PointerSelect(enum.IntEnum):
    ProgramCounter = 0b000
    Stack = 0b001
    X = 0b010
    Y = 0b011
    Temporary = 0b100
    IrqVector = 0b101
    NmiVector = 0b110
    SwiVector = 0b111


@enum.unique
class PointerLoadEnable(enum.IntEnum):
    Disable = 0x00
    LowByte = 0x01
    HighByte = 0x10
    FullWord = 0x11


@enum.unique
class PointerWriteBackSelect(enum.IntEnum):
    AluResult = 0b0
    AguResult = 0b1


@enum.unique
class OffsetMode(enum.IntEnum):
    Zero = 0b00
    Offset = 0b01
    One = 0b10
    NegativeOne = 0b11


@enum.unique
class JumpCondition(enum.IntEnum):
    Never = 0b000
    Equal = 0b001
    NotEqual = 0b010
    LessThan = 0b011
    GreaterOrEqual = 0b100
    SignedLessThan = 0b101
    SignedGreaterOrEqual = 0b110
    Always = 0b111


@dataclass
class State:
    interrupt_mode: InterruptMode
    opcode: OpcodeType
    step: InstructionStep

    @classmethod
    def decode(cls, state_address: StateAddress) -> Self:
        step_value = (state_address >> 0) & 0b111
        if State._is_valid_step(step_value):
            step = step_value

        opcode_value = (state_address >> 3) & 0b1111_1111

        is_extended_value = (state_address >> 11) & 0b1
        is_extended = is_extended_value == 1

        # Should check that the value is a valid opcode (perhaps there is not an opcode for that value)
        opcode: OpcodeType = (
            ExtendedOpcode(opcode_value) if is_extended else NormalOpcode(opcode_value)
        )

        # Same as above
        interrupt_mode = InterruptMode((state_address >> 12) & 0b11)

        return cls(
            interrupt_mode=interrupt_mode,
            opcode=opcode,
            step=step,
        )

    @staticmethod
    def _is_valid_step(step: int) -> TypeGuard[InstructionStep]:
        if step in range(8):
            return True
        raise ValueError(f"Valid InstructionStep must be in range(8), got {step}.")
