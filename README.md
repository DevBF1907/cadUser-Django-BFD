# 🧑‍💻 Sistema de Cadastro de Usuários — Django

Projeto desenvolvido com **Django** com o objetivo de implementar um **sistema simples e funcional de cadastro de usuários**, incluindo interface web, persistência em banco de dados e acesso administrativo.

Este projeto é ideal para fins **acadêmicos**, **aprendizado de Django** e também para **portfólio inicial**.

---

## 🚀 Funcionalidades

* Cadastro de usuários (nome, email e senha)
* Interface web simples e responsiva
* Persistência de dados com SQLite
* Listagem de usuários cadastrados
* Acesso administrativo via Django Admin

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.12**
* **Django 5.x**
* **SQLite** (banco de dados padrão)
* **HTML5 & CSS3**

---

## 📁 Estrutura do Projeto

```
cadUser/
├── venv/
├── sistema_usuarios/
│   ├── manage.py
│   ├── sistema_usuarios/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── ...
│   └── usuarios/
│       ├── models.py
│       ├── views.py
│       ├── forms.py
│       ├── urls.py
│       ├── admin.py
│       └── templates/
│           └── usuarios/
│               ├── cadastro.html
│               └── listar.html
└── README.md
```

---

## ⚙️ Como Executar o Projeto

### 1️⃣ Clonar o repositório

```bash
git clone <url-do-repositorio>
cd cadUser
```

---

### 2️⃣ Criar e ativar o ambiente virtual

```bash
python -m venv venv
```

**Ativar:**

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

---

### 3️⃣ Instalar as dependências

```bash
pip install django
```

---

### 4️⃣ Aplicar as migrações

```bash
cd sistema_usuarios
python manage.py makemigrations
python manage.py migrate
```

---

### 5️⃣ Criar superusuário (opcional)

```bash
python manage.py createsuperuser
```

---

### 6️⃣ Rodar o servidor

```bash
python manage.py runserver
```

Acesse no navegador:

* Cadastro: `http://127.0.0.1:8000/cadastro/`
* Listagem: `http://127.0.0.1:8000/usuarios/`
* Admin: `http://127.0.0.1:8000/admin/`

---

## 🧩 Model de Usuário

```python
class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)
    criado_em = models.DateTimeField(auto_now_add=True)
```

---

## 🎨 Interface

* Layout moderno e simples
* Design focado em clareza e usabilidade
* Estilização feita com CSS puro

---

## 🔒 Observações Importantes

* Este projeto **não utiliza autenticação nativa do Django**
* As senhas **não estão criptografadas** (projeto educacional)
* Para produção, recomenda-se:

  * Usar `django.contrib.auth.User`
  * Criptografar senhas
  * Configurar variáveis de ambiente

---

## 📌 Possíveis Melhorias Futuras

* Autenticação e login
* Criptografia de senha
* Edição e exclusão de usuários (CRUD completo)
* Validações avançadas
* Estilização com Bootstrap ou Tailwind
* Deploy em servidor (Railway, Render, etc.)

---

## 👨‍💻 Autor

**Brenno**
Estudante de Análise e Desenvolvimento de Sistemas
Focado em Back-end, Django e Java

---

## 📄 Licença

Este projeto é de uso livre para fins educacionais.
