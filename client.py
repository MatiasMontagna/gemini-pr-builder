from google import genai
import os

GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]

class Client:
  def __init__(self):
    self.client = genai.Client(api_key=GEMINI_API_KEY)

  def _prompt(self, template, commits, user_context=None):
    if template:
      return self._prompt_with_template(template, commits, user_context)
    else:
      return self._prompt_without_template(commits, user_context)
    
  def _prompt_with_template(self, template, commits, user_context=None):
    context_str = f"\n\nContexto adicional proporcionado por el usuario:\n{user_context}" if user_context else ""
    return f"""
Aquí tienes una plantilla de pull request de GitHub. Viene con un --- al principio y al final. Ignora esos caracteres en el output.

---
{template}
---

Y estos son los commits que se van a incluir en el pull request:

{commits}{context_str}

Devuélveme la plantilla, pero con una lista en markdown (en español) que describa brevemente cada commit, insertada en el lugar adecuado de la plantilla (por ejemplo, en la sección de descripción o donde corresponda). No añadas ningún texto adicional fuera de la plantilla. Si hay checkboxes, chequealos todos.
"""
  
  def _prompt_without_template(self, commits, user_context=None):
    context_str = f"\n\nContexto adicional proporcionado por el usuario:\n{user_context}" if user_context else ""
    return f"""
Resume estos commits de git para la descripción de un pull request:
{commits}{context_str}

Hazlo en español, en una lista markdown. No incluyas ningún texto adicional. No uses backticks triple y --- .
"""

  def build_pr_body(self, template, commits, user_context=None):
    response = self.client.models.generate_content(
      model="gemini-2.0-flash",
      contents=self._prompt(template, commits, user_context)
      )
    return response.text.replace("```", "")

