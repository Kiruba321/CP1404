class ProgrammingLanguage:

    def __init__(self, lang_name, typing_style, supports_reflection, year_invented):
        self.lang_name = lang_name
        self.typing_style = typing_style
        self.supports_reflection = supports_reflection
        self.year_invented = year_invented

    def __str__(self):
        reflection_str = "Yes" if self.supports_reflection else "No"
        return f"{self.lang_name}, {self.typing_style} Typing, Reflection={reflection_str}, First appeared in {self.year_invented}"

    def is_dynamically_typed(self):
        return self.typing_style == "Dynamic"


def run_demo():
    ruby_lang = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python_lang = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic_lang = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [ruby_lang, python_lang, visual_basic_lang]
    print(python_lang)

    print("The dynamically typed languages are:")
    for lang in languages:
        if lang.is_dynamically_typed():
            print(lang.lang_name)


if __name__ == "__main__":
    run_demo()
