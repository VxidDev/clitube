import os , argparse , subprocess
from colorama import Fore , Style , init

init()

def main():
    parser = argparse.ArgumentParser(description="Small script that allows you to control youtube through terminal!")

    parser.add_argument("-n" , "--name" , help="name of video to search it!")
    parser.add_argument("-id" , help="ID of the video to use it instead of searching!")
    parser.add_argument("-p" , "--play" , action="store_true" , help="play the video!")
    parser.add_argument("-d" , "--download" , action="store_true" , help="download the video!")
    parser.add_argument("-s" , "--search" , help="number of searches for the ID!")
    parser.add_argument("-l" , "--loop" , action="store_true" , help="loop the video!")
    parser.add_argument("-nv" , "--no-video" , action="store_true" , help="disable the video!")
    parser.add_argument("-na" , "--no-audio" , action="store_true" , help="disable the audio!")

    args = parser.parse_args()
    
    if args.name and not args.search:
        video_id = subprocess.run(f"yt-dlp 'ytsearch1: {args.name}' --get-id" , capture_output=True , shell=True , text=True).stdout.strip()
    
        if video_id == '':
            print(Style.BRIGHT , Fore.RED + "No Video Found!" , Style.RESET_ALL)
            return
            
        command = f'mpv https://youtube.com/watch?v={video_id}'

    if args.id:
        command = f'mpv https://youtube.com/watch?v={args.id}'
    
    if args.play:
        if args.loop:
            command = f"{command} --loop"
        if args.no_video:
            command = f"{command} --no-video"
        if args.no_audio:
            command = f"{command} --no-audio"

        os.system(command)
    elif args.download:
        os.system(f"yt-dlp {command}")

    if args.search:
        try:
            print(Style.BRIGHT , Fore.WHITE + "Searching..." , Style.RESET_ALL)
            video_data = subprocess.run(["yt-dlp" , f"ytsearch{int(args.search)}: {args.name}" , "--get-id" , "--get-title"] , capture_output=True , text=True)
            if video_data.stdout != '':
                print(video_data.stdout)
            else:
                print(Style.BRIGHT , Fore.RED + "No Videos Found!" , Style.RESET_ALL)
        except ValueError:
            print(Style.BRIGHT , Fore.RED , "You must provide a number in -s argument!" , Style.RESET_ALL)
            return

if __name__ == "__main__":
    main()
