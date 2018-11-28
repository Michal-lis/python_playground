from abc import ABC, abstractmethod


class SongComponent(ABC):
    # instead of @abstractclass we  use NotImplementedError
    def add(self, song_component):
        raise NotImplementedError

    def remove(self, song_idx):
        raise NotImplementedError

    def get(self, component_index):
        raise NotImplementedError

    def get_name(self):
        raise NotImplementedError

    def get_band_name(self):
        raise NotImplementedError

    def get_release_year(self):
        raise NotImplementedError

    def display_song_info(self):
        raise NotImplementedError


class SongGroup(SongComponent):
    def __init__(self, group_name, group_description):
        self.song_components = []
        self.group_name = group_name
        self.group_desciption = group_description

    def get_group_descption(self):
        return self.group_desciption

    def get_group_name(self):
        return self.group_name

    def add(self, song_component):
        self.song_components.append(song_component)

    def remove(self, song_idx):
        try:
            del (self.song_components[song_idx])
        except IndexError:
            print("there are not that many elements in you list!")

    def get(self, song_idx):
        try:
            return self.song_components[song_idx]
        except IndexError:
            print("there are not that many elements in you list!")

    def display_song_info(self):
        print(self.group_desciption + " " + self.group_name)
        for e in self.song_components:
            e.display_song_info()


class Song(SongComponent):

    def __init__(self, song_name, band_name, release_year) -> None:
        self.song_name = song_name
        self.band_name = band_name
        self.release_year = release_year

    def get_name(self):
        return self.song_name

    def get_band_name(self):
        return self.band_name

    def get_release_year(self):
        return self.release_year

    def display_song_info(self):
        print(f'{self.song_name}, {self.band_name}, {self.release_year}')


a = SongGroup('brit top', 'Most popular british music')
b = SongGroup('pop', 'nothing more than typical pop music')
c = Song('Franz Ferdinand', 'Devils Eye', 1994)
a.add(b)
b.add(c)
a.display_song_info()
