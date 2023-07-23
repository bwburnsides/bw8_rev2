from instructions.opcodes import NormalOpcode, ExtendedOpcode
from instructions.base import *
from instructions.control_lines import *


class InputRegister(metaclass=InstructionMeta):
    opcodes = {
        # --------------------------
        # Input to A
        # --------------------------
        NormalOpcode.InputPortToA: (AddressingMode.AbsolutePort, RegisterLoad.A),
        NormalOpcode.InputXIndexedToA: (AddressingMode.PointerIndirectIndexed, 0),
        NormalOpcode.InputYIndexedToA: (AddressingMode.PointerIndirectIndexed, 0),
        ExtendedOpcode.InputXOffsetByAToA: (AddressingMode.PointerIndirectOffset, 0),
        ExtendedOpcode.InputXOffsetByBToA: (AddressingMode.PointerIndirectOffset, 0),
        ExtendedOpcode.InputXOffsetByCToA: (AddressingMode.PointerIndirectOffset, 0),
        ExtendedOpcode.InputXOffsetByDToA: (AddressingMode.PointerIndirectOffset, 0),
        ExtendedOpcode.InputYOffsetByAToA: (AddressingMode.PointerIndirectOffset, 0),
        ExtendedOpcode.InputYOffsetByBToA: (AddressingMode.PointerIndirectOffset, 0),
        ExtendedOpcode.InputYOffsetByCToA: (AddressingMode.PointerIndirectOffset, 0),
        ExtendedOpcode.InputYOffsetByDToA: (AddressingMode.PointerIndirectOffset, 0),
        # --------------------------
        # Input to B
        # --------------------------
        NormalOpcode.InputPortToB: (AddressingMode.AbsolutePort, RegisterLoad.B),
        NormalOpcode.InputXIndexedToB: (AddressingMode.PointerIndirectIndexed, 0),
        NormalOpcode.InputYIndexedToB: (AddressingMode.PointerIndirectIndexed, 0),
        ExtendedOpcode.InputXOffsetByAToB: (AddressingMode.PointerIndirectOffset, 0),
        ExtendedOpcode.InputXOffsetByBToB: (AddressingMode.PointerIndirectOffset, 0),
        ExtendedOpcode.InputXOffsetByCToB: (AddressingMode.PointerIndirectOffset, 0),
        ExtendedOpcode.InputXOffsetByDToB: (AddressingMode.PointerIndirectOffset, 0),
        ExtendedOpcode.InputYOffsetByAToB: (AddressingMode.PointerIndirectOffset, 0),
        ExtendedOpcode.InputYOffsetByBToB: (AddressingMode.PointerIndirectOffset, 0),
        ExtendedOpcode.InputYOffsetByCToB: (AddressingMode.PointerIndirectOffset, 0),
        ExtendedOpcode.InputYOffsetByDToB: (AddressingMode.PointerIndirectOffset, 0),
        # --------------------------
        # Input to C
        # --------------------------
        NormalOpcode.InputPortToC: (AddressingMode.AbsolutePort, RegisterLoad.C),
        NormalOpcode.InputXIndexedToC: (AddressingMode.PointerIndirectIndexed, 0),
        NormalOpcode.InputYIndexedToC: (AddressingMode.PointerIndirectIndexed, 0),
        ExtendedOpcode.InputXOffsetByAToC: (AddressingMode.PointerIndirectOffset, 0),
        ExtendedOpcode.InputXOffsetByBToC: (AddressingMode.PointerIndirectOffset, 0),
        ExtendedOpcode.InputXOffsetByCToC: (AddressingMode.PointerIndirectOffset, 0),
        ExtendedOpcode.InputXOffsetByDToC: (AddressingMode.PointerIndirectOffset, 0),
        ExtendedOpcode.InputYOffsetByAToC: (AddressingMode.PointerIndirectOffset, 0),
        ExtendedOpcode.InputYOffsetByBToC: (AddressingMode.PointerIndirectOffset, 0),
        ExtendedOpcode.InputYOffsetByCToC: (AddressingMode.PointerIndirectOffset, 0),
        ExtendedOpcode.InputYOffsetByDToC: (AddressingMode.PointerIndirectOffset, 0),
        # --------------------------
        # Input to D
        # --------------------------
        NormalOpcode.InputPortToD: (AddressingMode.AbsolutePort, RegisterLoad.D),
        NormalOpcode.InputXIndexedToD: (AddressingMode.PointerIndirectIndexed, 0),
        NormalOpcode.InputYIndexedToD: (AddressingMode.PointerIndirectIndexed, 0),
        ExtendedOpcode.InputXOffsetByAToD: (AddressingMode.PointerIndirectOffset, 0),
        ExtendedOpcode.InputXOffsetByBToD: (AddressingMode.PointerIndirectOffset, 0),
        ExtendedOpcode.InputXOffsetByCToD: (AddressingMode.PointerIndirectOffset, 0),
        ExtendedOpcode.InputXOffsetByDToD: (AddressingMode.PointerIndirectOffset, 0),
        ExtendedOpcode.InputYOffsetByAToD: (AddressingMode.PointerIndirectOffset, 0),
        ExtendedOpcode.InputYOffsetByBToD: (AddressingMode.PointerIndirectOffset, 0),
        ExtendedOpcode.InputYOffsetByCToD: (AddressingMode.PointerIndirectOffset, 0),
        ExtendedOpcode.InputYOffsetByDToD: (AddressingMode.PointerIndirectOffset, 0),
    }

    @classmethod
    def generate_microcode(cls, state: State) -> Microcode:
        try:
            addressing_mode, operands = cls.opcodes[state.opcode]
        except KeyError:
            raise KeyError(
                f"Invalid opcode {state.opcode} for InputRegister instruction."
            )

        match addressing_mode:
            case AddressingMode.AbsolutePort:
                return cls.generate_absolute_port_microcode(operands)
            case AddressingMode.PointerIndirectIndexed:
                return cls.generate_pointer_indirect_indexed_microcode(operands)
            case AddressingMode.PointerIndirectOffset:
                return cls.generate_pointer_indirect_offset_microcode(operands)
            case _:
                raise ValueError(
                    f"Invalid addressing mode {addressing_mode} for InputRegistr instruction."
                )

    @classmethod
    def generate_absolute_port_microcode(cls, register_load: RegisterLoad) -> Microcode:
        microcode = Microcode()

        # Calculate and save PC + 1
        microcode += MicroOperation(
            pointer_select=PointerSelect.ProgramCounter,
            offset_mode=OffsetMode.One,
            pointer_load=PointerLoad.ProgramCounter,
            pointer_writeback=PointerWriteBackSelect.AguResult,
            pointer_load_enable=PointerLoadEnable.FullWord,
        )

        # Read in port immediate
        microcode += MicroOperation(
            register_writeback=RegisterWriteBackSelect.MemoryDataRegister,
            pointer_writeback=PointerWriteBackSelect.AluResult,
            pointer_load=PointerLoad.Temporary,
            pointer_load_enable=PointerLoadEnable.LowByte,
        )

        # Clear high byte of pointer
        microcode += MicroOperation(
            left_select=LeftSelect.Zero,
            alu_function=AluFunction.LeftPassThrough,
            register_writeback=RegisterWriteBackSelect.AluResult,
            pointer_writeback=PointerWriteBackSelect.AluResult,
            pointer_load=PointerLoad.Temporary,
            pointer_load_enable=PointerLoadEnable.HighByte,
        )

        # Compute IO address
        microcode += MicroOperation(
            pointer_select=PointerSelect.Temporary,
            address_type=AddressType.Io,
        )

        # Read into register
        microcode += MicroOperation(
            register_writeback=RegisterWriteBackSelect.MemoryDataRegister,
            register_load=register_load,
            reset_sequencer=True,
        )

        return microcode

    @classmethod
    def generate_pointer_indirect_indexed_microcode(cls, operands) -> Microcode:
        microcode = Microcode()

        # Calculate and save PC + 1
        microcode += MicroOperation(
            pointer_select=PointerSelect.ProgramCounter,
            offset_mode=OffsetMode.One,
            pointer_load=PointerLoad.ProgramCounter,
            pointer_writeback=PointerWriteBackSelect.AguResult,
            pointer_load_enable=PointerLoadEnable.FullWord,
        )

        return microcode

    @classmethod
    def generate_pointer_indirect_offset_microcode(cls, operands) -> Microcode:
        return Microcode()
