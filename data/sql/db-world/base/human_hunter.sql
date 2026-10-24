-- ===========================================================
-- Parche Base acore_world: Human Hunter (Raza 1 / Clase 3)
-- ===========================================================

-- 1. Posición e información de inicio (Elwynn Forest / Bosque de Elwynn)
DELETE FROM `playercreateinfo` WHERE `race` = 1 AND `class` = 3;
INSERT INTO `playercreateinfo` (`race`, `class`, `map`, `zone`, `position_x`, `position_y`, `position_z`, `orientation`)
SELECT 1, 3, `map`, `zone`, `position_x`, `position_y`, `position_z`, `orientation`
FROM `playercreateinfo` WHERE `race` = 1 AND `class` = 1 LIMIT 1;

-- 2. Barras de acción iniciales (Copiadas de Cazador Elfo de la Noche, raza 4 clase 3)
DELETE FROM `playercreateinfo_action` WHERE `race` = 1 AND `class` = 3;
INSERT INTO `playercreateinfo_action` (`race`, `class`, `button`, `action`, `type`)
SELECT 1, 3, `button`, `action`, `type`
FROM `playercreateinfo_action`
WHERE `race` = 4 AND `class` = 3;

-- 3. Competencias de armas y habilidades de Cazador directas para Humano (raceMask = 1, classMask = 4)
-- Inserta explícitamente arcos, espadas de 2 manos, armas de fuego, dagas, etc., sin depender de registros previos.
DELETE FROM `playercreateinfo_skills` WHERE `raceMask` = 1 AND `classMask` = 4;
INSERT INTO `playercreateinfo_skills` (`raceMask`, `classMask`, `skill`, `rank`, `comment`) VALUES
(1, 4, 45, 0, 'Human Hunter - Bows'),
(1, 4, 46, 0, 'Human Hunter - Guns'),
(1, 4, 226, 0, 'Human Hunter - Crossbows'),
(1, 4, 43, 0, 'Human Hunter - Swords'),
(1, 4, 55, 0, 'Human Hunter - Two-Handed Swords'),
(1, 4, 44, 0, 'Human Hunter - Axes'),
(1, 4, 172, 0, 'Human Hunter - Two-Handed Axes'),
(1, 4, 173, 0, 'Human Hunter - Daggers'),
(1, 4, 229, 0, 'Human Hunter - Polearms'),
(1, 4, 136, 0, 'Human Hunter - Staves');