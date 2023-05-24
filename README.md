# Langchain
# GPT Creator

This project provides a web application that generates YouTube video titles and scripts based on user prompts using the GPT-3.5 language model.

## Installation

1. Clone the repository:


2. Install the required dependencies:

pip install -r requirements.txt

3. Set up the API key:

- Obtain an API key from OpenAI and save it in the `apikey.py` file.
- Set the `OPENAI_API_KEY` environment variable with your API key.

## Usage

1. Run the application:

streamlit run main.py

2. Open your web browser and go to `http://localhost:8501`.

3. Enter a prompt in the provided text input.

4. The application will generate a YouTube video title and script based on the prompt.

5. The generated title, script, and relevant information will be displayed on the screen.

## Prompt Templates

The application uses prompt templates to structure the input prompts for generating titles and scripts. Currently, the following templates are available:

- Title Template: `write me a youtube video title about {topic}`
- Script Template: `write me a youtube video script based on this title TITLE: {title} while leveraging this wikipedia research: {wikipedia_research}`

## Conversations and Memory

The application uses conversation buffers and memory to keep track of previous interactions. The following buffers are used:

- Title History: Displays the conversation history for generating titles.
- Script History: Displays the conversation history for generating scripts.
- Wikipedia Research: Displays the Wikipedia research used for script generation.

## Contributing

Contributions are welcome! If you find any issues or want to add new features, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
