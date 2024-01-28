import telebot
from fpdf import FPDF
from io import BytesIO
from transformers import pipeline, set_seed
import re
import threading

TOKEN = '6938276707:AAH0-NfQ92Fm91hpJv-a5RE8hCnuSFIcX5E'  # Replace with your token
bot = telebot.TeleBot(TOKEN)
generator = pipeline('text-generation', model='gpt2')
set_seed(42)

def remove_urls(text):
    return re.sub(r'http\S+', '', text)

def generate_report(title):
    intro = "This is a professional report on"
    prompt = f"{intro} {title}. The report includes: Introduction, Purpose of the Report, Standard Specifications, Steps of Work, Calculations, and Discussion."
    results = generator(prompt, max_length=600, temperature=0.7, top_p=0.9, num_return_sequences=1, truncation=True)
    generated_text = remove_urls(results[0]['generated_text'])

    print("AI-Generated Text:\n", generated_text)
    report_sections = ["Introduction", "Purpose of the Report", "Standard Specifications", "Steps of Work", "Calculations", "Discussion"]
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
    bot.reply_to(message, "Send me the title of the report.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    title = message.text

    def generate_and_send_report():
        pdf_content = generate_report(title)
        pdf_file = create_pdf(pdf_content)
        pdf_file.name = "report.pdf"
        bot.send_document(message.chat.id, pdf_file)

    # Start a new thread for report generation
    thread = threading.Thread(target=generate_and_send_report)
    thread.start()

bot.polling(timeout=60)  # Increase timeout to 60 seconds
