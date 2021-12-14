from pytube import YouTube as Yt
from pytube import Playlist as Pl


# maybe there is some mistakes never mind me
def finish():
    print("Download Done!")


path = "path name!"
# this my own pc path u could change by ur own

one_or_playlist = input("what do u want to download(video/playlist): ")

if one_or_playlist == "video":
    link = input("plz enter ur full video url : ")
    # link = 'https://www.youtube.com/watch?v=HhjHYkPQ8F0'
    video = Yt(link)
    print(f"the video title is: \n{video.title} \n--------------------------------")
    print(f"the video description is: \n{video.description} \n--------------------------------")
    print(f"the video views is: {video.views} \n--------------------------------")
    print(f"the video rating is: {video.rating}\n--------------------------------")
    print(f"the video duration is: {video.length} seconds")
    # print(video.streams)
    # for stream in video.streams:
    #     print(stream)

    way_download = input("manual/auto: ")

    if way_download == "manual":

        dwn_file_type = input("full video, just audio or only video")

        if dwn_file_type == "full video":
            fp_s = "25fps"
            type_dld = "video/mp4"
            prg = True
            res = input("resolution*:")

            if res == "144":
                resolution = "144p"
                video.streams.filter(res=resolution, progressive=prg, subtype="mp4").download(output_path=path)
                video.register_on_complete_callback(finish())
            elif res == "360":
                resolution = "360p"
                video.streams.filter(res=resolution, progressive=prg, subtype="mp4").download(output_path=path)
                video.register_on_complete_callback(finish())

            elif res == "720":
                resolution = "720p"
                video.streams.filter(res=resolution, progressive=prg, subtype="mp4").download(output_path=path)
                video.register_on_complete_callback(finish())

            else:
                print("non valid resolution")
        elif dwn_file_type == "just audio":
            type_dld = "audio/webm"
            prg = False
            abr = input("audio quality(48/50/70/160)kbps: ")

            if abr == "50":
                abres = "50kbps"
                video.streams.filter(abr=abres, progressive=prg, subtype="mp4").download(output_path=path)
                video.register_on_complete_callback(finish())

            elif abr == "70":
                abres = "70kbps"
                video.streams.filter(abr=abres, progressive=prg, subtype="mp4").download(output_path=path)
                video.register_on_complete_callback(finish())

            elif abr == "48":
                abres = "48kbps"
                video.streams.filter(abr=abres, progressive=prg, subtype="mp4").download(output_path=path)
                video.register_on_complete_callback(finish())

            elif abr == "160":
                abres = "160kbps"
                video.streams.filter(abr=abres, progressive=prg, subtype="mp4").download(output_path=path)
                video.register_on_complete_callback(finish())

        else:
            fps = "25fps"
            type_dld = "video/mp4"
            prg = False
            res = input("resolution*:")

            if res == "144":
                resolution = "144p"
                video.streams.filter(res=resolution, progressive=prg, subtype="mp4").download(output_path=path)
                video.register_on_complete_callback(finish())

            elif res == "360":
                resolution = "360p"
                video.streams.filter(res=resolution, progressive=prg, subtype="mp4").download(output_path=path)
                video.register_on_complete_callback(finish())

            elif res == "720":
                resolution = "720p"
                video.streams.filter(res=resolution, progressive=prg, subtype="mp4").download(output_path=path)
                video.register_on_complete_callback(finish())

            else:
                print("non valid resolution")

    else:
        quality = input("lowest/highest: ")
        if quality == "lowest":
            video.streams.get_lowest_resolution().download(output_path=path)
            video.register_on_complete_callback(finish())

        elif quality == "highest":
            video.streams.get_highest_resolution().download(output_path=path)
            video.register_on_complete_callback(finish())

elif one_or_playlist == "playlist":
    link = input("the playlist url plz: ")
    playlist = Pl(link)
    quality = input("lowest/highest: ")
    if quality == "lowest":
        for video in playlist.videos:
            print(f"the video title is: \n{video.title} \n--------------------------------")
            video.streams.get_lowest_resolution().download(output_path=path)
            video.register_on_complete_callback(finish())

    elif quality == "highest":
        for video in playlist.videos:
            print(f"the video title is: \n{video.title} \n--------------------------------")
            video.streams.get_highest_resolution().download(output_path=path)
            video.register_on_complete_callback(finish())

else:
    print("something wrong!")
