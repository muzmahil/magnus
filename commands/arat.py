import webbrowser


def google(query):
    if not query:
     return print("Aratmam için bir şeyler söylemen gerek!")
    else:
     webbrowser.open("https://www.google.com/search?q=" + query)

def youtube(query):
    if not query:
     return print("Aratmam için bir şey söylemen gerek!")
    else:
        webbrowser.open("https://www.youtube.com/results?search_query="+query)

exec = {
    "araştır": {
        "exec": lambda query: google(query) 
    
    },
    "youtube" : {
        "exec" : lambda query : youtube(query)
    },
    "github hesabımı aç" : {
        "exec" : lambda query : webbrowser.open("https://www.github.com/isuthecoder")
    }
}
