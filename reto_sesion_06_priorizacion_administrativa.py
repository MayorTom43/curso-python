#datos de entrada: DICCIONARIO
solicitud = {
    "codigo": "ADM-004",
    "tipo": "actualizacion de datos",
    "area_solicitante": "talento humano",
    "dias_pendiente": 4,
    "afecta_operacion": False, 
    "estado": "PENDIENTE" 
}
# CONSULTAR LOS DATOS QUE SE VAN A EVALUAR
estado = solicitud["estado"]
dias_pend = solicitud["dias_pendiente"]
afecta_op = solicitud["afecta_operacion"]

# CONSTRUCCION DE LAS CONDICIONALES
if estado == "CERRADA":
    clasificacion = "CERRADA"
    accion = "REGISTRAR QUE NO REQUIERE NUEVA GESTIÓN"
elif afecta_op == True and dias_pend >= 2:
    clasificacion = "URGENTE"
    accion = "ESCALAR AL RESPONSABLE PARA ATENCIÓN PRIORITARIA"
elif afecta_op == True or dias_pend >= 5:
    clasificacion = "PRIORITARIA"
    accion = "PROGRAMA ATENCIÓN PREFERENTE"
else:
    clasificacion = "NORMAL" 
    accion = "MANTENER EN EL FLUJO HABITUAL DE ATENCIÓN"

# RESUMEN DE SALIDA
print(" ---- RESUMEN DE SOLICITUD ----")
print(
    f"Código: {solicitud["codigo"]}"
    f"\nTipo: {solicitud["tipo"]}"
    f"\nClasificación: {clasificacion}"
    f"\nAcción recomendada: {accion}"
)

# ¿Por qué la solicitud cerrada debe evaluarse antes que las demás condiciones?
# EVALUARLO PRIMERO EVITA QUE LA SOLICITUD FINALIZADA APAREZCA EN OTRA CLASIFICACION NO CORRESPONDIENTE

# ¿Qué diferencia hay entre utilizar and y utilizar or en las reglas de prioridad?
# AND las dos condiciones debe ser verdadera para cumplir la regla. 
# OR una de las dos condiciones es verdadera

# ¿Qué podría ocurrir si cambiamos el orden de las condiciones?
# LA SOLICITUD SE CLASIFICARIA DE FORMA ERRONEA.
