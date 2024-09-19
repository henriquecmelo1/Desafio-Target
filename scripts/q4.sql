-- 4) Banco de dados

-- Uma empresa solicitou a você um aplicativo para manutenção de um cadastro de clientes. Após a reunião de definição dos requisitos, as conclusões foram as seguintes:

-- - Um cliente pode ter um número ilimitado de telefones;
-- - Cada telefone de cliente tem um tipo, por exemplo: comercial, residencial, celular, etc. O sistema deve permitir cadastrar novos tipos de telefone;
-- - A princípio, é necessário saber apenas em qual estado brasileiro cada cliente se encontra. O sistema deve permitir cadastrar novos estados;

-- Você ficou responsável pela parte da estrutura de banco de dados que será usada pelo aplicativo. Assim sendo:

-- - Proponha um modelo lógico para o banco de dados que vai atender a aplicação. Desenhe as tabelas necessárias, os campos de cada uma e marque com setas os relacionamentos existentes entre as tabelas;
-- - Aponte os campos que são chave primária (PK) e chave estrangeira (FK);
-- - Faça uma busca utilizando comando SQL que traga o código, a razão social e o(s) telefone(s) de todos os clientes do estado de São Paulo (código “SP”);

-- Resposta:

CREATE TABLE Estados (
    sigla CHAR(2) PRIMARY KEY
    nome VARCHAR(50) NOT NULL,
);

CREATE TABLE TiposTelefone (
    codigo INT PRIMARY KEY
    descricao VARCHAR(50) NOT NULL,
);

CREATE TABLE Clientes (
    codigo INT PRIMARY KEY,
    razao_social VARCHAR(100) NOT NULL,
    estado CHAR(2) NOT NULL,

    FOREIGN KEY (estado) REFERENCES Estados(sigla)
);

CREATE TABLE Telefones (
    numero VARCHAR(20) NOT NULL,
    cliente INT NOT NULL,
    tipo INT NOT NULL,

    FOREIGN KEY (cliente) REFERENCES Clientes(codigo),
    FOREIGN KEY (tipo) REFERENCES TiposTelefone(codigo)
);


SELECT C.codigo, C.razao_social, T.numero FROM Clientes C JOIN Telefones T ON C.Codigo = T.cliente WHERE C.estado = 'SP';