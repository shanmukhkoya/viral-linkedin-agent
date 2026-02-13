import os
from news_search_tool import GoogleNewsSearch
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

class ResearchAgent:
    def __init__(self, model_name="llama3"):
        self.search_tool = GoogleNewsSearch()
        self.llm = OllamaLLM(model=model_name)
        
    def search_web(self, topic):
        """Searches the web for the given topic using Google News RSS."""
        print(f"Searching for: {topic}...")
        try:
            results = self.search_tool.search(topic, days=3) # Search last 3 days for freshness
            if results:
                # Format results for the LLM
                formatted_results = ""
                for item in results:
                    formatted_results += f"- Title: {item['title']}\n  Link: {item['link']}\n  Summary: {item['summary']}\n\n"
                return formatted_results
            else:
                return "No recent viral news found."
        except Exception as e:
            print(f"Search failed: {e}")
            return f"Search failed due to error: {e}"

    def summarize_research(self, research_data, topic):
        """Summarizes the research data using Ollama."""
        print(f"Summarizing research for: {topic}...")
        template = """
        You are a research assistant. Summarize the following news search results about "{topic}" 
        into a concise bulleted list of key trends and potential viral angles for a LinkedIn post.
        
        Search Results:
        {research_data}
        
        Summary:
        """
        prompt = PromptTemplate(template=template, input_variables=["topic", "research_data"])
        
        # Using LCEL pipe syntax
        chain = prompt | self.llm | StrOutputParser()
        
        summary = chain.invoke({"topic": topic, "research_data": research_data})
        return summary

    def run(self, topic):
        research_data = self.search_web(topic)
        summary = self.summarize_research(research_data, topic)
        return summary

if __name__ == "__main__":
    agent = ResearchAgent()
    topic = "Generative AI"
    print(agent.run(topic))
