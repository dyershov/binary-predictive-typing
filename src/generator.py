class ChoiceGenerator:
    def __init__(self, opt_no):
        self.__opt_no = opt_no
        self.__letter_options = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        self.__options = [self.__letter_options]
        self.__new_line = False
        self.__space = False


    def up(self):
        if len(self.__options) <= 1:
            return "Enter"
        else:
            return ".."

    def dn(self):
        return "Space"

    def options(self):
        return [" ".join(self.__options[-1][self.__option_slice(i)]) for i in range(self.__opt_no)]

    def choose(self, opt):
        option_slice = self.__option_slice(opt)
        if option_slice.stop - option_slice.start != 0:
            self.__options.append(self.__options[-1][option_slice])

    def go_up(self):
        if len(self.__options) <= 1:
            self.__new_line = True
        else:
            self.__options.pop()

    def go_dn(self):
        self.__space = True

    def flush(self):
        if self.__new_line:
            self.__new_line = False
            return "\n"
        if self.__space:
            self.__space = False
            return " "
        if len(self.__options[-1]) <= 1:
            result = self.__options[-1].pop()
            self.__options = [self.__letter_options]
            return result
        return ""

    def __option_slice(self, opt):
        q, r = divmod(len(self.__options[-1]), self.__opt_no)
        return slice(opt*q + min(opt, r), (opt+1)*q + min(opt+1, r))
