# Trabalho 02 - IFTO - Campus Palmas - Extensão Noturno

## 🚀 Instalação

Essas instruções permitirão que você execute a aplicação no seu computador.

### 📋 Pré-requisitos

os sequintes softwares devem estar instalados na sua máquina:

* **Python** - *3.13.0* - [Acessar](https://www.python.org/downloads/)
* **Django** - *5.1.2* - [Acessar](https://docs.djangoproject.com/en/5.1/topics/install/#installing-official-release)
* **PIP** - *1.3* - [Acessar](https://pypi.org/project/pip/)

## 📦 Implantação

Primeiramente deve ser instalado o módulo mysql correspondente

```
> pip install pymysql
```

Para inicar o tratamento de dados básicos do DB, deve ser gerado as migrations criadas no módulo mysite

```
> python manage.py migrate mysite
```

Após isso, as migrations devem ser executadas (lembrando que o banco de dados deve estar instalado e sendo executado conforme configuraçõs do arquivo settings.py do módulo mysite)

```
> python manage.py migrate
```

Com isso todas as tabelas devem ser devidamente criadas no banco de dados fornecido ao projeto, logo após a aplicação deve ser executada na porta 8000 com o seguinte comando

```
> py manage.py runserver
```

Para instalar o módulo responsável por request a API externas

```
> pip install requests
```

Para instalar o módulo responsável por variaveis de ambiente

```
> pip install python-decouple
```

Para instalar o módulo responsável por gerar arquivo word

```
> pip install python-docx
```

## ✒️ Autores

4° período do curso noturno de sistemas para internet do Instituto Federal de Educação, Ciências e Tecnoclogia do Tocantins - *Campus Palmas*

* **Arthur Machado Guimarães Sampaio Perna** - *Desenvolvedor* - [Acessar Github](https://github.com/arthurmachado011)
* **Caio Alexandre de Sousa Ramos** - *Desenvolvedor* - [Acessar Github](https://github.com/caioalexandredev)
* **Daniel** - *Desenvolvedor*
* **Fernando Martins** - *Desenvolvedor*