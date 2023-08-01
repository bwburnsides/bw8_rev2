from instructions.base import InstructionMeta, Microcode, MicroOperation
from instructions.opcodes import NormalOpcode, ExtendedOpcode, OpcodeType
from instructions.control_lines import *


class MoveRegister(metaclass=InstructionMeta):
    opcodes: dict[OpcodeType, tuple] = {
        NormalOpcode.MoveBtoA: (LeftSelect.B, RegisterLoad.A),
        NormalOpcode.MoveCtoA: (LeftSelect.C, RegisterLoad.A),
        NormalOpcode.MoveDtoA: (LeftSelect.D, RegisterLoad.A),
        NormalOpcode.MoveAtoB: (LeftSelect.A, RegisterLoad.B),
        NormalOpcode.MoveCtoB: (LeftSelect.C, RegisterLoad.B),
        NormalOpcode.MoveDtoB: (LeftSelect.D, RegisterLoad.B),
        NormalOpcode.MoveAtoC: (LeftSelect.A, RegisterLoad.C),
        NormalOpcode.MoveBtoC: (LeftSelect.B, RegisterLoad.C),
        NormalOpcode.MoveDtoC: (LeftSelect.D, RegisterLoad.C),
        NormalOpcode.MoveAtoD: (LeftSelect.A, RegisterLoad.D),
        NormalOpcode.MoveBtoD: (LeftSelect.B, RegisterLoad.D),
        NormalOpcode.MoveCtoD: (LeftSelect.C, RegisterLoad.D),
    }

    @classmethod
    def generate_microcode(cls, state: State) -> Microcode:
        try:
            source, destination = cls.opcodes[state.opcode]
        except KeyError:
            raise KeyError(
                f"Invalid opcode {state.opcode} for MoveRegister instruction."
            )

        microcode = Microcode()

        microcode += MicroOperation(
            left_select=source,
            alu_function=AluFunction.LeftPassThrough,
            register_load=destination,
            register_writeback=RegisterWriteBackSelect.AluResult,
            reset_sequencer=True,
        )

        return microcode
