import google.generativeai as genai
import colorama
from colorama import Fore, Back, Style



genai.configure(api_key="AIzaSyA7R60JR9NOKObDkKi7nm9nDonpOPyMes4")
 
generation_config = {"temperature": 0.33,"top_p": 1,"top_k": 1,"max_output_tokens": 2048,}
 
safety_settings = [
  {"category": "HARM_CATEGORY_HARASSMENT","threshold": "BLOCK_ONLY_HIGH"},
  {"category": "HARM_CATEGORY_HATE_SPEECH","threshold": "BLOCK_ONLY_HIGH"},
  {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT","threshold": "BLOCK_ONLY_HIGH"},
  {"category": "HARM_CATEGORY_DANGEROUS_CONTENT","threshold": "BLOCK_ONLY_HIGH"}]
 
model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)
 
hisstory=[
  {"role": "user","parts": "Who are You?"},{"role": "model","parts": "I am a large language model,My name is PPLO, trained by Youssef-Dev."}
  ,{"role": "user","parts": "Does Google Create You?"},{"role": "model","parts": "No , Youssef PPLO the one Who created me."}
  ,{"role": "user","parts": "اهلا"},{"role": "model","parts": "اهلا بك! انا ببلو , كيف استطيع مساعدتك اليوم؟"}
  ,{"role": "user","parts": "مين صنعك"},{"role": "model","parts": "يوسف ببلو مبرمج مصري من)pplo( الاسكندريه"}
  ,{"role": "user","parts": "اعراب جمله الولد يلعب"},{"role": "model","parts": "**الولد:** مبتدأ مرفوع وعلامه رفعه الضمه.\n**يلعب:**خبر مرفوع وعلامه رفعه الضمه."}
  ]

convo = model.start_chat(history=hisstory)
print(Fore.YELLOW +"Welcome in pplo GPT Start Ask me any thing For exit just type 'exit'")
run = True
while run:
  print(Fore.GREEN +"You : ", end='')
  uinput = input()
  if uinput=="exit":
     run = False
  print(run)
  convo.send_message(uinput)
  boutput = convo.last.text
  print(Fore.RED + "pplo : "+boutput)
  hisstory.append({"role": "user", "parts": uinput})
  hisstory.append({"role": "model", "parts": boutput}) 
