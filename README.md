# Web Scraping with OpenAI-Powered AI

Welcome to the Web Scraping AI project! This project leverages artificial intelligence provided by OpenAI, combined with powerful Python libraries, to extract structured data from websites. The extracted data is stored in JSON files for further analysis and usage.

---

## About the Project

This project integrates OpenAI's advanced language models with web scraping techniques to automate the extraction of relevant data from websites. The goal is to provide a streamlined and efficient way to gather, process, and structure web data for various applications.

### Key Objectives:
- Scrape data from web pages.
- Structure the extracted data into JSON format.
- Utilize AI models for intelligent scraping and data processing.

---

## Features

- **AI-Powered Scraping**: Uses OpenAI and LangChain for intelligent and efficient web data extraction.
- **JSON Output**: Saves extracted data in structured JSON format.
- **Automation**: Automates data scraping tasks using Playwright for seamless navigation and data collection.

---

## Technologies Used

The project relies on the following Python libraries and tools:

- [**BeautifulSoup4**](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) `4.12.3` - For parsing HTML and XML documents.
- [**LangChain**](https://github.com/hwchase17/langchain) `0.3.14` - To build chains for AI-powered decision-making.
- [**LangChain-OpenAI**](https://github.com/langchain-ai/langchain-openai) `0.3.0` - Integration with OpenAI's API.
- [**Playwright**](https://playwright.dev/python/) `1.49.1` - For browser automation and navigation.
- [**Python-Decouple**](https://github.com/henriquebastos/python-decouple) `3.8` - For environment variable management.
- [**LangChain-Community**](https://github.com/langchain-community) `0.3.14` - Additional community-based extensions for LangChain.

---

## Setup and Installation

Follow these steps to set up and run the project locally:

### Prerequisites

- Python 3.9 or higher
- Access to OpenAI API
- Node.js (for Playwright dependencies)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/web-scraping-ai.git
   cd web-scraping-ai
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright browsers**:
   ```bash
   playwright install
   ```

5. **Configure environment variables**:
   Create a `.env` file and add your OpenAI API key:
   ```env
   OPENAI_API_KEY=your-openai-api-key
   ```

---

## Usage

1. **Run the web scraper**:
   Execute the main script to start scraping:
   ```bash
   python main.py
   ```

2. **Output**:
   Extracted data will be saved in the `data` directory as JSON files.

3. **Customize scraping targets**:
   Edit the `config.py` file to modify the target URLs and scraping logic.

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add a new feature"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request.

---

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute this project with proper attribution.

---

## Acknowledgments

- [OpenAI](https://openai.com/) for their powerful language models.
- [LangChain](https://github.com/hwchase17/langchain) for enabling advanced AI chains.
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) for HTML parsing.
- [Playwright](https://playwright.dev/python/) for browser automation.
- [Python-Decouple](https://github.com/henriquebastos/python-decouple) for environment management.

---

Feel free to reach out for support or further questions!

