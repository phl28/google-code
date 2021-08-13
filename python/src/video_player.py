"""A video player class."""

from src.video import Video
from .video_library import VideoLibrary
from .video_playlist import Playlist
import random

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._current_vid = None
        self._paused = False
        self._playlists = {}

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        
        print("Here's a list of all available videos:")
        for video in sorted(self._video_library.get_all_videos(), key = lambda x: x._title):
            print("{} ({}) [{}]".format(video.title, video.video_id, video.tags))
        
        # print("show_all_videos needs implementation")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        
        video = self._video_library.get_video(video_id)
        if video is None:
            print("Cannot play video: Video does not exist")
            return 
        if self._current_vid:
            self.stop_video()
        print("Playing video: {}".format(video.title))  
        self._current_vid = video      
        
        # print("play_video needs implementation")

    def stop_video(self):
        """Stops the current video."""
        
        if self._current_vid is None:
            print("Cannot stop video: No video is currently playing")
            return 
        print("Stopping video: {}".format(self._current_vid.title))
        self._current_vid = None
        self._paused = False
        
        # print("stop_video needs implementation")

    def play_random_video(self):
        
        """Plays a random video from the video library."""
        if self._current_vid:
            self.stop_video()
        videos = [v for v in self._video_library.get_all_videos()]
        self.play_video(random.choice(videos).video_id)
        
        # print("play_random_video needs implementation")

    def pause_video(self):
        """Pauses the current video."""
        
        if self._paused:
            print("Video already paused: {}".format(self._current_vid.title))
            return 
        if self._current_vid is None:
            print("Cannot pause video: No video is currently playing")
            return 
        print("Pausing video: {}".format(self._current_vid.title))
        self._paused = True
        
        # print("pause_video needs implementation")

    def continue_video(self):
        """Resumes playing the current video."""
        
        if self._current_vid is None:
            print("Cannot continue video: No video is currently playing")
            return 
        elif self._paused == False:
            print("Cannot continue video: Video is not paused")
            return 
        self._paused = False
        print("Continuing video: {}".format(self._current_vid.title))
        
        # print("continue_video needs implementation")

    def show_playing(self):
        """Displays video currently playing."""
        
        if self._current_vid is not None:
            msg = "Currently playing: {} ({}) {}".format(self._current_vid.title, self._current_vid.video_id, self._current_vid.tags)
            if self._paused:
                msg += " - PAUSED"
        else:
            msg = "No video is currently playing"
        print(msg)

        # print("show_playing needs implementation")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        if playlist_name.lower() in self._playlists:
            print("Cannot create playlist: A playlist with the same name already exists")
            return 
        print("Successfully created new playlist: {}".format(playlist_name))
        self._playlists[playlist_name.lower()] = Playlist(playlist_name)

        # print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """

        video = self._video_library.get_video(video_id)
        if playlist_name.lower() not in self._playlists:
            print("Cannot add video to {}: Playlist does not exist".format(playlist_name))
            return
        if video is None:
            print("Cannot add video to {}: Video does not exist".format(playlist_name))
            return     
        playlist = self._playlists[playlist_name.lower()]
        if video in playlist.videos:
            print("Cannot add video to {}: Video already added".format(playlist_name))
            return  
        
        playlist.videos.append(video)
        print("Added video to {}: {}".format(playlist_name, video.title))

        # print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""
        if not self._playlists:
            print("No playlists exist yet")
            return 
        print("Showing all playlists:")
        for playlist in sorted(self._playlists):
            print(f"{self._playlists[playlist].name}")
        # print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() not in self._playlists:
            print("Cannot show playlist {}: Playlist does not exist".format(playlist_name))
            return 
        print("Showing playlist: {}".format(playlist_name))
        playlist = self._playlists[playlist_name.lower()]
        if not playlist.videos:
            print("No videos here yet")
            return 
        for video in playlist.videos:
            print(video)

        # print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """

        if playlist_name.lower() not in self._playlists:
            print("Cannot remove video from {}: Playlist does not exist".format(playlist_name))
            return 
        video = self._video_library.get_video(video_id)
        playlist = self._playlists[playlist_name.lower()]
        if video is None:
            print("Cannot remove video from {}: Video does not exist".format(playlist_name))
            return 
        if video not in playlist.videos:
            print("Cannot remove video from {}: Video is not in playlist".format(playlist_name))
            return 
        print("Removed video from {}: {}".format(playlist_name, video.title))
        playlist.videos.remove(video)

        # print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        if playlist_name.lower() not in self._playlists:
            print("Cannot clear playlist {}: Playlist does not exist".format(playlist_name))
            return 
        playlist = self._playlists[playlist_name.lower()]
        playlist.videos.clear()
        print("Successfully removed all videos from {}".format(playlist_name))

        # print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        if playlist_name.lower() not in self._playlists:
            print("Cannot delete playlist {}: Playlist does not exist".format(playlist_name))
            return 
        print("Deleted playlist: {}".format(playlist_name))
        self._playlists.pop(playlist_name.lower())

        # print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """

        results = []
        for video in self._video_library.get_all_videos():
            if search_term.lower() in video.title.lower():
                results.append(video)
        if not results:
            print("No search results for {}".format(search_term))
            return 
        print("Here are the results for {}:".format(search_term))
        for i, result in enumerate(results):
            print("{}) {}".format(i+1, result))
        print("Would you like to play any of the above? If yes, specify the number of the video.")
        print("If your answer is not a valid number, we will assume it's a no.")
        answer = input()
        if answer.isnumeric() and 0 <= int(answer) <= len(results):
            self.play_video(results[int(answer) - 1].video_id)

        # print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        
        results = []
        for video in self._video_library.get_all_videos():
            if video_tag.lower() in video.tags:
                results.append(video)
        if not results:
            print("No search results for {}".format(video_tag))
            return 
        print("Here are the results for {}:".format(video_tag))
        for i, result in enumerate(results):
            print("{}) {}".format(i+1, result))
        print("Would you like to play any of the above? If yes, specify the number of the video.")
        print("If your answer is not a valid number, we will assume it's a no.")
        answer = input()
        if answer.isnumeric() and 0 <= int(answer) <= len(results):
            self.play_video(results[int(answer) - 1].video_id)
        
        # print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        if flag_reason == "" : 
            flag_reason += "Not supplied"
        video = self._video_library.get_video(video_id)
        print("Successfully flagged video: {} (reason: {})".format(video.title, flag_reason))

        # print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """



        # print("allow_video needs implementation")
