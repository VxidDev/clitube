import typer , subprocess , tomli
from rich.console import Console
from random import choice

app = typer.Typer(name="clitube")
console = Console()

downloadColors = [
    "bold purple",
    "bold magenta",
    "bold cyan",
]

playColors = [
    "bold yellow",
    "bold blue"
]

logStatuses = {
    "info": "bold white",
    "success": "bold green",
    "warn": "bold yellow",
    "error": "bold red",
    "fatal": "bold dark_red"
}

class LogStatusError(BaseException):
    pass

def log(message: str , status: str):
    if status not in logStatuses.keys():
        raise LogStatusError("Unknown status.")
    
    console.print(f"[{logStatuses[status.lower()]}][{status.upper()}][/{logStatuses[status.lower()]}] [bold white]{message}[/bold white]")

@app.command()
def play(name: str=None , id: str=None , loop: bool=False , noAudio: bool=False , noVideo: bool=False , debug: bool=False):
    videoData = [None , None]
    if debug:
        log("Checking if passed arguments meet requirements..." , "info")
    if id and name:
        raise typer.BadParameter("You cant use both 'id' and 'name'!")
    if not (id or name):
        raise typer.BadParameter("You must pass either 'id' or 'name'!")
    if noVideo and noAudio:
        raise typer.BadParameter("You cant use both of 'noAudio' and 'noVideo' parameters!")
    if debug:
        log("All arguments pass requirements. Proceeding..." , "success")
    
    if debug:
        log("Randomizing color..." , "info")
    color = choice(playColors)
    if debug:
        log(f"Color is {color}" , "success")

    if name:
        console.print(f"[bold white]Fetching video [bold {color}]ID[/bold {color}] based on video name...[/bold white]")
        videoData = subprocess.run(["yt-dlp" , f"ytsearch: {name}" , "--get-id" , "--get-title"] , capture_output=True , text=True).stdout.strip().split("\n")
        if videoData[1] == '':
            if debug:
                log("Empty video id. exiting..." , "fatal")
            console.print(f"[bold red]No videos found! [/bold red][bold white]Consider adding [bold {color}]--debug[/bold {color}].[/bold white]")
            return
    
    args = []
    
    if noVideo:
        args.append("--no-video")
    if noAudio:
        args.append("--no-audio")
    if loop:
        args.append("--loop")
    
    console.print(f"[bold white]Playing [bold {color}]{id if id else videoData[0]}[/bold {color}][/bold white]")
    subprocess.Popen(["mpv" , f"ytdl://https://youtube.com/watch?v={id if id else videoData[1]}" , *args]).wait()

@app.command() 
def download(name: str=None , id: str=None , debug: bool=False):
    if debug:
        log("Checking if passed arguments meet requirements..." , "info")
    if id and name:
        raise typer.BadParameter("You cant use both 'id' and 'name'!")
    if not (id or name):
        raise typer.BadParameter("You must pass either 'id' or 'name'!")
    if debug:
        log("All arguments pass requirements. Proceeding..." , "success")
    
    if debug:
        log("Randomizing color..." , "info")
    color = choice(downloadColors)
    if debug:
        log(f"Color is {color}" , "success")
    console.print(f"[bold white]Downloading [{color}]{name or id}[/{color}]...[/bold white]")

    if name:
        if debug:
            log(f"Downloading video based on name..." , "info")
        subprocess.run(["yt-dlp" , f"ytsearch: {name}"])
        if debug:
            log(f"Video downloaded." , "success")
    else:
        if debug:
            log(f"Downloading video based on id..." , "info")
        subprocess.run(["yt-dlp" , id])
        if debug:
            log("Video downloaded." , "success")

@app.command()
def version(debug: bool=False):
    if debug:
        log("Extracting pyproject.toml for version..." , "info")
    version = tomli.load(open("pyproject.toml" , "rb"))["project"]["version"]
    if debug:
        log("Successfully extracted version." , "success")
    console.print(f"[bold red]Cli[/bold red][bold white]Tube - {version}[/bold white]")

@app.command()
def search(amount: int , name: str , debug: bool=False):
    console.print(f"[bold white]Searching {amount} videos with name similar to '{name}'...")

    subprocess.run(["yt-dlp" , f"ytsearch{amount}: {name}" , "--get-id" , "--get-title"])

if __name__ == "__main__":
    app()
