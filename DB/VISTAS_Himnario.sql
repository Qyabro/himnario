USE himnario;

-- =============  AUTORES ==============
-- Crear Vista:
CREATE OR REPLACE VIEW lista_autores AS
SELECT * FROM autores ORDER BY nombre;
-- Autores disponibles:
SELECT * FROM lista_autores;
SELECT * FROM lista_autores LIMIT 4 OFFSET 8;
-- Insertar Autores:
INSERT INTO lista_autores (nombre)
VALUES ('Andres Calamaro');
-- Eliminar Autores:
DELETE FROM lista_autores WHERE nombre='Andres Calamaro';
-- Editar Autores:
UPDATE lista_autores SET nombre = 'Andres Calamardo'
WHERE nombre = 'Andres Calamaro';

-- =============  CATEGORIAS  ==============
-- Crear Vista:
CREATE OR REPLACE VIEW lista_categorias AS
SELECT * FROM categorias ORDER BY categoria;
-- Consultar:
SELECT * FROM lista_categorias;
SELECT * FROM lista_categorias WHERE id_categoria=2;
SELECT * FROM lista_categorias WHERE categoria='cena';
-- Insertar:
INSERT INTO lista_categorias (categoria)
VALUES ('Amor');
-- Eliminar:
DELETE FROM lista_categorias WHERE categoria='Amor';
DELETE FROM lista_categorias WHERE id_categoria=2;
-- Editar:
UPDATE lista_categorias SET nombre = 'Andres Calamardo'
WHERE nombre = 'Andres Calamaro';

-- =============  PAGINAS  ==============
-- Crear Vista:
CREATE OR REPLACE VIEW lista_paginas AS
SELECT * FROM paginas ORDER BY num_pagina;
-- Consultar:
SELECT * FROM lista_paginas;
-- Insertar:
INSERT INTO lista_paginas (num_pagina)
VALUES (10);
-- Eliminar:
DELETE FROM lista_paginas WHERE num_pagina=10;
-- Editar:
UPDATE lista_paginas SET num_pagina = 78
WHERE num_pagina = 10;

-- =============  HIMNOS  ==============

-- Vista Basic Himnos:
CREATE OR REPLACE VIEW lista_himnos_basica AS
SELECT * FROM himnos;


-- Crear Vista General:
CREATE OR REPLACE VIEW lista_himnos_general AS
SELECT himnos.id_himno,himnos.num_himno AS num, himnos.titulo, categorias.categoria, autores.nombre AS autores, paginas.num_pagina AS pag
FROM himnos
INNER JOIN paginas
ON himnos.fk_pagina = paginas.id_pagina
INNER JOIN categorias
ON himnos.fk_categoria = categorias.id_categoria
LEFT JOIN himnos_autores
ON himnos.id_himno = himnos_autores.fk_himno
LEFT JOIN autores
ON himnos_autores.fk_autor = autores.id_autor
ORDER BY titulo;

-- Crear Vista Himnos SIN Autores:
CREATE OR REPLACE VIEW lista_himnos_sin_autores AS
SELECT *
FROM himnos
INNER JOIN paginas
ON himnos.fk_pagina = paginas.id_pagina
INNER JOIN categorias
ON himnos.fk_categoria = categorias.id_categoria
ORDER BY titulo;

-- Crear Vista Pantalla Inicio:
CREATE OR REPLACE VIEW lista_himnos AS
SELECT himnos.id_himno,himnos.num_himno AS num, himnos.titulo, categorias.categoria, autores.nombre AS autores, paginas.num_pagina AS pag
FROM himnos
INNER JOIN paginas
ON himnos.fk_pagina = paginas.id_pagina
INNER JOIN categorias
ON himnos.fk_categoria = categorias.id_categoria
INNER JOIN himnos_autores
ON himnos.id_himno = himnos_autores.fk_himno
INNER JOIN autores
ON himnos_autores.fk_autor = autores.id_autor
ORDER BY titulo;

-- Consultar:
SELECT * FROM lista_himnos_basica;
SELECT * FROM lista_himnos_general;
SELECT * FROM lista_himnos_sin_autores;
SELECT id_himno,num_himno,titulo,categoria,fecha,num_pagina FROM lista_himnos_sin_autores;
SELECT * FROM lista_himnos;	-- Ordenado por titulo
SELECT * FROM lista_himnos LIMIT 4;
SELECT * FROM lista_himnos LIMIT 4 OFFSET 4;
SELECT * FROM lista_himnos ORDER BY num;
SELECT * FROM lista_himnos ORDER BY categoria;
SELECT * FROM lista_himnos ORDER BY autores;
SELECT * FROM lista_himnos ORDER BY pag;

-- Insertar Himnos SIN autores:
INSERT INTO lista_himnos_general (num_himno,titulo,letra,fk_pagina,fk_categoria,fecha) 
VALUES (527,"Recordad al Señor", 
"Recordad al Seor, bendecid
su santo nombre; celebremos su gloria
y amor. Fue levantado en la cruz,
di su vida por nosotros;
Recordemos al Salvador Jesus.",
(SELECT id_pagina FROM lista_paginas WHERE num_pagina=78),
(SELECT id_categoria FROM lista_categorias WHERE categoria='Cena'),'1800-01-01'
);


-- Asignar Autor a Himno (no se puede repetir Autor):
INSERT INTO lista_himnos_general (fk_himno,fk_autor) 
VALUES (
(SELECT id_himno FROM lista_himnos_sin_autores WHERE titulo='Recordad al Señor'),
(SELECT id_autor FROM lista_autores WHERE nombre='Pablo Mejia')
);

-- Eliminar:
DELETE FROM lista_himnos_basica WHERE titulo='BUENO ES ALABARTE, OH JEHOVÁ';
-- Editar:
UPDATE lista_paginas SET num_pagina = 78
WHERE num_pagina = 10;


SELECT version();
