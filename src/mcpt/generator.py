class ChoiceGenerator:
    __LETTER__ = 0
    __WORD__ = 1
    __SENTENCE__ = 2

    def __init__(self, opt_no, alphabet, word_ac=None):
        self.__opt_no = opt_no
        self.__alphabet = alphabet
        self.__word_ac = word_ac
        self.__options = [self.__alphabet]
        self.__mode = self.__LETTER__
        self.__word_prefix = ""
        self.__result = ""


    def up(self):
        if self.__mode == self.__LETTER__:
            if len(self.__options) <= 1:
                if self.__word_ac is None or self.__word_prefix == "":
                    return "Enter"
                return " ".join(self.__word_ac(self.__word_prefix))
            else:
                return ".."

        if self.__mode == self.__WORD__:
            if len(self.__options) <= 1:
                return "A B C"
            else:
                return ".."

    def dn(self):
        return "Space"

    def options(self):
        print(self.__options)
        return [" ".join(self.__options[-1][self.__option_slice(i)]) for i in range(self.__opt_no)]

    def choose(self, opt):
        option_slice = self.__option_slice(opt)
        if option_slice.stop - option_slice.start == 1:
            if self.__mode == self.__LETTER__:
                letter = self.__options[-1][option_slice].pop()
                self.__word_prefix += letter
                self.__result += letter
            if self.__mode == self.__WORD__:
                word = self.__options[-1][option_slice].pop()
                self.__result += word[len(self.__word_prefix):] + " "
                self.__word_prefix = ""
            self.__options = [self.__alphabet]
            self.__mode = self.__LETTER__
        if option_slice.stop - option_slice.start > 1:
            self.__options.append(self.__options[-1][option_slice])

    def go_up(self):
        if self.__mode == self.__LETTER__:
            if len(self.__options) <= 1:
                if self.__word_ac is None or self.__word_prefix == "":
                    self.__result += "\n"
                else:
                    self.__options = [self.__word_ac(self.__word_prefix)]
                    self.__mode = self.__WORD__
            else:
                self.__options.pop()
            return

        if self.__mode == self.__WORD__:
            if len(self.__options) <= 1:
                self.__options = [self.__alphabet]
                self.__mode = self.__LETTER__
            else:
                self.__options.pop()
            return

    def go_dn(self):
        self.__word_prefix = ""
        self.__mode = self.__LETTER__
        self.__options = [self.__alphabet]
        self.__result += " "

    def flush(self):
        result = self.__result
        self.__result = ""
        return result

    def __option_slice(self, opt):
        q, r = divmod(len(self.__options[-1]), self.__opt_no)
        return slice(opt*q + min(opt, r), (opt+1)*q + min(opt+1, r))
