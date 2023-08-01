import enum
from typing import TypeGuard


@enum.unique
class NormalOpcode(enum.Enum):
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        assert count < 256, "Too many NormalOpcode entries."
        return count

    # --------------------------
    # CPU Management
    # --------------------------
    NoOperation = enum.auto()
    ExtendInstruction = enum.auto()
    ClearCarry = enum.auto()
    SetCarry = enum.auto()

    # --------------------------
    # Moves (8-bit)
    # --------------------------
    MoveBtoA = enum.auto()
    MoveCtoA = enum.auto()
    MoveDtoA = enum.auto()

    MoveAtoB = enum.auto()
    MoveCtoB = enum.auto()
    MoveDtoB = enum.auto()

    MoveAtoC = enum.auto()
    MoveBtoC = enum.auto()
    MoveDtoC = enum.auto()

    MoveAtoD = enum.auto()
    MoveBtoD = enum.auto()
    MoveCtoD = enum.auto()

    # --------------------------
    # Input to A
    # --------------------------
    InputPortToA = enum.auto()
    InputXIndexedToA = enum.auto()
    InputYIndexedToA = enum.auto()

    # --------------------------
    # Input to B
    # --------------------------
    InputPortToB = enum.auto()
    InputXIndexedToB = enum.auto()
    InputYIndexedToB = enum.auto()

    # --------------------------
    # Input to C
    # --------------------------
    InputPortToC = enum.auto()
    InputXIndexedToC = enum.auto()
    InputYIndexedToC = enum.auto()

    # --------------------------
    # Input to D
    # --------------------------
    InputPortToD = enum.auto()
    InputXIndexedToD = enum.auto()
    InputYIndexedToD = enum.auto()

    # --------------------------
    # Output from A
    # --------------------------
    OutputAtoPort = enum.auto()
    OutputAtoXIndexed = enum.auto()
    OutputAtoYIndexed = enum.auto()

    # --------------------------
    # Output from B
    # --------------------------
    OutputBtoPort = enum.auto()
    OutputBtoXIndexed = enum.auto()
    OutputBtoYIndexed = enum.auto()

    # --------------------------
    # Output from C
    # --------------------------
    OutputCtoPort = enum.auto()
    OutputCtoXIndexed = enum.auto()
    OutputCtoYIndexed = enum.auto()

    # --------------------------
    # Output from D
    # --------------------------
    OutputDtoPort = enum.auto()
    OutputDtoXIndexed = enum.auto()
    OutputDtoYIndexed = enum.auto()

    # --------------------------
    # Load A
    # --------------------------
    LoadAwithImmediate = enum.auto()
    LoadAfromAbsoluteAddress = enum.auto()

    LoadAfromXIndexed = enum.auto()
    LoadAfromXOffsetA = enum.auto()
    LoadAfromXOffsetB = enum.auto()
    LoadAfromXOffsetC = enum.auto()
    LoadAfromXOffsetD = enum.auto()

    LoadAfromYIndexed = enum.auto()
    LoadAfromYOffsetA = enum.auto()
    LoadAfromYOffsetB = enum.auto()
    LoadAfromYOffsetC = enum.auto()
    LoadAfromYOffsetD = enum.auto()

    LoadAfromSPIndexed = enum.auto()
    LoadAfromSPOffsetA = enum.auto()
    LoadAfromSPOffsetB = enum.auto()
    LoadAfromSPOffsetC = enum.auto()
    LoadAfromSPOffsetD = enum.auto()

    # --------------------------
    # Load B
    # --------------------------
    LoadBwithImmediate = enum.auto()
    LoadBfromAbsoluteAddress = enum.auto()

    LoadBfromXIndexed = enum.auto()
    LoadBfromXOffsetA = enum.auto()
    LoadBfromXOffsetB = enum.auto()
    LoadBfromXOffsetC = enum.auto()
    LoadBfromXOffsetD = enum.auto()

    LoadBfromYIndexed = enum.auto()
    LoadBfromYOffsetA = enum.auto()
    LoadBfromYOffsetB = enum.auto()
    LoadBfromYOffsetC = enum.auto()
    LoadBfromYOffsetD = enum.auto()

    LoadBfromSPIndexed = enum.auto()
    LoadBfromSPOffsetA = enum.auto()
    LoadBfromSPOffsetB = enum.auto()
    LoadBfromSPOffsetC = enum.auto()
    LoadBfromSPOffsetD = enum.auto()

    # --------------------------
    # Load C
    # --------------------------
    LoadCwithImmediate = enum.auto()
    LoadCfromAbsoluteAddress = enum.auto()

    LoadCfromXIndexed = enum.auto()
    LoadCfromXOffsetA = enum.auto()
    LoadCfromXOffsetB = enum.auto()
    LoadCfromXOffsetC = enum.auto()
    LoadCfromXOffsetD = enum.auto()

    LoadCfromYIndexed = enum.auto()
    LoadCfromYOffsetA = enum.auto()
    LoadCfromYOffsetB = enum.auto()
    LoadCfromYOffsetC = enum.auto()
    LoadCfromYOffsetD = enum.auto()

    LoadCfromSPIndexed = enum.auto()
    LoadCfromSPOffsetA = enum.auto()
    LoadCfromSPOffsetB = enum.auto()
    LoadCfromSPOffsetC = enum.auto()
    LoadCfromSPOffsetD = enum.auto()

    # --------------------------
    # Load D
    # --------------------------
    LoadDwithImmediate = enum.auto()
    LoadDfromAbsoluteAddress = enum.auto()

    LoadDfromXIndexed = enum.auto()
    LoadDfromXOffsetA = enum.auto()
    LoadDfromXOffsetB = enum.auto()
    LoadDfromXOffsetC = enum.auto()
    LoadDfromXOffsetD = enum.auto()

    LoadDfromYIndexed = enum.auto()
    LoadDfromYOffsetA = enum.auto()
    LoadDfromYOffsetB = enum.auto()
    LoadDfromYOffsetC = enum.auto()
    LoadDfromYOffsetD = enum.auto()

    LoadDfromSPIndexed = enum.auto()
    LoadDfromSPOffsetA = enum.auto()
    LoadDfromSPOffsetB = enum.auto()
    LoadDfromSPOffsetC = enum.auto()
    LoadDfromSPOffsetD = enum.auto()

    # --------------------------
    # Store A
    # --------------------------
    StoreAatAbsoluteAddress = enum.auto()

    StoreAatXIndexed = enum.auto()
    StoreAatXOffsetA = enum.auto()
    StoreAatXOffsetB = enum.auto()
    StoreAatXOffsetC = enum.auto()
    StoreAatXOffsetD = enum.auto()

    StoreAatYIndexed = enum.auto()
    StoreAatYOffsetA = enum.auto()
    StoreAatYOffsetB = enum.auto()
    StoreAatYOffsetC = enum.auto()
    StoreAatYOffsetD = enum.auto()

    StoreAatSPIndexed = enum.auto()
    StoreAatSPOffsetA = enum.auto()
    StoreAatSPOffsetB = enum.auto()
    StoreAatSPOffsetC = enum.auto()
    StoreAatSPOffsetD = enum.auto()

    # --------------------------
    # Store B
    # --------------------------
    StoreBatAbsoluteAddress = enum.auto()

    StoreBatXIndexed = enum.auto()
    StoreBatXOffsetA = enum.auto()
    StoreBatXOffsetB = enum.auto()
    StoreBatXOffsetC = enum.auto()
    StoreBatXOffsetD = enum.auto()

    StoreBatYIndexed = enum.auto()
    StoreBatYOffsetA = enum.auto()
    StoreBatYOffsetB = enum.auto()
    StoreBatYOffsetC = enum.auto()
    StoreBatYOffsetD = enum.auto()

    StoreBatSPIndexed = enum.auto()
    StoreBatSPOffsetA = enum.auto()
    StoreBatSPOffsetB = enum.auto()
    StoreBatSPOffsetC = enum.auto()
    StoreBatSPOffsetD = enum.auto()

    # --------------------------
    # Store C
    # --------------------------
    StoreCatAbsoluteAddress = enum.auto()

    StoreCatXIndexed = enum.auto()
    StoreCatXOffsetA = enum.auto()
    StoreCatXOffsetB = enum.auto()
    StoreCatXOffsetC = enum.auto()
    StoreCatXOffsetD = enum.auto()

    StoreCatYIndexed = enum.auto()
    StoreCatYOffsetA = enum.auto()
    StoreCatYOffsetB = enum.auto()
    StoreCatYOffsetC = enum.auto()
    StoreCatYOffsetD = enum.auto()

    StoreCatSPIndexed = enum.auto()
    StoreCatSPOffsetA = enum.auto()
    StoreCatSPOffsetB = enum.auto()
    StoreCatSPOffsetC = enum.auto()
    StoreCatSPOffsetD = enum.auto()

    # --------------------------
    # Store D
    # --------------------------
    StoreDatAbsoluteAddress = enum.auto()

    StoreDatXIndexed = enum.auto()
    StoreDatXOffsetA = enum.auto()
    StoreDatXOffsetB = enum.auto()
    StoreDatXOffsetC = enum.auto()
    StoreDatXOffsetD = enum.auto()

    StoreDatYIndexed = enum.auto()
    StoreDatYOffsetA = enum.auto()
    StoreDatYOffsetB = enum.auto()
    StoreDatYOffsetC = enum.auto()
    StoreDatYOffsetD = enum.auto()

    StoreDatSPIndexed = enum.auto()
    StoreDatSPOffsetA = enum.auto()
    StoreDatSPOffsetB = enum.auto()
    StoreDatSPOffsetC = enum.auto()
    StoreDatSPOffsetD = enum.auto()

    # --------------------------
    # Moves (16-bit)
    # --------------------------
    MoveYtoX = enum.auto()
    MoveABtoX = enum.auto()
    MoveCDtoX = enum.auto()

    MoveXtoY = enum.auto()
    MoveABtoY = enum.auto()
    MoveCDtoY = enum.auto()

    MoveXtoAB = enum.auto()
    MoveYtoAB = enum.auto()

    MoveXtoCD = enum.auto()
    MoveYtoCD = enum.auto()

    # --------------------------
    # Load (16-bit)
    # --------------------------
    LoadXwithImmediate = enum.auto()
    LoadXfromAbsoluteAddress = enum.auto()
    LoadXfromXIndexed = enum.auto()
    LoadXfromYIndexed = enum.auto()
    LoadXfromSPIndexed = enum.auto()

    LoadYwithImmediate = enum.auto()
    LoadYfromAbsoluteAddress = enum.auto()
    LoadYfromXIndexed = enum.auto()
    LoadYfromYIndexed = enum.auto()
    LoadYfromSPIndexed = enum.auto()

    # --------------------------
    # Store (16-bit)
    # --------------------------
    StoreXatAbsoluteAddress = enum.auto()
    StoreXatXIndexed = enum.auto()
    StoreXatYIndexed = enum.auto()
    StoreXatSPIndexed = enum.auto()

    StoreYatAbsoluteAddress = enum.auto()
    StoreYatXIndexed = enum.auto()
    StoreYatYIndexed = enum.auto()
    StoreYatSPIndexed = enum.auto()

    # --------------------------
    # 16-bit Operations
    # --------------------------
    LoadXIndexedEffectiveAddress = enum.auto()
    LoadYIndexedEffectiveAddress = enum.auto()
    LoadSPIndexedEffectiveAddress = enum.auto()

    IncrementX = enum.auto()
    IncrementY = enum.auto()
    DecrementX = enum.auto()
    DecrementY = enum.auto()

    # --------------------------
    # Stack Operations
    # --------------------------
    PushA = enum.auto()
    PushB = enum.auto()
    PushC = enum.auto()
    PushD = enum.auto()
    PushX = enum.auto()
    PushY = enum.auto()

    PopA = enum.auto()
    PopB = enum.auto()
    PopC = enum.auto()
    PopD = enum.auto()
    PopX = enum.auto()
    PopY = enum.auto()

    # --------------------------
    # Comparison
    # --------------------------
    CompareAwithImmediate = enum.auto()
    CompareBwithImmediate = enum.auto()
    CompareCwithImmediate = enum.auto()
    CompareDwithImmediate = enum.auto()

    # --------------------------
    # Control Flow
    # --------------------------
    CallAbsoluteAddress = enum.auto()
    CallRelativeAddress = enum.auto()
    Return = enum.auto()

    JumpToAbsoluteAddress = enum.auto()
    JumpToRelativeAddress = enum.auto()

    JumpToAbsoluteAddressIfOverflow = enum.auto()
    JumpToRelativeAddressIfOverflow = enum.auto()

    JumpToAbsoluteAddressIfNotOverflow = enum.auto()
    JumpToRelativeAddressIfNotOverflow = enum.auto()

    JumpToAbsoluteAddressIfSign = enum.auto()
    JumpToRelativeAddressIfSign = enum.auto()

    JumpToAbsoluteAddressIfNotSign = enum.auto()
    JumpToRelativeAddressIfNotSign = enum.auto()

    JumpToAbsoluteAddressIfEqual = enum.auto()
    JumpToRelativeAddressIfEqual = enum.auto()

    JumpToAbsoluteAddressIfNotEqual = enum.auto()
    JumpToRelativeAddressIfNotEqual = enum.auto()

    JumpToAbsoluteAddressIfCarry = enum.auto()
    JumpToRelativeAddressIfCarry = enum.auto()

    JumpToAbsoluteAddressIfNotCarry = enum.auto()
    JumpToRelativeAddressIfNotCarry = enum.auto()

    JumpToAbsoluteAddressIfBelowOrEqual = enum.auto()
    JumpToRelativeAddressIfBelowOrEqual = enum.auto()

    JumpToAbsoluteAddressIfAbove = enum.auto()
    JumpToRelativeAddressIfAbove = enum.auto()

    JumpToAbsoluteAddressIfLess = enum.auto()
    JumpToRelativeAddressIfLess = enum.auto()

    JumpToAbsoluteAddressIfGreaterOrEqual = enum.auto()
    JumpToRelativeAddressIfGreaterOrEqual = enum.auto()

    JumpToAbsoluteAddressIfLessOrEqual = enum.auto()
    JumpToRelativeAddressIfLessOrEqual = enum.auto()

    JumpToAbsoluteAddressIfGreater = enum.auto()
    JumpToRelativeAddressIfGreater = enum.auto()


@enum.unique
class ExtendedOpcode(enum.Enum):
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        assert count < 256, "Too many ExtendedOpcode entries."
        return count

    # --------------------------
    # CPU Management
    # --------------------------
    Halt = enum.auto()
    EnableInterrupts = enum.auto()
    DisableInterrupts = enum.auto()
    EnableUserDataAccess = enum.auto()
    DisableUserDataAccess = enum.auto()

    MoveAtoBR = enum.auto()
    MoveBRtoA = enum.auto()

    # --------------------------
    # Input to A
    # --------------------------
    InputXOffsetByAToA = enum.auto()
    InputXOffsetByBToA = enum.auto()
    InputXOffsetByCToA = enum.auto()
    InputXOffsetByDToA = enum.auto()

    InputYOffsetByAToA = enum.auto()
    InputYOffsetByBToA = enum.auto()
    InputYOffsetByCToA = enum.auto()
    InputYOffsetByDToA = enum.auto()

    # --------------------------
    # Input to B
    # --------------------------
    InputXOffsetByAToB = enum.auto()
    InputXOffsetByBToB = enum.auto()
    InputXOffsetByCToB = enum.auto()
    InputXOffsetByDToB = enum.auto()

    InputYOffsetByAToB = enum.auto()
    InputYOffsetByBToB = enum.auto()
    InputYOffsetByCToB = enum.auto()
    InputYOffsetByDToB = enum.auto()

    # --------------------------
    # Input to C
    # --------------------------
    InputXOffsetByAToC = enum.auto()
    InputXOffsetByBToC = enum.auto()
    InputXOffsetByCToC = enum.auto()
    InputXOffsetByDToC = enum.auto()

    InputYOffsetByAToC = enum.auto()
    InputYOffsetByBToC = enum.auto()
    InputYOffsetByCToC = enum.auto()
    InputYOffsetByDToC = enum.auto()

    # --------------------------
    # Input to D
    # --------------------------
    InputXOffsetByAToD = enum.auto()
    InputXOffsetByBToD = enum.auto()
    InputXOffsetByCToD = enum.auto()
    InputXOffsetByDToD = enum.auto()

    InputYOffsetByAToD = enum.auto()
    InputYOffsetByBToD = enum.auto()
    InputYOffsetByCToD = enum.auto()
    InputYOffsetByDToD = enum.auto()

    # out <port>, #immediate
    OutputImmediateToPort = enum.auto()

    # --------------------------
    # Output from A
    # --------------------------
    OutputAtoXOffsetByA = enum.auto()
    OutputAtoXOffsetByB = enum.auto()
    OutputAtoXOffsetByC = enum.auto()
    OutputAtoXOffsetByD = enum.auto()

    OutputAtoYOffsetByA = enum.auto()
    OutputAtoYOffsetByB = enum.auto()
    OutputAtoYOffsetByC = enum.auto()
    OutputAtoYOffsetByD = enum.auto()

    # --------------------------
    # Output from B
    # --------------------------
    OutputBtoXOffsetByA = enum.auto()
    OutputBtoXOffsetByB = enum.auto()
    OutputBtoXOffsetByC = enum.auto()
    OutputBtoXOffsetByD = enum.auto()

    OutputBtoYOffsetByA = enum.auto()
    OutputBtoYOffsetByB = enum.auto()
    OutputBtoYOffsetByC = enum.auto()
    OutputBtoYOffsetByD = enum.auto()

    # --------------------------
    # Output from C
    # --------------------------
    OutputCtoXOffsetByA = enum.auto()
    OutputCtoXOffsetByB = enum.auto()
    OutputCtoXOffsetByC = enum.auto()
    OutputCtoXOffsetByD = enum.auto()

    OutputCtoYOffsetByA = enum.auto()
    OutputCtoYOffsetByB = enum.auto()
    OutputCtoYOffsetByC = enum.auto()
    OutputCtoYOffsetByD = enum.auto()

    # --------------------------
    # Output from D
    # --------------------------
    OutputDtoXOffsetByA = enum.auto()
    OutputDtoXOffsetByB = enum.auto()
    OutputDtoXOffsetByC = enum.auto()
    OutputDtoXOffsetByD = enum.auto()

    OutputDtoYOffsetByA = enum.auto()
    OutputDtoYOffsetByB = enum.auto()
    OutputDtoYOffsetByC = enum.auto()
    OutputDtoYOffsetByD = enum.auto()

    # --------------------------
    # Stack Operations
    # --------------------------
    MoveXtoSP = enum.auto()
    MoveSPtoX = enum.auto()

    # --------------------------
    # 16-bit Operations
    # --------------------------
    LoadXOffsetByAEffectiveAddress = enum.auto()
    LoadXOffsetByBEffectiveAddress = enum.auto()
    LoadXOffsetByCEffectiveAddress = enum.auto()
    LoadXOffsetByDEffectiveAddress = enum.auto()

    LoadYOffsetByAEffectiveAddress = enum.auto()
    LoadYOffsetByBEffectiveAddress = enum.auto()
    LoadYOffsetByCEffectiveAddress = enum.auto()
    LoadYOffsetByDEffectiveAddress = enum.auto()

    LoadSPOffsetByAEffectiveAddress = enum.auto()
    LoadSPOffsetByBEffectiveAddress = enum.auto()
    LoadSPOffsetByCEffectiveAddress = enum.auto()
    LoadSPOffsetByDEffectiveAddress = enum.auto()

    # --------------------------
    # Add with Carry
    # --------------------------
    AddWithCarryAandA = enum.auto()
    AddWithCarryAandB = enum.auto()
    AddWithCarryAandC = enum.auto()
    AddWithCarryAandD = enum.auto()
    AddWithCarryAandImmediate = enum.auto()

    AddWithCarryBandA = enum.auto()
    AddWithCarryBandB = enum.auto()
    AddWithCarryBandC = enum.auto()
    AddWithCarryBandD = enum.auto()
    AddWithCarryBandImmediate = enum.auto()

    AddWithCarryCandA = enum.auto()
    AddWithCarryCandB = enum.auto()
    AddWithCarryCandC = enum.auto()
    AddWithCarryCandD = enum.auto()
    AddWithCarryCandImmediate = enum.auto()

    AddWithCarryDandA = enum.auto()
    AddWithCarryDandB = enum.auto()
    AddWithCarryDandC = enum.auto()
    AddWithCarryDandD = enum.auto()
    AddWithCarryDandImmediate = enum.auto()

    # --------------------------
    # Subtract with Carry
    # --------------------------
    SubtractWithCarryAandA = enum.auto()
    SubtractWithCarryAandB = enum.auto()
    SubtractWithCarryAandC = enum.auto()
    SubtractWithCarryAandD = enum.auto()
    SubtractWithCarryAandImmediate = enum.auto()

    SubtractWithCarryBandA = enum.auto()
    SubtractWithCarryBandB = enum.auto()
    SubtractWithCarryBandC = enum.auto()
    SubtractWithCarryBandD = enum.auto()
    SubtractWithCarryBandImmediate = enum.auto()

    SubtractWithCarryCandA = enum.auto()
    SubtractWithCarryCandB = enum.auto()
    SubtractWithCarryCandC = enum.auto()
    SubtractWithCarryCandD = enum.auto()
    SubtractWithCarryCandImmediate = enum.auto()

    SubtractWithCarryDandA = enum.auto()
    SubtractWithCarryDandB = enum.auto()
    SubtractWithCarryDandC = enum.auto()
    SubtractWithCarryDandD = enum.auto()
    SubtractWithCarryDandImmediate = enum.auto()

    # --------------------------
    # Bitwise AND
    # --------------------------
    BitwiseAndAandB = enum.auto()
    BitwiseAndAandC = enum.auto()
    BitwiseAndAandD = enum.auto()
    BitwiseAndAandImmediate = enum.auto()

    BitwiseAndBandA = enum.auto()
    BitwiseAndBandC = enum.auto()
    BitwiseAndBandD = enum.auto()
    BitwiseAndBandImmediate = enum.auto()

    BitwiseAndCandA = enum.auto()
    BitwiseAndCandB = enum.auto()
    BitwiseAndCandD = enum.auto()
    BitwiseAndCandImmediate = enum.auto()

    BitwiseAndDandA = enum.auto()
    BitwiseAndDandB = enum.auto()
    BitwiseAndDandC = enum.auto()
    BitwiseAndDandImmediate = enum.auto()

    # --------------------------
    # Bitwise OR
    # --------------------------
    BitwiseOrAandB = enum.auto()
    BitwiseOrAandC = enum.auto()
    BitwiseOrAandD = enum.auto()
    BitwiseOrAandImmediate = enum.auto()

    BitwiseOrBandA = enum.auto()
    BitwiseOrBandC = enum.auto()
    BitwiseOrBandD = enum.auto()
    BitwiseOrBandImmediate = enum.auto()

    BitwiseOrCandA = enum.auto()
    BitwiseOrCandB = enum.auto()
    BitwiseOrCandD = enum.auto()
    BitwiseOrCandImmediate = enum.auto()

    BitwiseOrDandA = enum.auto()
    BitwiseOrDandB = enum.auto()
    BitwiseOrDandC = enum.auto()
    BitwiseOrDandImmediate = enum.auto()

    # --------------------------
    # Bitwise XOR
    # --------------------------
    BitwiseXorAandA = enum.auto()
    BitwiseXorAandB = enum.auto()
    BitwiseXorAandC = enum.auto()
    BitwiseXorAandD = enum.auto()
    BitwiseXorAandImmediate = enum.auto()

    BitwiseXorBandA = enum.auto()
    BitwiseXorBandB = enum.auto()
    BitwiseXorBandC = enum.auto()
    BitwiseXorBandD = enum.auto()
    BitwiseXorBandImmediate = enum.auto()

    BitwiseXorCandA = enum.auto()
    BitwiseXorCandB = enum.auto()
    BitwiseXorCandC = enum.auto()
    BitwiseXorCandD = enum.auto()
    BitwiseXorCandImmediate = enum.auto()

    BitwiseXorDandA = enum.auto()
    BitwiseXorDandB = enum.auto()
    BitwiseXorDandC = enum.auto()
    BitwiseXorDandD = enum.auto()
    BitwiseXorDandImmediate = enum.auto()

    # --------------------------
    # Bitwise NOT
    # --------------------------
    BitwiseNotA = enum.auto()
    BitwiseNotB = enum.auto()
    BitwiseNotC = enum.auto()
    BitwiseNotD = enum.auto()

    # --------------------------
    # Negation (Twos Complement)
    # --------------------------
    NegateA = enum.auto()
    NegateB = enum.auto()
    NegateC = enum.auto()
    NegateD = enum.auto()

    # --------------------------
    # Shift Right with Carry
    # --------------------------
    ShiftARightWithCarry = enum.auto()
    ShiftBRightWithCarry = enum.auto()
    ShiftCRightWithCarry = enum.auto()
    ShiftDRightWithCarry = enum.auto()

    # --------------------------
    # Arithmetic Shift Right
    # --------------------------
    ArithmeticShiftARight = enum.auto()
    ArithmeticShiftBRight = enum.auto()
    ArithmeticShiftCRight = enum.auto()
    ArithmeticShiftDRight = enum.auto()

    # --------------------------
    # Increment / Decrement
    # --------------------------
    IncrementA = enum.auto()
    IncrementB = enum.auto()
    IncrementC = enum.auto()
    IncrementD = enum.auto()

    DecrementA = enum.auto()
    DecrementB = enum.auto()
    DecrementC = enum.auto()
    DecrementD = enum.auto()

    # --------------------------
    # Comparison
    # --------------------------

    CompareAandA = enum.auto()
    CompareAandB = enum.auto()
    CompareAandC = enum.auto()
    CompareAandD = enum.auto()

    CompareBandA = enum.auto()
    CompareBandB = enum.auto()
    CompareBandC = enum.auto()
    CompareBandD = enum.auto()

    CompareCandA = enum.auto()
    CompareCandB = enum.auto()
    CompareCandC = enum.auto()
    CompareCandD = enum.auto()

    CompareDandA = enum.auto()
    CompareDandB = enum.auto()
    CompareDandC = enum.auto()
    CompareDandD = enum.auto()

    TestBitA = enum.auto()
    TestBitB = enum.auto()
    TestBitC = enum.auto()
    TestBitD = enum.auto()

    # --------------------------
    # Control
    # --------------------------

    CallXPointer = enum.auto()
    CallYPointer = enum.auto()
    SoftwareInterrupt = enum.auto()
    ReturnFromInterrupt = enum.auto()

    JumpToXPointer = enum.auto()
    JumpToYPointer = enum.auto()

    JumpToXPointerIfOverflow = enum.auto()
    JumpToYPointerIfOverflow = enum.auto()

    JumpToXPointerIfNotOverflow = enum.auto()
    JumpToYPointerIfNotOverflow = enum.auto()

    JumpToXPointerIfSign = enum.auto()
    JumpToYPointerIfSign = enum.auto()

    JumpToXPointerIfNotSign = enum.auto()
    JumpToYPointerIfNotSign = enum.auto()

    JumpToXPointerIfEqual = enum.auto()
    JumpToYPointerIfEqual = enum.auto()

    JumpToXPointerIfNotEqual = enum.auto()
    JumpToYPointerIfNotEqual = enum.auto()

    JumpToXPointerIfCarry = enum.auto()
    JumpToYPointerIfCarry = enum.auto()

    JumpToXPointerIfNotCarry = enum.auto()
    JumpToYPointerIfNotCarry = enum.auto()

    JumpToXPointerIfBelowOrEqual = enum.auto()
    JumpToYPointerIfBelowOrEqual = enum.auto()

    JumpToXPointerIfAbove = enum.auto()
    JumpToYPointerIfAbove = enum.auto()

    JumpToXPointerIfLess = enum.auto()
    JumpToYPointerIfLess = enum.auto()

    JumpToXPointerIfGreaterOrEqual = enum.auto()
    JumpToYPointerIfGreaterOrEqual = enum.auto()

    JumpToXPointerIfLessOrEqual = enum.auto()
    JumpToYPointerIfLessOrEqual = enum.auto()

    JumpToXPointerIfGreater = enum.auto()
    JumpToYPointerIfGreater = enum.auto()


OpcodeType = ExtendedOpcode | NormalOpcode
