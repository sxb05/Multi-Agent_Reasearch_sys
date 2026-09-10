# from src.tools.tools import web_search, scrape_webpage
from src.pipelines.pipeline import research_pipeline
                                        # from rich import print
                                        # # result = web_search("what is the capital of France?")
                                        # # print(result)
                                        # web_result = web_search.invoke("tell me about Bangalore")
                                        # print(web_result)
                                        # print(scrape_webpage.invoke("https://en.wikipedia.org/wiki/Paris"))
topic = " the impact of ai on job market in 2026"
research_pipeline(topic, num_results=5)