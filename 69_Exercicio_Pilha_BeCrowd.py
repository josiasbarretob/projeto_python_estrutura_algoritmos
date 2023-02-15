pilha = []
expressao = input()
for i in range(len(expressao)):
    if expressao[i] == '(':
        pilha.append('(')
    elif expressao[i] == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('correct')
else:
    print('incorrect')
