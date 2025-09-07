import finnhub #pip install finnhub-python
import gradio as fr
import pandas as pd 
import requests
from dotenv import load_dotenv
import os

load_dotenv()

finnhub_apikey = os.getenv("finnhub_apikey")
marketaux_apikey = os.getenv("marketaux_apikey_apikey")

#we make a function to sort given ticker by industry, and also take the industry name and put individual stocks into new lists grouped by industries

def sortbyindustry(tickrinpt)

    return 

def industrylists()
#take each industry list and get financial data for the industry name, and then all the individual stocks in the industry, + an option to store the average financial data of all in order to see things like portfolio changes

#request for news on the industries/ indivudal stocks, or for both, using a graphical choice, 3 articles per industry

#take some kind of model, take the news headline+summarything per article, group by the industry lists and plug into ai to try and get some insights/reasonable predictions etc

def build_news_prompt()

#output result, maybbe have a regenerate/ more features

#GET https://api.marketaux.com/v1/news/all HTTP/1.1 for news and sort input tickers by industry    finnhub actual stock data/industry


#take stocks input from user seperated by commas, or up to a number maybe(so not make too many requests), send into finnhub and classify whichever stock we ask for into industries, than save those + pull other relevant info


#take news based on the industries and/or stocks specifically?, input relevant headlines/whatever into whatever model we prompt, have it spit out a concise summary in an organized way that we prompt later thing by thing


#show changes from previous asks in stock price/etc, read that from saved csv file that repeats everytime when ran, also maybe evnentually make autorefreshing option, with diff time increments






#gradio interface will make funciton here for everyhting taking input/spitting output

#input could be enter stock ticker for a recent news summary of its industry(could also sort this news by recent), up to 9

def build_app():
    with gr.Blocks(title="Financial News puller") as demo:
        gr.Markdown("Financial News puller")
        gr.Markdown("Enter various stocks, and we will generate a concise overview of news on the industries and the specific stock. To specify a date range please enter in the date range box. For suggestions click Top 20 tickers today. ") # articles will be newest at top to oldest down, and we will max it out at 9 articles

        stocks = gr.Textbox(placeholder="Stocks, seperated by commas", show_label=False)
        daterangepb = gr.Textbox(placeholder="Published before Ex:2025-09-04T20:06:55 ", show_label=False)
        daterangepa = gr.Textbox(placeholder="Published after Ex:2025-09-04T20:06:55 ", show_label=False)
        20ticker_btn = gr.Button("Top 20 Gainers/Losers") #The API function of your choice. In this case, function=TOP_GAINERS_LOSERS Alphavantage
        generate_btn = gr.Button("Generate")

        output_box = gr.Textbox(lines=16, show_label=False, placeholder="Result will appear here")

'''        def generate_handler(ptype, city_name):
            weather = get_weather(city_name)
            if not isinstance(weather, dict):
                return weather
            prompt = build_weather_prompt(ptype, city_name, weather)
            model_output = call_ollama(prompt)
            return f"[{weather['location']}, {weather['temp_f']}°F, {weather['condition']}]\n\n{model_output}"
'''
        generate_btn.click(generate_handler, inputs=[piece_type, city], outputs=[output_box])
    return demo


app = build_app()
app.launch()

