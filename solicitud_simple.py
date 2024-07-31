import openai
import config

openai.api_key = config.api_key

try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "Eres un asistente muy útil."},
                  {"role": "user", "content": "Escribe un breve ensayo sobre la importancia de la inteligencia artificial en la educación"}]
    )
    print(response.choices[0].message.content)
except openai.error.RateLimitError:
    print("Has excedido tu cuota de uso. Por favor, revisa tu plan y los detalles de facturación.")
except openai.error.InvalidRequestError as e:
    print(f"Error en la solicitud: {e}")
except openai.error.AuthenticationError as e:
    print(f"Error de autenticación: {e}")
except openai.error.APIError as e:
    print(f"Error de la API: {e}")
except Exception as e:
    print(f"Se produjo un error: {e}")
