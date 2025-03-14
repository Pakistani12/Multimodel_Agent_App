# Multimodel_Agent_App
## This is a Streamlit-based Stock Analysis application that utilizes AI agents to fetch financial data and provide investment recommendations.
## Features
- Fetch stock price, fundamentals, and analyst recommendations.
- Uses OpenAI and Groq models for financial insights.
- Web search for additional information.
- Displays data in a structured format.

 ```sh
   pip install -r requirements.txt
   ```

Create a `.env` file and add:
   ```ini
   OPENAI_API_KEY=your_openai_api_key
   GROQ_API_KEY=your_groq_api_key
   ```

Run the application with:
```sh
streamlit run app.py
```

## Technologies Used
- Python
- Streamlit
- Agno AI Agents
- OpenAI API
- Groq API
- YFinance
- DuckDuckGo Search

## License
MIT License

