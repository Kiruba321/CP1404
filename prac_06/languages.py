from prac_06.programming_language import ProgrammingLanguage


def main():
    ruby_lang = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python_lang = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic_lang = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages_list = [ruby_lang, python_lang, visual_basic_lang]
    print("The dynamically typed languages are:")
    for lang in languages_list:
        if lang.is_dynamic():
            print(lang.lang_name)


main()





