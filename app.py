import pathlib
import textwrap
import google.generativeai as genai
import os
import gradio as gr
from dotenv import load_dotenv
import json



def gemini_chat_builder(language_input,Budget_input,meal_type,diet_type,zip_code):
    if not zip_code:
        response=chat.send_message(f""" "I'm looking for restaurants near {zip_code} that offer {meal_type} meals within a budget of {Budget_input}. I prefer {diet_type} options. Please provide a list of popular restaurants in this area with their details in {language_input}
  Please provide a list of 8-10 popular restaurants in this area. For each restaurant, include:
  - Name
  - Type of cuisine
  - Approximate address or area
  - Price range (budget, moderate, expensive)
  - What makes it special or popular
  
  Format your response as a JSON array with this structure:
  
    {{
      "name": "Restaurant Name",
      "cuisine": "Type of cuisine",
      "address": "Approximate address or area",
      "priceRange": "budget|moderate|expensive",
      "specialty": "What makes it special",
      "rating": "4.5",
      "distance": "0.8"
    }}
  
  
  Make sure the JSON is valid and properly formatted. Include a variety of cuisines and price ranges in {language_input}""",generation_config=generation_config)
    else:
        response=chat.send_message(f""" "I'm looking for restaurants near 95051 that offer {meal_type} meals within a budget of {Budget_input}. I prefer {diet_type} options. Please provide a list of popular restaurants in this area with their details in {language_input}.Please provide a list of 8-10 popular restaurants in this area. For each restaurant, include:
  - Name
  - Type of cuisine
  - Approximate address or area
  - Price range (budget, moderate, expensive)
  - What makes it special or popular  
  Format your response as a JSON array with this structure:
  
    {{
      "name": "Restaurant Name",
      "cuisine": "Type of cuisine",
      "address": "Approximate address or area",
      "priceRange": "budget|moderate|expensive",
      "specialty": "What makes it special",
      "rating": "4.5",
      "distance": "0.8"
    }}
   Make sure the JSON is valid and properly formatted. Include a variety of cuisines and price ranges in {language_input}""",generation_config=generation_config)
    #return json_to_html(response.text)
    #text = response.text.replace("json", "").replace("[", "").replace("]", "").replace("```","").strip()
    return generate_google_maps_iframes(response.text)
    #return f"""The {type_input} is required for the {name_input}"""

def generate_google_maps_iframes(json_str):
    try:
        restaurants = json.loads(json_str)
    except Exception:
        return "<p>Invalid JSON response.</p>"
    iframes_html = ""
    for r in restaurants:
        address = r.get('address', '')
        name = r.get('name', '')
        if address:
            # Use Google Maps Embed API with place search
            query = f"{name} {address}".replace(' ', '+')
            iframe = f"""
            <iframe
                width="400"
                height="300"
                style="border:0;margin:10px;"
                loading="lazy"
                allowfullscreen
                referrerpolicy="no-referrer-when-downgrade"
                src="https://www.google.com/maps/embed/v1/search?key={MAP_API_KEY}&q={query}">
            </iframe>
            """
            # Build bullet points for restaurant details
            details = "<ul style='margin:0 0 10px 0;padding-left:20px;'>"
            details += f"<li><strong>Name:</strong> {name}</li>"
            details += f"<li><strong>Cuisine:</strong> {r.get('cuisine','')}</li>"
            details += f"<li><strong>Address:</strong> {address}</li>"
            details += f"<li><strong>Price Range:</strong> {r.get('priceRange','')}</li>"
            details += f"<li><strong>Specialty:</strong> {r.get('specialty','')}</li>"
            details += f"<li><strong>Rating:</strong> {r.get('rating','')}</li>"
            details += f"<li><strong>Distance:</strong> {r.get('distance','')} miles</li>"
            details += "</ul>"
            # Show map and details side by side
            iframes_html += f"""
            <div style="display:flex;align-items:flex-start;margin-bottom:20px;">
                {iframe}
                <div style="margin-left:20px;max-width:350px;">{details}</div>
            </div>
            """
    return iframes_html if iframes_html else "<p>No valid addresses found.</p>"

def format_text_to_json(text):
    try:       
        data = json.loads(text)
        return json.dumps(data, indent=2, ensure_ascii=False)
    except Exception:
        return json.dumps({"error": "Invalid JSON input."}, indent=2)

def json_to_html(json_str):
    try:
        restaurants = json.loads(json_str)
    except Exception:
        return "<p>Invalid JSON response.</p>"
    html = "<div>"
    for r in restaurants:
        html += f"""
        <div style='margin-bottom:20px;padding:10px;border:1px solid #ccc;border-radius:8px;'>
            <h3>{r.get('name','')}</h3>
            <p><strong>Cuisine:</strong> {r.get('cuisine','')}</p>
            <p><strong>Address:</strong> {r.get('address','')}</p>
            <p><strong>Price Range:</strong> {r.get('priceRange','')}</p>
            <p><strong>Specialty:</strong> {r.get('specialty','')}</p>
            <p><strong>Rating:</strong> {r.get('rating','')}</p>
            <p><strong>Distance:</strong> {r.get('distance','')} miles</p>
        </div>
        """
    html += "</div>"
    return html


load_dotenv()

API_KEY=os.getenv('GOOGLE_API_KEY')
MAP_API_KEY=os.getenv('GOOGLE_MAP_API_KEY')

genai.configure(api_key=API_KEY)

#model=genai.GenerativeModel('gemini-pro')
model=genai.GenerativeModel('gemini-2.0-flash')
print(genai.list_models())

generation_config=genai.GenerationConfig(
    stop_sequences=None,
    temperature=0.9,
    top_p=1.0,
    top_k=40,
    candidate_count=1,
    max_output_tokens=2000,
    response_mime_type="application/json"
)

chat=model.start_chat()

demo=gr.Interface(
    gemini_chat_builder,[
    gr.Dropdown(
        ["English","Spanish","Chinese","Japanese","Korean","Hindi"],multiselect=False,label="Language",info="Select Language",value="English"
    ),
    gr.Textbox(
        label="Input Amount",
        info="Enter Budget Amount",
        lines=1,
        value="50"
    ),
    gr.Dropdown(
        ["Breakfast","Lunch","Dinner","Snacks"],multiselect=False,label="Meal Type",info="Select Type of Meal",value="Breakfast"
    ),
     gr.Dropdown(
        ["Any","Vegan","Vegeterian","Non-Veg"],multiselect=False,label="Diet Type",info="Select Type of Diet",value="Any"
    ),
    gr.Textbox(
        label="Input Zip Code",
        info="Add your current Zip Code",                
        lines=1,
        value="95051"
    )],
    "html",title="Budget Meal Finder",css="footer {visibility: hidden}",allow_flagging="never",submit_btn=gr.Button("Generate")
)

    
if __name__=='__main__':
    demo.launch()