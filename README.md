# NetSnake 🐍

**NetSnake** é uma ferramenta de automação de rede multivendor desenvolvida em Python. Ela simplifica a execução de comandos em múltiplos dispositivos de rede simultaneamente através do protocolo SSH, permitindo uma gestão ágil e eficiente de infraestruturas de rede.

---

## 🚀 Funcionalidades

- **Automação Multivendor:** Execute comandos em dispositivos de diferentes fabricantes (Huawei, Mikrotik, Juniper, etc).
- **Gestão de Inventário:** Organize seus dispositivos em arquivos de hosts simples.
- **Templates de Configuração:** Crie e reutilize scripts de configuração facilmente.
- **Interface Intuitiva:** Menu interativo via terminal para facilitar a operação.
- **Segurança:** Utiliza variáveis de ambiente (`.env`) para gerenciar credenciais de acesso.

---

## 📂 Estrutura do Projeto

O projeto utiliza duas pastas principais para organizar a automação:

- **`/hosts`**: Armazena arquivos `.txt` contendo a lista de IPs dos equipamentos.
- **`/configs`**: Armazena arquivos `.txt` com as sequências de comandos a serem enviadas.

---

## ⚙️ Pré-requisitos

Antes de começar, você precisará ter o Python instalado em sua máquina.

1. Instale as dependências necessárias:
   ```bash
   pip install -r requeriments.txt
   ```

2. Configure suas credenciais no arquivo `.env` na raiz do projeto (crie um se não existir):
   ```env
   USER=seu_usuario
   PASS=sua_senha
   ```

---

## 🛠️ Como Usar

### 1. Criar Arquivos de Hosts
Você pode criar um arquivo manualmente na pasta `/hosts` ou usar a opção **[3] - Criar Arquivo de Host** no menu principal. O formato deve ser um IP por linha:
```text
192.168.1.1
192.168.10.1
10.10.0.56
```

### 2. Criar Arquivos de Configuração
Crie um arquivo na pasta `/configs` ou use a opção **[2] - Criar Arquivo de Configuração**.
*Exemplo (Configuração SNMP em Huawei):*
```text
snmp-agent
snmp-agent community read senhaforte
snmp-agent sys-info version v2c
snmp-agent mib-view included ViewAll iso
return
save
```

### 3. Executar a Automação
1. Execute o script principal: `python app.py`.
2. No menu principal, selecione **[1] - Automações**.
3. Selecione o arquivo de **Host** desejado (Opção [1] no menu de automação).
4. Selecione o arquivo de **Configuração** desejado (Opção [2] no menu de automação).
5. Selecione a opção **[3] - Executar Automação** para iniciar o processo.

---

## 📝 Observações

- **Importante:** Certifique-se de que os dispositivos de rede estão acessíveis via SSH a partir da máquina que executa o script.
- O script utiliza o Bloco de Notas (Windows) ou Nano (Linux/Mac) para edição rápida dos arquivos quando criados via menu.
- Verifique se o arquivo `.env` contém as credenciais corretas antes de iniciar.

---

## 🤝 Contribuição

Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias!

---
*Desenvolvido para facilitar a vida do administrador de redes.*
