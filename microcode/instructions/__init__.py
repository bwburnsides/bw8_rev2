from typing import Callable, Optional
from dataclasses import dataclass, field

from instructions.opcodes import OpcodeType, NormalOpcode, ExtendedOpcode

from instructions.base import Microcode, MicroOperation
from instructions.move_register import MoveRegister
from instructions.input_register import InputRegister
