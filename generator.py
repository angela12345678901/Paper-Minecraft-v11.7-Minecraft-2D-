def anti_loop_generator():
    assistant_history = set()
    repeat_count = 0
    
    while True:
        # Recibe los datos del chat en cada iteración
        user_message, assistant_response = yield
        
        # Normaliza el texto eliminando espacios y saltos de línea extra
        cleaned_user = " ".join(user_message.strip().split())
        cleaned_assistant = " ".join(assistant_response.strip().split())
        
        if cleaned_user in assistant_history:
            repeat_count += 1
            if repeat_count >= 3:
                # Envía la alerta al sistema si se alcanza el límite
                yield "ALERTA: Bucle detectado. Bloqueando repeticiones."
                break
        else:
            # Resetea el contador si el usuario introduce un texto nuevo
            repeat_count = 0
            
        assistant_history.add(cleaned_assistant)
        # Devuelve la respuesta normal si todo está en orden
        yield "Mensaje procesado correctamente."
# 1. Inicializa el generador
bot_checker = anti_loop_generator()
next(bot_checker)  # Avanza hasta el primer yield

# 2. Simula el flujo del chat
# Entrada: (Mensaje_Usuario, Respuesta_Asistente)
print(bot_checker.send(("Hola", "¡Hola! ¿En qué te ayudo?"))) 
next(bot_checker)

# El usuario empieza a copiar y pegar la respuesta del asistente
print(bot_checker.send(("¡Hola! ¿En qué te ayudo?", "Elige un tema."))) 
next(bot_checker)

print(bot_checker.send(("¡Hola! ¿En qué te ayudo?", "Por favor, elige un tema."))) 
next(bot_checker)

# Tercera repetición: El generador activa la alerta y se detiene
alerta = bot_checker.send(("¡Hola! ¿En qué te ayudo?", "Por favor, elige un tema."))
print(alerta)
