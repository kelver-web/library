# Projeto Django library
Instalção do projeto:

1. Clone o repositório
   '''
   git clone https://github.com/kelver-web/library.git
   '''
2. entre na pasta library
   '''
   cd library
   '''
3. Crie um virtualenv com python 3.8
   '''
   python -m venv venv ou python3 -m venv venv
   '''
4. Ative o virtualenv
   '''
   source venv/bin/activate para sistemas Unix
   venv/Scripts/activate    para sistemas Windows
   '''
5. Instale as dependências
   '''
   pip install -r requirements.txt
   '''
6. rode com python ou python3 manage.py runserver
7. crie as tabelas necessárias
   '''
   python3 ou python manage.py migrate
   '''
8. crie um super usuário
   '''
   python3 ou python manage.py createsuperuser
   '''
9. Crie suas categorias
10. Adicione os livros
11. no campo de imagem da tabela de Books pode adicionar o url do caminho da imagem.
