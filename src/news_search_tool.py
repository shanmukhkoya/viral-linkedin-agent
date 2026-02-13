import feedparser
import urllib.parse

class GoogleNewsSearch:
    def __init__(self):
        self.base_url = "https://news.google.com/rss/search"

    def search(self, query, days=7):
        """
        Searches Google News RSS feed for the given query.
        Args:
            query (str): The search topic.
            days (int): Limit results to the past N days.
        Returns:
            list: A list of dictionaries containing title, link, and pubDate.
        """
        encoded_query = urllib.parse.quote(query)
        # q={query}+when:{days}d filters for the last N days
        rss_url = f"{self.base_url}?q={encoded_query}+when:{days}d&hl=en-US&gl=US&ceid=US:en"
        
        print(f"Fetching RSS feed from: {rss_url}")
        feed = feedparser.parse(rss_url)
        
        results = []
        if feed.entries:
            for entry in feed.entries[:10]:  # Limit to top 10 results
                results.append({
                    "title": entry.title,
                    "link": entry.link,
                    "published": entry.published,
                    "summary": entry.description
                })
        else:
            print("No entries found in RSS feed.")
            
        return results

if __name__ == "__main__":
    tool = GoogleNewsSearch()
    news = tool.search("Generative AI Agentic")
    for item in news:
        print(f"- {item['title']} ({item['published']})")
