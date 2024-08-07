# MAGOCINHO🧙‍♂️
O jogo acompanha o personagem principal que é o MagoCINho, ele é baseado no gnomo Crawly, e o objetivo dele é sobreviver aos guardas, coletar as moedas, poções e cogumelos pelo caminho. Será uma tarefa difícil, pois os inimigos irão perseguí-lo até pegá-lo no labirinto. Para o magocinho sobreviver nesse ambiente, que está infestado de guardas, ele precisa coletar poções, que o tornaram intangível para os vigias, e cogumelos, que aumenta sua velocidade. Após coletados, o jogador pode usar esses itens apertando as teclas ‘Q’ e ‘E’ respectivamente. Além disso, o magocinho pode coletar moedas que estãao distribuídas pelos corredores. Mudar a direção do magocinho também é muito fácil: apenas usar as teclas de setas para isso!

## Membros e divisão das tarefas
- <strong>Adrielly Alexandre</strong>: Gerência e idealização do projeto; Criação do design do jogo e todas as sprites; Criação de slides para a apresentação; Criação e execução da Tela Inicial; Criação e execução da Tela de Game Over; Implementação da trilha sonora; Apresentação do Slide.
- <strong>Angelina Santos</strong>: Integração da Tela Inicial ao jogo; Integração da Tela Game Over ao jogo; Design para o HUD do jogo; Otimização e integração da inteligência do segundo inimigo.
- <strong>Caio Lopes</strong>: Movimentação do jogador; Moeda e pontuação na tela; Incrementos na classe Item (poção).
- <strong>Gustavo Nogueira</strong>: Inteligência do Inimigo, incrementos na classe Inimigo; Inteligência do segundo inimigo.
- <strong>Luisa Longo</strong>:Movimentação do jogador; Moeda e pontuação na tela; Incrementos na classe Item (poção).
- <strong>Wesley Silveira</strong>: Gerência e idealização do projeto; Criação do esqueleto inicial do programa; Criação do repositório GitHub utilizado; Classe Player; Classe Item; Classe UI; Classe Vértice; Classe Inimigo; Classe Game; Classe Sprites; Apresentação do Slide; Implementação da animação das sprites.

## Arquitetura e organizacão do código
* __config__
> Esse arquivo é responsável por definir as principais __configurações do jogo__. Aqui estão definidas as dimensões da tela, o título do jogo, o tamanho dos tiles, as cores usadas, a música,  a velocidade dos personagens, e a taxa de quadros por segundo (FPS). Também tem as camadas de renderização, que determinam a ordem em que os elementos do jogo aparecem, como o chão e o jogador. As direções de movimento do jogador e alguns temporizadores para eventos especiais, como poções e cogumelos, também são configurados aqui. Por fim, há uma lista que representa o mapa do jogo, usando caracteres para marcar diferentes tipos de terreno e objetos.
* __inimigo__
> Esse arquivo cria a __classe inimigo__, que controla os inimigos no jogo. O inimigo é um sprite que se move pelo mapa, tentando seguir o jogador. Ele tem diferentes animações para cada direção (esquerda, direita, cima, baixo), e a direção muda quando ele chega em certos pontos chamados de vértices.
O inimigo escolhe a direção que o aproxima mais do jogador, mas evita voltar pelo mesmo caminho. Se ele não puder seguir diretamente o jogador, ele pega outra direção possível. A classe também gerencia a velocidade e a colisão com outros objetos no jogo. É uma parte importante para dar ao inimigo um comportamento funcional e “inteligente”, dentro do jogo.
* __vertice__
> A __classe Vertice__ armazena a posição e as direções possíveis de movimento a partir desse ponto, importante para a tomada de decisão do inimigo. Visualmente, o vértice é invisível aos olhos do jogador. Os principais atributos são “direcoes_posiveis”, que lista para onde o inimigo pode se mover, e número, que identifica o vértice. 
* __player__
> A __classe Player__ controla o personagem principal do jogo. Ela define a posição, imagem e velocidade do jogador e gerencia itens coletados, como poções e cogumelos. Durante o jogo, ela move o jogador conforme as teclas pressionadas e muda a imagem de acordo com a direção. Também verifica colisões com blocos, itens e inimigos. Se o jogador colidir com um inimigo e não estiver invencível, ele perde uma vida. O jogador pode usar poções e cogumelos pressionando teclas específicas (Q para poção e E para cogumelo), que ativam efeitos temporários.
* __main__
> O arquivo Main é responsável por criar as circunstâncias que permitem o jogo rodar no momento certo, assim como saber em que momento o jogo para. A __classe Tela Inicial__ tem como objetivo definir a tela que o programa apresenta antes do verdadeiro jogo começar. Nela são definidas funções que indicam quando e como o jogo sai da sua tela inicial (como por exemplo a função ‘fade_in’), outras que desenham elementos como a cor da tela, a logo, e até a música introdutória, além de atualizar a tela do jogo, permitindo que ele flua conforme esperado. A função principal do __jogo__ é a parte central onde tudo acontece, mantendo o jogo rodando enquanto o jogador está ativo. Dentro do loop principal, ela desempenha três funções principais. Primeiro, a função events() lida com eventos do jogo, como fechar a janela ou gerenciar temporizadores. Em seguida, a função update() atualiza os sprites e verifica quaisquer mudanças no estado do jogo. Por último, a função draw() é responsável por desenhar todos os elementos na tela e exibir a interface do jogo. Esse loop continua até que o jogador perca ou complete a fase. Temos também a classe que forma a tela de __Game Over__, que é similar a Tela Inicial, mas aparece apenas após o jogador perder a partida. Suas similaridades se mantêm também nos elementos que os compõem, já que essa classe também é escrito por funções que determinam em que momento a deve tela aparecer assim como sumir, além de seus componentes visuais. E por fim, essa aba contém a classe __GerenciadorDeEstados__, que instância o funcionamento das classes acima, para que elas ocorram na ordem correta.
* __sprites__
> O arquivo sprites.py define várias classes responsáveis pela criação e gerenciamento dos sprites no jogo: __Classe Block__ serve para criar blocos que o jogador não pode atravessar. Ela define onde o bloco fica no jogo e qual é o seu tamanho. A classe configura a imagem do bloco e a área onde ele pode colidir com o jogador ou outros objetos. __Classe Moeda__ é usada para criar um dos coletáveis do jogo, a moeda. Ela foi separada dos outros itens (poção e cogumelo) pois sua função é marcar a  pontuação do jogador em cada partida, mas o magocinho não consegue usá-las para nada além disso. A __classe Chao__ é usada para criar o chão onde o jogador pode andar. Ela coloca a imagem do piso nas coordenadas corretas e define seu tamanho. É basicamente o que forma o terreno do jogo, permitindo que o jogador se mova por cima dele. A __classe Barra__ adiciona um background que complementa os blocos de colisão, mostrando onde é a parede.
* __UI__
> A __classe UI__ é responsável por desenhar a interface do usuário no jogo. No método init, ela carrega as imagens necessárias para exibir ícones de itens e corações. As imagens são carregadas usando pygame.image.load e armazenadas em variáveis. O método desenhar_coracao desenha os corações na tela, começando com três corações vazios e depois substituindo alguns por corações cheios conforme a quantidade de corações que o jogador possui. O método display é chamado a cada frame para atualizar a tela com os ícones dos itens que o jogador tem, como cogumelo e poção, e desenha os corações atualizados. Os ícones são posicionados nas bordas da tela para indicar o estado atual do jogador.

## Capturas de Tela
<div style="display: flex; justify-content: space-around;">
  <img src="img\telamagocinho.webp" alt="Tela do jogo"width="712">
  <img src="img\telamenu.png" alt="Tela Menu"width="400">
  <img src="img\telagameover.webp" alt="Tela Game Over"width="382">
</div>

## Ferramentas, Frameworks e Bibliotecas utilizados
* __Discord /Whatsapp__
> Foram utilizadas essas ferramentas como principal meio de comunicação interna e também com os monitores para realizar as reuniões remotas.
* __Visual Studio Code__
> Utilizado para todo o desenvolvimento do código do jogo devido a sua integração com o GitHub e seus recursos variados.
* __Miro/Notion__
> Foi utilizado como ambiente de trabalho visual para o planejamento inicial da base do jogo.
* __GitHub/ GitHub Desktop__
> Utilizado através da criação de um repositório garantindo a atualização das alterações do código e facilitando o gerenciamento de mudanças no projeto sem perder as alterações anteriores.
* __Pixel Studio/ Photoshop__
> O Pixel Studio foi utilizado para a criação do design de todas as sprites e telas do jogo e o Photoshop foi usado para a edição do tamanho dessas sprites criadas.
* __Pygame__
> Biblioteca de desenvolvimento de jogos em Python, como a principal ferramenta para o desenvolvimento da interface gráfica e da dinâmica do jogo.
* __Random__
> Não é uma biblioteca externa, mas sim um módulo padrão do Python que implementa geradores de elementos aleatórios trazendo a imprevisibilidade e variedade na escolha de algum elemento.
* __os__
> Este módulo fornece uma maneira simples de usar funcionalidades que são dependentes do sistema operacional.
* __Sys__
> Utilizadas em geral para manipular diferentes partes do ambiente de tempo de execução Python, foi utilizado a função ‘exit’, para encerrar o jogo mais rapidamente.
* __Math__
> Biblioteca interna utilizada para executar operações matemáticas simples, como adição, subtração, multiplicação e divisão.

## Conceitos da disciplina aplicados
Os diversos conceitos aprendidos ao decorrer da disciplina foram utilizados durante a produção do jogo ‘MagoCINho’. Cada uma dessas noções foram fundamentais para que os componentes do projeto funcionasse conforme o previsto. Utilizamos **comandos condicionais** e **laços de repetição** para circunstanciar os eventos que devem ocorrer a cada etapa do projeto, as **listas** tiveram finalidades como auxiliar a construção do cenário e dos coletáveis; como também as **tuplas** que estabelecem as cores dos elementos do jogo, por exemplo.
Além disso, o emprego de **funções** favoreceu o desenvolvimento dos objetos das classes, tal qual os estudos sobre **Programação Orientada a Objetos (POO)**, uma exigência do projeto, facilitou a escrita do código, tornando mais fácil o seu entendimento e sua modificação.

## Desafios, Erros e Lições aprendidas
* __Qual foi o maior erro cometido durante o projeto? Como vocês lidaram com ele?__
> O maior erro cometido durante a confecção do projeto foi a falta de organização do tempo no início do trabalho, o que acabou prejudicando um pouco o andamento da construção do jogo. Entretanto, lidamos com isso ao atribuir definitivamente as tarefas de cada integrante do projeto, melhorando a organização interna e o uso do nosso tempo.
* __Qual foi o maior desafio enfrentado durante o projeto? Como vocês lidaram com ele?__
> O maior desafio do projeto foi desenvolver a inteligência do inimigo no jogo. Para superá-lo, realizamos pesquisas aprofundadas e consultamos referências de inteligências criadas para inimigos de outros jogos.
* __Quais as lições aprendidas durante o projeto?__
> Aprendemos a gerenciar nosso tempo de forma mais eficaz em projetos, nos aprofundamos em ferramentas com as quais não tínhamos familiaridade, como Pygame, GitHub, e Notion, além de aprendermos a delegar funções e a colaborar na criação de código em equipe.

## Instruções para execução e instalação
### Certifique-se de ter Python3 e Pygame instalados em seu computador

* Abra o terminal do seu sistema em uma pasta à sua escolha, copie e cole o comando abaixo:

#### Se você usa Windows, execute esse comando:
```
# Clone esse repositório
git clone  https://github.com/sillyveira/magocinho.git
#Entre na pasta do projeto
cd magocinho
#Execute o arquivo 'main.py'
py main.py
```
#### Se você usa MacOS ou Linux, execute esse comando:
```
# Clone esse repositório
git clone  https://github.com/sillyveira/magocinho.git
#Entre na pasta do projeto
cd magocinho
#Execute o arquivo 'main.py'
python3 main.py
```
Ou apenas baixe o arquivo .zip, extraia em algum lugar da sua escolha e execute o arquivo 'main.py'.

#
###### _Projeto referente a cadeira de Introdução a Programação do CIN-UFPE no período 2024.1._
