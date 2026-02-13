from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

class ContentAgent:
    def __init__(self, model_name="llama3"):
        self.llm = OllamaLLM(model=model_name)

    def generate_post(self, research_summary, topic, tone="Professional"):
        """Generates a LinkedIn post based on the research summary and tone."""
        print(f"Generating post for: {topic} with tone: {tone}...")
        
        template = """
        You are a expert LinkedIn content creator. Create a viral, engaging LinkedIn post about "{topic}" 
        based on the following research summary.
        
        Research Summary:
        {research_summary}
        
        Tone: {tone}
        
        Requirements:
        - Use a strong hook in the first line.
        - Use short paragraphs and bullet points for readability.
        - Include relevant emojis.
        - Include 3-5 relevant hashtags at the end.
        - The post should be professional yet engaging.
        - Do not include any preamble, just the post content.
        
        LinkedIn Post:
        """
        prompt = PromptTemplate(template=template, input_variables=["topic", "research_summary", "tone"])
        
        # Using LCEL pipe syntax
        chain = prompt | self.llm | StrOutputParser()
        
        post = chain.invoke({"topic": topic, "research_summary": research_summary, "tone": tone})
        return post

if __name__ == "__main__":
    agent = ContentAgent()
    summary = "AI is changing jobs. New roles like AI engineer are emerging."
    print(agent.generate_post(summary, "Generative AI", "Professional"))
