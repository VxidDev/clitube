import os , argparse , subprocess , sys                     # Crucial libraries.
from colorama import Fore , Style , init               

init() # initiating colorama.

def check_args(args): # function which was made to determine if any arguments were passed.
    global parser # get args
    no_vars = True 
    for var , value in vars(args).items(): # iterate over arguments
        if value not in [False , "False" , None , "None"]: # treat both Python None and string "None"/"False" as "not provided"
            no_vars = False # set "no argument" variable to false.
        else: # skip if its False.
            pass 

    if no_vars is True:
        print(parser.description) # print script's description and exit.
        sys.exit()

def main():
    global parser # make parser global so check_args can access parser's description.
    parser = argparse.ArgumentParser(description="Small script that allows you to control youtube through terminal!")

    parser.add_argument("-n" , "--name" , help="name of video to search it!")
    parser.add_argument("-id" , help="ID of the video to use it instead of searching!")
    parser.add_argument("-p" , "--play" , action="store_true" , help="play the video!")
    parser.add_argument("-d" , "--download" , action="store_true" , help="download the video!")
    parser.add_argument("-s" , "--search" , type=int , help="number of searches for the ID!")
    parser.add_argument("-l" , "--loop" , action="store_true" , help="loop the video!")
    parser.add_argument("-nv" , "--no-video" , action="store_true" , help="disable the video!")
    parser.add_argument("-na" , "--no-audio" , action="store_true" , help="disable the audio!")

    args = parser.parse_args() 

    check_args(args) # check args

    if (args.name and args.id) is (False or None or "False" or "None"): # check if name or id of video is passed.
        return print("No name/id given! Unable to" + Style.BRIGHT + Fore.RED + " proceed." + Style.RESET_ALL)
        
    if (args.play and args.download and args.search) is (False or None or "False" or "None"): # check if any action is selected.
        return print("No action selected!" + Style.BRIGHT + Fore.RED + " Quiting..." + Style.RESET_ALL)

    if args.name and not args.search: # get video's id
        video_id = subprocess.run(f"yt-dlp 'ytsearch1: {args.name}' --get-id" , capture_output=True , shell=True , text=True).stdout.strip()
    
        if video_id == '': # exit if no video/internet.
            print(Style.BRIGHT , Fore.RED + "No Video Found!" , Style.RESET_ALL)
            return
            
        command = f'mpv https://youtube.com/watch?v={video_id}' # make basic command.

    if args.id:
        command = f'mpv https://youtube.com/watch?v={args.id}' # skip getting id if id is already passed.
    
    if args.play: # play action logic.
        if args.loop:
            command = f"{command} --loop"
        if args.no_video:
            command = f"{command} --no-video"
        if args.no_audio:
            command = f"{command} --no-audio"

        os.system(command)
    elif args.download: # download action logic.
        os.system(f"yt-dlp {command.removeprefix('mpv').strip()}")

    if args.search: # search action logic.
        if not args.name:
            print("Please enter a --name/-name argument with name to search!") # if no name is passed skip. (POSSIBLE OPTIMIZATION HERE)
            return 0
        print(Style.BRIGHT , Fore.WHITE + "Searching..." , Style.RESET_ALL)
        video_data = subprocess.run(["yt-dlp" , f"ytsearch{int(args.search)}: {args.name}" , "--get-id" , "--get-title"] , capture_output=True , text=True) # download using yt-dlp
        if video_data.stdout != '': # if output is not an empty string, print.
            print(video_data.stdout)
        else: # if output is empty.
            print(Style.BRIGHT , Fore.RED + "No Videos Found!" , Style.RESET_ALL) 

if __name__ == "__main__":
    main() # run
