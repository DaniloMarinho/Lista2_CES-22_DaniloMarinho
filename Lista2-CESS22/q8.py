import abc

class Linguagem:
    def __init__(self, paradigmas):
        self.paradigmas = paradigmas

    def __repr__(self):
        return repr(self.paradigmas)

    @classmethod
    def python(cls):
        return cls(['funcional', 'imperativa', 'orientada a objeto'])

    @classmethod
    def javascript(cls):
        return cls(['orientada a eventos', 'funcional', 'imperativa'])

    @classmethod
    def c(cls):
        return cls(['imperativa', 'estruturada'])

    @staticmethod
    def isOlderThanFortran(year):
        #retorna se uma linguagem e mais antiga que o Fortran, baseada na sua data de criacao
        if(year < 1957):
            return "Sim"
        return "Nao"

class LinguagemMultiparadgima(object):
    __metaclass__ = abc.ABCMeta

    default_paradigms = ['multi-paradigma']

    @classmethod
    @abc.abstractmethod
    def get_paradigms(cls):
        return cls.default_paradigms

class Javascript(LinguagemMultiparadgima):
    def get_paradigms(self):
        return ['funcional'] + super(Javascript, self).get_paradigms()

print('Chamada do class method:')
print('Paradigmas do python: ')
print(Linguagem.python())
print('A vantagem se usar o class method e que, se decidirmos renomear a classe, nao sera necessario alterar os class methods, visto que "cls" faz referencia a classe.')
print('Chamada do static method:')
print('C e mais antiga que Fortran?')
print(Linguagem.isOlderThanFortran(1972))
print('A vantagem se usar o static method e que delimitamos o que pode ser acessado por esses metodos, evitando possiveis bugs associados a outras partes do codigo e simplificando a modificacao desse metodo. Alem disso, por ser um metodo independente da classe e mais facil de testar, visto que nao e necessario criar uma instancia da classe.')
print('Chamada do abstract method:')
print('Paradigmas do javascript: ')
print(Javascript().get_paradigms())
print('A vantagem se usar o abstract method e que ele ajuda na generalização desse metodo por herança, permitindo agrupar diversas classes semelhantes por herança a partir de uma classe mais abstrata que nao deve ser instanciada.')