-- Eliminar la tabla si ya existe (permite re-ejecutar sin error)
DROP TABLE IF EXISTS actions_log;

-- Crear tabla de auditoría
CREATE TABLE actions_log (
    id SERIAL PRIMARY KEY,
    riesgo_id INTEGER,
    accion VARCHAR(50) NOT NULL,
    resultado TEXT,
    fecha TIMESTAMP DEFAULT NOW()
);

-- Ejemplos de inserción (para demostración)
INSERT INTO actions_log (riesgo_id, accion, resultado)
VALUES 
    (1, 'evaluar_riesgo', 'riesgo asignado correctamente'),
    (1, 'aprobar', 'registro aprobado'),
    (2, 'evaluar_riesgo', 'riesgo elevado, requiere revisión');

-- Consulta: cuántas acciones por tipo se han ejecutado HOY
SELECT accion, COUNT(*) AS cantidad
FROM actions_log
WHERE fecha::date = CURRENT_DATE
GROUP BY accion
ORDER BY cantidad DESC;
