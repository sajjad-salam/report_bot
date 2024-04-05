import os
import telebot
from fpdf import FPDF
from io import BytesIO
from transformers import pipeline, set_seed
import re
import threading

print("\033[97;1m[\033[92;1m+\033[97;1m] \x1b[1;38;5;121mJOIN MY TELEGRAM CHANNEL")
import os
import requests
import time
Z = '\033[1;31m' #احمر
R = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
#-------------------#
Z = '\033[1;31m' 
X = '\033[1;33m' 
F = '\033[2;32m' 
C = "\033[1;97m" 
B = '\033[2;36m'
Y = '\033[1;34m' 
C = "\033[1;97m" 
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33'
#-----------------------------------------------------#
bRIMON="\033[1;30m" 
M="\033[1;31m"       
H="\033[1;33m"               
byellow="\033[1;33m"     
bblue="\033[1;34m"        
P="\033[1;35m"               
C="\033[1;36m"          
B="\033[1;37m"       
G="\033[1;32m"              
R="\033[1;31m"
AA="\033[1;32m"
BB="\033[1;31m"
CC="\033[1;36m"
X='\033[1;30m'
XX="\x1b[38;5;196m"
GGG="\x1b[38;5;214m"
#vers = requests.get('').text
#version = str(vers)
#-----------------------------------------------------#
#-------------------#
print(f"""\x1b[1;38;5;121m
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⢀⠀⠀⠀⣰⡇⢀⡄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡄⠀⣿⣰⡀⢠⣿⣇⣾⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣰⣿⣿⢇⣾⣿⣼⣿⢃⡞⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⢋⣾⣿⣿⣿⣯⣿⠇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⢟⣵⣿⣿⣿⣿⣿⣿⣯⡞⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣵⣿⣿⣿⣿⣿⣿⣿⣿⡿⡁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣦⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡡⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀
⠀⠀⢀⣀⣄⣀⡀⡀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡥⠀⠀⠀⠀⠀⠀
⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀
⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀
⠘⣿⠋⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀ENG-SAJJAD
⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣀⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡛⠃⠀⠀
⠀⠀⠀⠀⠀⠀⢈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀
⠀⠀⠀⠀⠀⢰⣾⣿⣿⣿⣿⣿⠟⠁⠉⠙⠻⠯⡛⠿⠛⠻⠿⠟⠛⠓⠀⠀
⠀⠜⡿⠳⡶⠻⣿⣿⣿⣿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣠⣽⣧⣾⠛⠉⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠉⠟⠁⠘⠃
  
{G}⋆{GGG}\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{G}⋆
\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m AUTHOR    \x1b[1;97m ● \x1b[1;92m ENG.SAJJAD
\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}] \x1b[38;5;47mUESER  \x1b[1;97m    ● \x1b[1;92m@S_J_O_D
\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;48m INFO   \x1b[1;97m    ● \x1b[1;92m BOT_REPORT_AI
\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}] \x1b[38;5;47mTOOLS     \x1b[1;97m ● \x1b[1;92mNO
\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}] \x1b[38;5;47mVERSION   \x1b[1;97m ● \x1b[1;92mV.1                 
{G}⋆{GGG}\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{G}⋆""")
import os
Z = '\033[1;31m' #احمر
R = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
try:
	import requests
except ImportError:
    Z = '''[1;31m'''
R = '''[1;31m'''
X = '''[1;33m'''
F = '''[2;32m'''
C = '''[1;97m'''
B = '''[2;36m'''
Y = '''[1;34m'''
E = '''[1;31m'''
B = '''[2;36m'''
G = '''[1;32m'''
S = '''[1;33m'''
ses = requests.Session()
F = '''[2;32m'''
Z = '''[1;31m'''
L = '''[1;95m'''
E = '''[1;31m'''
G = '''[1;32m'''
S = '''[1;33m'''
Z = '''[1;31m'''
X = '''[1;33m'''
Z1 = '''[2;31m'''
F = '''[2;32m'''
A = '''[2;39m'''
C = '''[2;35m'''
B = '''[2;36m'''
Y = '''[1;34m'''
xxh = '\x1b[38;5;208m'#برتقالي
r1='\x1b[38;5;8m'#رمادي
e1='\x1b[38;5;196m'#احمر
w1='\x1b[38;5;225m'#وردي فاتح جدا
t1='\x1b[38;5;92m'#بنفسجي غامق
y1='\x1b[1;93m'#اصفر نيون
u1='\x1b[1;38;5;203m'#وردي لطيف
i1='\x1b[1;38;5;121m'#اخضر نيون
o1='\x1b[1;96m'#ازرق سماوي
p1='\x1b[38;5;205m'#وردي فاتح
a1='\x1b[38;5;161m'#وردي جميل جدا
S0='\x1b[1;93m'  
S9='\x1b[1;38;5;121m'
S8='\x1b[1;93m'
S7='\x1b[38;5;92m' 
S6='\x1b[1;38;5;121m' 
S5='\x1b[1;38;5;121m'
S4='\x1b[1;96m'
S3='\x1b[1;38;5;121m'
S2='\x1b[38;5;92m' 
S1='\x1b[1;38;5;121m' 
S00='\x1b[1;38;5;121m' 
S99='\x1b[1;96m'
S88='\x1b[1;38;5;121m'
S77='\x1b[38;5;117m'
S66='\x1b[1;32m'
S55='\x1b[38;5;117m'
S44='\x1b[38;5;180m'
S33='\x1b[1;38;5;121m'
S22='\x1b[38;5;117m'
S11='\033[2;35m'
S000='\x1b[38;5;117m'
S999='\x1b[1;32m'
S888='\x1b[38;5;117m'
S777='\x1b[1;38;5;121m'
time1 = time.localtime()
time2 = time.strftime('''%d/%m/%Y''')
print('')
time3 = time.strftime('''%H:%M:%S''')
print('')
print('')
print(f'''{C} \x1b[38;5;208m 𝕋ℍ𝔼 𝔻𝔸𝕋𝔼 \x1b[1;38;5;121m ♥   \x1b[1;38;5;121m   ♣ \x1b[1;96m{time2} \x1b[1;38;5;121m ♣''')
print('')
print(f'''{C} \x1b[38;5;208m 𝕋ℍ𝔼 𝕋𝕀𝕄𝔼 \x1b[1;38;5;121m ♥   \x1b[1;38;5;121m    ♣	\x1b[1;96m{time3} \x1b[1;38;5;121m ♣''')
print()
print(' ✖✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖  ')
print()
TOKEN=input('  \x1b[38;5;117m{\x1b[1;32m•\x1b[38;5;117m}  \x1b[38;5;180m𝐓𝐎𝐊𝐄𝐍  \x1b[1;38;5;121m ๛   \x1b[38;5;117m')
bot = telebot.TeleBot(TOKEN)
print('\033[2;35m')
print(' ✖✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖  ')
print()
print()
print(' ✖✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖  ')
print("the bot is ready to work by @S_J_O_D ")			

# TOKEN = str(input("Enter your token: "))  # 
generator = pipeline('text-generation', model='gpt2')
set_seed(42)

def remove_urls(text):
    return re.sub(r'http\S+', '', text)

def generate_report(title):
    prompt = f" {title}"
    results = generator(prompt, max_length=600, temperature=0.7, top_p=0.9, num_return_sequences=1, truncation=True)
    generated_text = remove_urls(results[0]['generated_text'])

    print("النص الناتج من قبل النموذج :\n", generated_text)
    report_sections = [generated_text, "Purpose of the Report", "Standard Specifications", "Steps of Work", "Calculations", "Discussion"]
    report = {section: "" for section in report_sections}

    current_section = None
    for line in generated_text.split('\n'):
        line = line.strip()
        if line in report_sections:
            current_section = line
        elif current_section:
            report[current_section] += line + '\n'

    return report

def create_pdf(content):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=14)
    for title, text in content.items():
        pdf.add_page()
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 10, title, ln=True, align='C')
        pdf.set_font("Arial", size=14)
        pdf.multi_cell(0, 10, text)
    pdf_content = pdf.output(dest='S').encode('latin-1')
    pdf_file = BytesIO(pdf_content)
    pdf_file.name = "report.pdf"
    return pdf_file

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "ارسل لي عنوان التقرير.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    title = message.text
    prompt = f" {title}"
    results = generator(prompt, max_length=600, temperature=0.7, top_p=0.9, num_return_sequences=1, truncation=True)
    generated_text = remove_urls(results[0]['generated_text'])
    bot.send_message(message.chat.id, generated_text)


    # def generate_and_send_report():
    #     pdf_content = generate_report(title)
    #     pdf_file = create_pdf(pdf_content)
    #     pdf_file.name = "report.pdf"

    # Start a new thread for report generation
    # thread = threading.Thread(target=generate_and_send_report)
    # thread.start()



bot.polling(timeout=60)  # Increase timeout to 60 seconds
