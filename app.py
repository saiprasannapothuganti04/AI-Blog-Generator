from google import genai
import gradio as gr

client=genai.Client(api_key="Gemini_API")

def generate_blog(topic,audience,tone,words):
  prompt=f"""

  write a {words}-word blog
  Topic:{topic}
  Audience:{audience}
  Tone:{tone}

  Include:
  -Introduction
  -abstract
  -workflow
  -applications
  -advantages
  -conculsion
  """
  response=client.models.generate_content(
      model="gemini-2.5-flash",
      contents=prompt
  )
  return response.text
demo=gr.Interface(
      fn=generate_blog,
      inputs=[
          gr.Textbox(label="Topic"),
          gr.Textbox(label="Audience"),
          gr.Dropdown(
          ["professional","casual","funny","technical","Inspirational"],
          label="Tone"
          ),
          gr.Slider(200,1000,value=500,label="word count")

      ],
      outputs="markdown",
      title="AI Blog Generater (gemini)"
   )
demo.launch()
