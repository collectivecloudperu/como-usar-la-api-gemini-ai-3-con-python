from google import genai

cliente = genai.Client(api_key="API KEY")

model_id = "gemini-3-flash-preview"

reponse = cliente.models.generate_content(
    model = model_id,
    contents = "¿Donde esta Egipto?"
)

print(f"Respuesta de {model_id}")
print(reponse.text)
