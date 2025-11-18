-- Utilizando o VScode apenas para salvar os códigos 

-- Criando tabelas
create table cliente(
	idCliente integer not null, -- todo cliente tem um id.
	nome varchar(50) not null, 
	data_nascimento date not null, -- valores corresponde a data é no formato americano -> aaaa-mm-dd
	genero char(1),
	observacoes text, -- Campo livre para textos.

	-- chave primária
	constraint pk_cln_idCliente primary key (idCliente)
);

-- aula 2 -- CRUD

-- Adicionando itens na tabela

select * from cliente; -- O asterisco é igual a tudo, e o from é a referência para a tabela. "tudo de cliente"

insert into cliente(idCliente, nome, data_nascimento, genero, observacoes)
		values(1, 'Emerson', '2001-06-11', 'M', 'Tem as manhas para o show do safadão') -- inserir em cliente() inserir valores()

insert into cliente(idCliente, nome, data_nascimento, genero, observacoes)
		values(2, 'Brad' , '1970-03-17', 'M', 'Qual a primeira regra do clube?')

insert into cliente(idCliente, nome, data_nascimento, genero) -- sem observacoes
		values(3, 'Maria', '1999-06-02', 'M') -- vai mostrar obs null na tabela

insert into cliente(idCliente, nome, data_nascimento, genero, observacoes)
		values(4, 'Joicy', '2000-08-09', 'F', 'Gosta do Justhen')

insert into cliente(idCliente, nome, data_nascimento, genero, observacoes) -- deixando observacoes
		values(5, 'Florentina', '1978-10-10', 'F', '') -- porém, em baixo obs está vazia, assim dificultando na planilha 

-- Aula 3 - Consultando itens em uma tabela 

select nome from cliente; -- para mostrar apenas o nome 

select nome, data_nascimento, idCliente from cliente; -- podemos selecionar os itens que queremos ver 

select idCliente, genero, nome from cliente; -- os itens iram aparecer com a forma que chamamos a tabela

select * from cliente limit 3; -- mostra apenas as 3 primeiras linhas da tabela 

select nome from cliente where nome like 'J%'; -- classificação ou clausula - No caso estamos filtrando os nomes com a letra J

select nome from cliente where nome like '%n'; -- chamando pela letra final do nome 

select nome from cliente where nome like '%e%'; -- chamando pela letra no meio do nome 

select * from cliente order by nome asc; -- Mostra a tabela com a ordem alfabética na coluna nome. (asc) não precisa ser implicito já bem na base

select * from cliente order by nome desc; -- Mostra a tabela com a ordem descendente - Precisa ser declarado 

select nome, data_nascimento from cliente where data_nascimento between '1960-01-01' and '2000-01-01'; -- between (entre) - seleciando os dados entre data

-- Aula 04 - Atualizações na tabela 

update cliente set nome = 'Emerson Cristo' where idCliente = 1; -- alterando o dado nome cliente com id igual a 1 

update cliente set nome = 'JhonyJhony', data_nascimento = '1992-11-11', observacoes = 'Gosta de panelada' where idCliente = 3;

update cliente set idCliente = 11 where idCliente = 10; -- alterando o id do cliente 

-- Aula 5 - Removendo elementos da tabela 

delete from cliente where idCliente = 5;
