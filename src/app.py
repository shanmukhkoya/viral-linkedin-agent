import streamlit as st
import time
from research_agent import ResearchAgent
from content_agent import ContentAgent

def main():
    st.set_page_config(page_title="Viral Topic Researcher & Post Generator", page_icon="🚀", layout="wide")
    
    st.title("🚀 Viral Topic Researcher & LinkedIn Post Generator")
    st.markdown("Enter a topic to research viral trends and generate a LinkedIn post.")

    # Sidebar for configuration
    st.sidebar.header("Configuration")
    model_options = ["llama3", "phi3", "gemma2:2b", "mistral"]
    model_name = st.sidebar.selectbox("Ollama Model Name", model_options, index=0)
    tone = st.sidebar.selectbox("Post Tone", ["Professional", "Casual", "Controversial", "Inspirational", "Educational"])
    
    # Initialization
    if 'research_agent' not in st.session_state or st.session_state.research_agent.llm.model != model_name:
        st.session_state.research_agent = ResearchAgent(model_name=model_name)
    if 'content_agent' not in st.session_state or st.session_state.content_agent.llm.model != model_name:
        st.session_state.content_agent = ContentAgent(model_name=model_name)

    # Main Content
    topic = st.text_input("Enter Topic (e.g., Generative AI, Quantum Computing)", "Generative AI")
    
    @st.cache_data(show_spinner=False)
    def get_research_summary(_agent, topic):
        return _agent.run(topic)

    if st.button("Research & Generate Post"):
        with st.status("Working...", expanded=True) as status:
            start_time = time.time()
            st.write("🔍 Researching topic...")
            try:
                # Use cached research if available
                research_summary = get_research_summary(st.session_state.research_agent, topic)
                st.write("✅ Research complete!")
                
                st.subheader("Research Summary")
                st.info(research_summary)
                
                st.write("📝 Generating LinkedIn Post...")
                post = st.session_state.content_agent.generate_post(research_summary, topic, tone)
                
                end_time = time.time()
                st.write(f"✅ Post generated in {end_time - start_time:.2f} seconds!")
                status.update(label="Process Complete!", state="complete", expanded=False)
                
                st.subheader("Generated LinkedIn Post")
                st.text_area("Copy your post:", value=post, height=400)
                
            except Exception as e:
                st.error(f"An error occurred: {e}")
                status.update(label="Error Occurred", state="error")

if __name__ == "__main__":
    main()
