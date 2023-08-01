from dataclasses import dataclass, field
import enum
from typing import Self, Optional, Callable

from instructions import (
    OpcodeType,
    NormalOpcode,
    ExtendedOpcode,
    Microcode,
    MicroOperation,
    MoveRegister,
    InputRegister,
)

from instructions.control_lines import (
    State,
    MemoryAccessType,
    AddressType,
    RegisterLoad,
    LeftSelect,
    RightSelect,
    RegisterWriteBackSelect,
    PointerLoad,
    PointerSelect,
    PointerWriteBackSelect,
    OffsetMode,
    JumpCondition,
    AluFunction,
    PointerLoadEnable,
)
import instructions.control_lines as ctrl


def generate_microcode(state: State) -> Microcode:
    microcode = Microcode()

    if state.interrupt_mode != ctrl.InterruptMode.Normal:
        # TODO: How to handle interrupts. Would like to not have microcode
        # in main ROM in order to reduce overall size of ROM.
        pass

    if state.opcode is NormalOpcode.NoOperation:
        microcode += MicroOperation(reset_sequencer=True)

    if MoveRegister(state.opcode):
        return MoveRegister.generate_microcode(state)

    if InputRegister(state.opcode):
        return InputRegister.generate_microcode(state)

    if state.opcode is NormalOpcode.InputPortToA:
        microcode += MicroOperation(
            pointer_select=PointerSelect.ProgramCounter,
            offset_mode=OffsetMode.One,
            # Load zero into high byte of IO pointer
            left_select=LeftSelect.Zero,
            alu_function=AluFunction.LeftPassThrough,
            register_writeback=RegisterWriteBackSelect.AluResult,
            pointer_writeback=PointerWriteBackSelect.AluResult,
            pointer_load=PointerLoad.Temporary,
            pointer_load_enable=PointerLoadEnable.HighByte,
        )

    return Microcode()


def main(args: list[str]) -> int:
    microcode = []

    for state_address in ctrl.state_range():
        state = State.decode(state_address)
        microcode.append(generate_microcode(state))

    return 0


if __name__ == "__main__":
    import sys

    code = main(sys.argv)
    exit(code)
