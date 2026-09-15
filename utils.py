class utils:
    @staticmethod
    def reversed(num: int) -> int:
        sign = -1 if num < 0 else 1
        return sign * int(str(abs(num))[::-1])
    @staticmethod
    def formatter(num: int) -> tuple[str, str]:
        return bin(num), oct(num)
        