from random import randint

class Forca:

    dict_palavras = {1: 'paralelepipedo', 2: 'sara', 3: 'megumi'}
    
    def __init__(self) -> None:
        self.palavra_secreta = self.dict_palavras[randint(1, 3)]
        self.letras_corretas = set()
        self.vidas = 5
    
    def desenhar(self, letra=None):
        if letra is None:
            print(len(self.palavra_secreta) * '_')
            return
        
        for i in self.palavra_secreta:
            if i == letra or i in self.letras_corretas:
                print(i, end='')
                self.letras_corretas.add(i)
                continue
            print('_', end='')


    def testar(self, letra):
        if isinstance(letra , str) and len(letra) == 1 and letra.isalpha():
            return True
        return False
    
    def vencer(self):
        return set(self.palavra_secreta) == self.letras_corretas and self.vidas >= 0

    def iniciar_jogo(self):
        count = 0
        while self.vidas > 0:
            if count == 0:
                self.desenhar()
                count += 1
            letra = input('letra: ')
            if self.testar(letra):
                if letra not in self.palavra_secreta:
                    self.vidas -= 1
                print(f'vidas: {self.vidas}')
                print()
                self.desenhar(letra)
                print()
            if self.vencer():
                print('Parabéns, você venceu!!')
                break
        else:
            print('Perdeu!')


if __name__ == '__main__':
    jogo = Forca()
    jogo.iniciar_jogo()
            
            
        