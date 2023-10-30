from random import choice, shuffle
from characters import chars_dict
from Utilities import get_int_input, build_question


class Generator:
    _selections = dict()
    _char_labels= list(chars_dict.keys())
    _generated_string = []

    def __init__(self):
        print("Welcome to password generator!")
        for label in self._char_labels:
            self._selections[label] = get_int_input(build_question(label))

        self._generated_string = self._select_random()
        shuffle(self._generated_string)
        print(self)

    def _select_random(self) -> list[str]:
        ret_string = []
        for label, selection in self._selections.items():
            for i in range(selection):
                ret_string.append(choice(chars_dict[label]))

        return ret_string

    def __str__(self):
        return f"Your new password is {"".join(self._generated_string)}"
