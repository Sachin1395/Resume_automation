import PyPDF2
import google.generativeai as genai

def pdf_to_text(pdf_path, output_path=None):
    try:
        # Open the PDF file
        with open(pdf_path, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            text = ""

            # Extract text from each page
            for page in reader.pages:
                text += page.extract_text()

            # Save to a text file if output_path is provided
            if output_path:
                with open(output_path, 'w', encoding='utf-8') as text_file:
                    text_file.write(text)
                print(f"Text extracted and saved to {output_path}")
            else:
                print("Extracted Text:")
                print(text)

            return text
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

pdf_path = "_9225 Sachin one page (1).pdf"  # Replace with your PDF file path
output_path = "output.txt"  # Optional: Replace with your desired text file path


genai.configure(api_key="AIzaSyA-UjYFpBvXHa7EEXPgVTKB5DuQF8h9wWs")
model = genai.GenerativeModel("gemini-1.5-flash")
def extract_data(file):
    data_str = pdf_to_text(pdf_path, output_path)

    data_list = ["Name", "Skills", "Experience", "Education", "Email",
                 "Phone Number"]
    data = {
        "Name": "",
        "Email": "",
        "Phone Number": "",
        "Skills": "",
        "Experience": "",
        "Education": "",
    }
    for x in data_list:
        response = model.generate_content(
            f"{data_str}: from the data find the {x} and if there are multiple items give it as a comma seperated list that is suitable to store in excel sheet")
        gen_content = response.text
        data[x] = gen_content
        print(x + ":" + data[x])
    return data

job_desc = "flask, python, web development, flutter, reactjs, tensorflow"
def validate(data):
    response = model.generate_content(f"{data} : give only the percentage match (without any text) for this skills with the job description  : {job_desc} ")
    return response.text