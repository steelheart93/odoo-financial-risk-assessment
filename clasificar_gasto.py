import requests
import random

def clasificar_gasto(data: dict) -> dict:
    """
    data = {
        "concepto": "compra equipo",
        "monto": 15000,
        "pais": "CL"
    }
    """

    # 1) Intentar obtener un dato desde API externa
    try:
        resp = requests.get("https://dummyjson.com/products", timeout=5)
        resp.raise_for_status()
        # Tomamos el nombre del primer producto como referencia simple
        producto = resp.json()['products'][0]['title']
    except Exception:
        producto = "No disponible"

    # 2) Evaluación de riesgo básica
    riesgo = random.randint(0, 100)

    if riesgo > 70:
        motivo = "importe inusual para categoría"
        accion = "revisar"
    else:
        motivo = "gasto dentro de rango normal"
        accion = "continuar"

    # 3) Retornar el resultado estructurado
    return {
        "riesgo": riesgo,
        "motivo": motivo,
        "accion_sugerida": accion,
        "detalle_api": producto,
    }


# --- Ejecución de prueba ---
if __name__ == "__main__":
    entrada = {"concepto": "compra equipo", "monto": 15000, "pais": "CL"}
    resultado = clasificar_gasto(entrada)
    print(resultado)
