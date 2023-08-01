from typing import Callable, Optional, NewType
from dataclasses import dataclass, field
from instructions.opcodes import *
from instructions.control_lines import *


ControlWord = NewType("ControlWord", int)

class InstructionMeta(type):
    def __init__(cls, name: str, bases: tuple[type, ...], dct: dict[str, Callable]):
        cls.opcodes: dict[OpcodeType, tuple]

    def __call__(cls, opcode: OpcodeType) -> bool:
        return opcode in cls.opcodes.keys()


@dataclass
class MicroOperation:
    reset_sequencer: bool = False
    alu_function: AluFunction = AluFunction.NoOperation
    address_type: AddressType = AddressType.Memory

    pointer_select: PointerSelect = PointerSelect.Temporary
    pointer_load: PointerLoad = PointerLoad.Temporary

    # TODO: UBR flag
    # If PointerSelect.ProgramCounter, use code, otherwise data
    access_type: Optional[MemoryAccessType] = None

    register_load: Optional[RegisterLoad] = None

    # TODO: Are these the most appropriate defaults?
    left_select: LeftSelect = LeftSelect.A
    right_select: RightSelect = RightSelect.A

    # Require to be set if RegisterLoadEnable = True
    register_writeback: Optional[RegisterWriteBackSelect] = None

    pointer_load_enable: PointerLoadEnable = PointerLoadEnable.Disable
    pointer_writeback: Optional[PointerWriteBackSelect] = None

    offset_mode: OffsetMode = OffsetMode.Zero
    jump_condition: JumpCondition = JumpCondition.Never

    def __post_init__(self):
        if self.access_type is None:
            if self.pointer_select is PointerSelect.ProgramCounter:
                self.access_type = MemoryAccessType.Code
            else:
                self.access_type = MemoryAccessType.Data

        assert not (self.register_load is not None and self.register_writeback is None)
        assert not (
            self.pointer_load_enable is not PointerLoadEnable.Disable
            and self.pointer_writeback is None
        )

    def encode_control_word(self) -> ControlWord:
        # Bits 0-3: RegisterLoadSelect
        return ControlWord(0)

TSTATE_ZERO = MicroOperation(
    pointer_select=PointerSelect.ProgramCounter,
)


@dataclass
class Microcode:
    # Needs strict typing on length of list
    micro_operations: list[MicroOperation] = field(default_factory=list)

    def __post_init__(self):
        self += TSTATE_ZERO

    def __iadd__(self, uop: MicroOperation) -> Self:
        self.micro_operations.append(uop)
        assert len(self.micro_operations) < 9
        return self


class AddressingMode(enum.Enum):
    PointerIndirectIndexed = enum.auto()  # EA = [ptr + imm]
    PointerIndirectOffset = enum.auto()  # EA = [ptr + reg]
    AbsolutePort = enum.auto()  # EA = <imm>
