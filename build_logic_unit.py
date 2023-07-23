import enum
import control_lines as ctrl


def logic_unit(function: ctrl.LogicSelect, left: int, right: int) -> int:
    Func = ctrl.LogicSelect

    return {
        Func.Clear: 0x00,
        Func.Set: 0xFF,
        Func.Left: left,
        Func.Right: right,
        Func.NotLeft: ~left,
        Func.NotRight: ~right,
        Func.LeftOrRight: left | right,
        Func.NotLeftOrRight: ~left | right,
        Func.LeftOrNotRight: left | ~right,
        Func.NotLeftOrNotRight: ~left | ~right,
        Func.LeftAndRight: left & right,
        Func.NotLeftAndRight: ~left & right,
        Func.LeftAndNotRight: left & ~right,
        Func.NotLeftAndNotRight: ~left & ~right,
        Func.LeftXorRight: left ^ right,
        Func.AllNotLeftXorRight: ~(left ^ right),
    }[function] & 0xFF


def write_table(table: list[int]):
    with open("logic_unit.bin", "wb") as file:
        file.write(bytes(table))


def main():
    table = []

    for address in range(2**20):
        left = address & 0xFF
        right = (address >> 8) & 0xFF
        function = (address >> 16) & 0xF

        result = logic_unit(
            LogicFunction(function),
            left,
            right,
        )

        table.append(result)

    write_table(table)


if __name__ == "__main__":
    main()
