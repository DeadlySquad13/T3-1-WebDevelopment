from models import ProgrammingLanguage, Ide, ProgrammingLanguageIde

# Набор языков программирования.
programming_languages = [
    ProgrammingLanguage(1, 'C++'),
    ProgrammingLanguage(2, 'C#'),
    ProgrammingLanguage(11, 'Java'),
    ProgrammingLanguage(22, 'Python'),
    ProgrammingLanguage(33, 'JavaScript'),
]
 
# Набор средств разработки.
ides = [
    Ide(2, 'CLion', 3500, 1),

    Ide(1, 'Resharper', 2500, 2),

    Ide(4, 'IntelliJ', 3500, 11),
    Ide(9, 'SublimeText', 0, 11),

    Ide(7, 'PyCharm', 6000, 22),
    Ide(10, 'Atom', 0, 22),

    Ide(3, 'VisualStudio', 0, 33),
    Ide(6, 'WebStorm', 1000, 33),
    Ide(8, 'Eclipse', 0, 33),
]
 
# Реализация много-ко-многим.
programming_languages_ides = [
    ProgrammingLanguageIde(1,2),
    ProgrammingLanguageIde(1,3),
    ProgrammingLanguageIde(1,8),
    ProgrammingLanguageIde(1,9),

    ProgrammingLanguageIde(2,1),
    ProgrammingLanguageIde(2,2),
    ProgrammingLanguageIde(2,3),
    ProgrammingLanguageIde(2,8),
    ProgrammingLanguageIde(2,9),

    ProgrammingLanguageIde(11,4),
    ProgrammingLanguageIde(11,8),
    ProgrammingLanguageIde(11,3),
    ProgrammingLanguageIde(11,6),
    ProgrammingLanguageIde(11,9),
    ProgrammingLanguageIde(11,10),

    ProgrammingLanguageIde(22,7),
    ProgrammingLanguageIde(22,8),
    ProgrammingLanguageIde(22,3),
    ProgrammingLanguageIde(22,6),
    ProgrammingLanguageIde(22,9),
    ProgrammingLanguageIde(22,10),
 
    ProgrammingLanguageIde(33,3),
    ProgrammingLanguageIde(33,6),
    ProgrammingLanguageIde(33,8),
    ProgrammingLanguageIde(33,9),
    ProgrammingLanguageIde(33,10),
]
 
