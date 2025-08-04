# Budget Meal Maps 🍽️🗺️

A smart web application that helps you find restaurants near your location based on your budget, meal preferences, and dietary requirements. The app uses Google's Gemini AI to provide personalized restaurant recommendations and displays them on an interactive Google Maps interface.

## Features ✨

- **Multi-language Support**: Available in English, Spanish, Chinese, Japanese, Korean, and Hindi
- **Budget Filtering**: Find restaurants within your specified budget range
- **Meal Type Selection**: Choose from Breakfast, Lunch, Dinner, or Snacks
- **Dietary Preferences**: Filter by Any, Vegan, Vegetarian, or Non-Veg options
- **Cuisine Types**: Select from various cuisines including American, Mexican, Indian, Japanese, Mediterranean, Chinese, Thai, Korean, or Any
- **Location-based Search**: Enter your zip code to find nearby restaurants
- **Interactive Maps**: View restaurant locations on Google Maps with directions
- **Detailed Information**: Get restaurant details including name, cuisine, address, price range, specialty, rating, and distance

## Screenshots 📸

The app provides a clean, user-friendly interface where you can:
- Select your preferences from dropdown menus
- Enter your budget and zip code
- Generate personalized restaurant recommendations
- View results on an interactive map

## Installation 🚀

### Prerequisites

- Python 3.7 or higher
- Google API Key for Gemini AI
- Google Maps API Key

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Budget-Meal-Maps
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the project root and add your API keys:
   ```
   GOOGLE_API_KEY=your_gemini_api_key_here
   GOOGLE_MAP_API_KEY=your_google_maps_api_key_here
   ```

4. **Get API Keys**
   
   - **Google Gemini API Key**: Visit [Google AI Studio](https://makersuite.google.com/app/apikey) to get your API key
   - **Google Maps API Key**: Visit [Google Cloud Console](https://console.cloud.google.com/) and enable the Maps Embed API

## Usage 💡

1. **Run the application**
   ```bash
   python app.py
   ```

2. **Open your browser**
   - The app will launch on `http://localhost:7860` (or another port if 7860 is busy)

3. **Configure your search**
   - **Language**: Select your preferred language
   - **Budget**: Enter your maximum budget amount
   - **Meal Type**: Choose Breakfast, Lunch, Dinner, or Snacks
   - **Diet Type**: Select Any, Vegan, Vegetarian, or Non-Veg
   - **Cuisine Type**: Choose from available cuisine options or "Any"
   - **Zip Code**: Enter your current zip code for location-based results

4. **Generate Results**
   - Click the "Generate" button
   - View restaurant recommendations with detailed information
   - Explore locations on the interactive Google Maps interface

## How It Works 🔧

1. **AI-Powered Recommendations**: The app uses Google's Gemini 2.0 Flash model to generate restaurant recommendations based on your criteria
2. **JSON Processing**: Restaurant data is returned in JSON format and processed for display
3. **Map Integration**: Restaurant addresses are used to create interactive Google Maps with directions
4. **Multi-language Support**: The AI model can provide recommendations in multiple languages

## Dependencies 📦

- `google.generativeai`: Google's Gemini AI API client
- `gradio`: Web interface framework
- `pathlib`: Path manipulation utilities
- `textwrap`: Text formatting utilities
- `python-dotenv`: Environment variable management
- `json`: JSON data processing

## API Configuration ⚙️

The app uses two main APIs:

### Google Gemini AI
- **Model**: gemini-2.0-flash
- **Temperature**: 0.9 (for creative responses)
- **Max Output Tokens**: 2000
- **Response Format**: JSON

### Google Maps Embed API
- **Purpose**: Display interactive maps with restaurant locations
- **Features**: Directions, waypoints, and location visualization

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.

## License 📄

This project is open source and available under the [MIT License](LICENSE).

## Support 💬

If you encounter any issues or have questions, please open an issue on the repository.

---

**Happy dining! 🍕🍜🍔**
