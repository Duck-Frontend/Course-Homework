class SuperStr(str):
    """Нечего не придумал, но что-то написать нужно"""

    def is_repeatance(self, s):
        if not s or not self:
            return False
        n = len(self) / len(s)
        return n.is_integer() and self == s * int(n)

    def is_palindrom(self):
        s_lower = self.lower()
        return s_lower == s_lower[::-1]
