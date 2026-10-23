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