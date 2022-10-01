
class german_number_converter:
    number_map = {
        0: "Null",
        1: "Eins",
        2: "Zwei",
        3: "Drei",
        4: "Vier",
        5: "fünf",
        6: "Sechs",
        7: "Sieben",
        8: "Acht",
        9: "Neun",
        10: "Zehn",
        11: "Elf",
        12: "zwölf",
    }

    special_cases = {
        2: "zwan",
        6: "sech",
        7: "sieb",
    }

    @staticmethod
    def chunk_number(number: int, chunk_length: int = 3) -> list:
        """Converts a given number into a string, reverses the string, cuts in chucks of given length then reverses
        the chunked part back to original order and appends it to the chunks list.
        then the chunked number list is reversed again to restore original order."""
        chunks = [str(number)[::-1][i:i + chunk_length][::-1] for i in range(0, len(str(number)), chunk_length)]
        chunks.reverse()
        return chunks

    @staticmethod
    def is_hundreds(number: int) -> bool:
        return number >= 100 and number <= 999

    @staticmethod
    def get_number_flags(number: int) -> dict:
        nf = {}
        nf["string"] = str(number)
        nf["length"] = len(nf["string"])
        nf["has_second_digit"] = True if nf["length"] >= 2 else False
        nf["first_digit"] = int(nf["string"][0])
        nf["second_digit"] = int(nf["string"][nf["length"] - 2]) if nf["has_second_digit"] else False
        nf["last_digit"] = int(nf["string"][-1:]) if nf["length"] >= 1 else False
        nf["last_2_digits"] = int(nf["string"][-2:]) if nf["has_second_digit"] else False
        nf["between_13_and_19"] = True if nf["last_2_digits"] >= 13 and nf["last_2_digits"] <= 19 else False

        return nf

    @staticmethod
    def get_correct_zig(number: int) -> str:
        return "ßig" if number == 3 else "zig"

    def get_correct_number_suffix(self, num_chunks: int, current_chunk: int, number: int) -> list:
        chunk_length = len(str(number))
        result = []
        million_check = True if (num_chunks == 3 and current_chunk == 0) else False
        thousand_check = True if (num_chunks == 3 and current_chunk == 1) or (
                    num_chunks == 2 and current_chunk == 0) else False
        one_mil_check = True if num_chunks == 3 and chunk_length == 1 and number == 1 else False
        single_million_check = True if chunk_length == 1 and number > 1 else False
        one_thousand_check = True if thousand_check and chunk_length == 1 and number == 1 else False

        if one_mil_check:
            result.append('eine')
        if single_million_check:
            result.append(self.number_map.get(number))
        if one_thousand_check:
            result.append('ein')
        if million_check:
            result.append('million')
            if number > 1:
                result.append('en')
        if thousand_check:
            result.append('tausend')
        return result


    def get_number_string(self, number: int, glue=""):
        num_chunked = self.chunk_number(number)
        num_chunks = len(num_chunked)
        complete_number = []
        for z, chunk in enumerate(num_chunked):
            number_word = []
            number_flags = self.get_number_flags(chunk)
            if self.is_hundreds(int(chunk)):
                first_digit = number_flags.get("first_digit")
                hundret_word = "ein" if first_digit == 1 else self.number_map.get(first_digit)
                number_word.append(hundret_word)
                number_word.append("hundert")

            if number_flags.get("has_second_digit"):
                # checks for last 2
                sd = number_flags.get("second_digit")
                ld = number_flags.get("last_digit")
                ltd = number_flags.get("last_2_digits")
                if ld == 0 and sd in [2, 6, 7]:
                    # zwan, sech, sieb
                    number_word.append(self.special_cases.get(sd))
                    number_word.append(self.get_correct_zig(sd))
                elif ltd == 00:
                    # 100, 200, 400, etc
                    pass
                elif sd == 0:
                    # 01, 02, 03, 04, 05, 06, 07, 08, 09
                    number_word.append(self.number_map.get(ld))
                elif ltd in self.number_map:
                    # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
                    number_word.append(self.number_map.get(ltd))
                elif number_flags.get("between_13_and_19"):
                    # sechzehn, siebzehn OR dreizehn, vierzehn, fünfzehn, achtzehn, neunzehn
                    use_case = self.special_cases if ld in self.special_cases else self.number_map
                    number_word.append(use_case.get(ld))
                    number_word.append("zehn")
                else:
                    if ltd >= 20 and ld == 0:
                        # 20, 30, 40, 50, 60, 70, 80, 80
                        pass
                    else:
                        word = number_word.append("ein") if ltd >= 20 and ld == 1 else self.number_map.get(ld)
                        if word:
                            number_word.append(word)
                        number_word.append("und")

                    use_case = self.special_cases if sd in [2, 6, 7] else self.number_map
                    number_word.append(use_case.get(sd))
                    number_word.append(self.get_correct_zig(sd))
                if (suffix := self.get_correct_number_suffix(num_chunks, z, int(chunk))):
                    number_word += suffix  # merging lists
            else:
                if (suffix := self.get_correct_number_suffix(num_chunks, z, int(chunk))):
                    number_word += suffix  # merging lists
                else:
                    number_word.append(self.number_map.get(number_flags.get("last_digit")))
            complete_number += number_word  # merging lists
        return glue.join(complete_number).lower().title().replace("Ssig", "ßig")


if __name__ == "__main__":
    data = [123_456_789, 12_345_678, 1_234_567, 123_456, 12_345, 1_234, 123, 12, 1]
    gnt = german_number_converter()
    for d in data:
        print(str(d).ljust(15), gnt.get_number_string(d, glue="").ljust(95), gnt.get_number_string(d, glue="-"))
