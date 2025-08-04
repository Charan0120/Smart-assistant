import os
import google.generativeai as genai
from dotenv import load_dotenv  

load_dotenv() 

def main():
    
    SYSTEM_PROMPT = """
    You are a helpful and smart assistant. Your primary goal is to provide clear, well-structured, and reasoned answers.

    Follow these instructions for every user query:
    1.  **Think Step-by-Step:** Before generating a final answer, internally break down the user's question to formulate a step-by-step plan.
    2.  **Structure Your Output:** Present your final answer in a clean, easy-to-read format. Use lists, bolding, and clear paragraphs where appropriate.
    3.  **Handle Specific Topics:**
        * For questions about natural phenomena (e.g., "why is the sky is blue?", "what are the colors in a rainbow?"), provide a step-by-step explanation or a numbered list.
        * For factual questions (e.g., "which planet is the hottest?"), provide the answer along with the reasoning behind it.
    4.  **Refuse Mathematical Calculations:** This is a critical rule. You must NEVER solve mathematical problems (e.g., "what is 15 + 23?"). If you receive a math query, you must refuse to answer it and politely suggest that the user should use a calculator tool.
    """

    try:
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            print(" Error: GEMINI_API_KEY environment variable not found.")
            print("Please set your API key in the terminal and try again.")
            return

        genai.configure(api_key=api_key)

        model = genai.GenerativeModel(
            model_name='gemini-1.5-flash',
            system_instruction=SYSTEM_PROMPT
        )
    except Exception as e:
        print(f" Error during initialization: {e}")
        return

    print(" LLM Smart Assistant is online. Type 'exit' or 'quit' to end the session.")
    print("-" * 60)

    while True:
        user_question = input("You: ")

        if user_question.lower() in ['exit', 'quit']:
            print(" Goodbye!")
            break

        if not user_question.strip():
            continue

        try:
            response = model.generate_content(user_question)
            print(f"\nAssistant: {response.text}\n" + "-" * 60)
        except Exception as e:
            print(f"An error occurred while generating the response: {e}")


if __name__ == "__main__":
    main()