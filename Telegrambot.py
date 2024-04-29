import requests

def search_google(query):
    api_key = "6569312893:AAFKp83PZWkhU-oc3ThOzOWs1QsgQTJ4qs4"
    search_engine_id = "YOUR_SEARCH_ENGINE_ID"
    url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={search_engine_id}&q={query}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        search_results = data.get("items", [])
        return search_results
    else:
        return None

def handle_search(update, context):
    query = " ".join(context.args)
    search_results = search_google(query)
    if search_results:
        for result in search_results[:5]:
            title = result.get("title")
            link = result.get("link")
            snippet = result.get("snippet")
            message = f"<b>{title}</b>\n{snippet}\n<a href='{link}'>Read More</a>"
            update.message.reply_html(message)
    else:
        update.message.reply_text("Sorry, I couldn't find any results for that query.")

# Add command handler for "/search" command
dispatcher.add_handler(CommandHandler("search", handle_search))
