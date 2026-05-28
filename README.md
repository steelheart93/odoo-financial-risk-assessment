# 📌 Proyecto Prueba Técnica – Odoo + Python

**Desarrollador:** Stiven Muñoz Murillo  
**Empresa:** Borner  
**Versión:** Odoo 18+ Community  

---

## 🧩 Bloque 1 – Módulo Odoo `borner_riesgos`

Módulo que permite registrar operaciones financieras y evaluar su riesgo mediante un botón que asigna un valor aleatorio entre 0 y 100.

### ▶️ Ejecutar Odoo con el módulo

Asegúrate de que la carpeta del módulo esté dentro de `addons` o `custom_addons`.

```bash
python odoo-bin -r odoo -w odoo -d odoo --addons-path=addons,custom_addons
```

> Luego, desde **Aplicaciones → Actualizar lista** e instalar **"Riesgos Financieros"**.

---

## ⚙️ Bloque 2 – Automatización / API Externa

Script que simula una consulta a una API para clasificar un gasto en base a su concepto, país y monto.

### ▶️ Ejecutar script

```bash
python clasificar_gasto.py
```

---

## 🗄️ Bloque 3 – SQL / Auditoría

El archivo **`auditar_riesgo.sql`** contiene:

- Eliminación y creación de la tabla `actions_log`
- Relaciones con el modelo de riesgos (`borner_riesgo`)
- Ejemplos de inserción
- Consulta agrupada de acciones realizadas en el día

> Permite auditar las operaciones ejecutadas sobre los riesgos.

---

## 📄 Bloque 4 – Respuestas Teóricas

Las respuestas a las preguntas teóricas se encuentran en:

➡️ `respuestas_teoricas_borner.pdf`

Documento listo para entrega.

---

## ✅ Estado Final

| Bloque | Entregado | Archivos |
|--------|:--------:|----------|
| Bloque 1 – Módulo Odoo | ✅ | `borner_riesgos/` |
| Bloque 2 – Automatización Python | ✅ | `clasificar_gasto.py` |
| Bloque 3 – SQL Auditoría | ✅ | `auditar_riesgo.sql` |
| Bloque 4 – Respuestas Teóricas | ✅ | `respuestas_teoricas_borner.pdf` |
