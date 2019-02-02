import sublime
import sublime_plugin


class SimpleWordCounter(sublime_plugin.EventListener):

    def on_selection_modified_async(self, view):
        word_count = self.count_words(view)

        display_string = ''
        if word_count == 1:
            display_string = str(word_count) + ' Word'
        elif word_count > 1:
            display_string = str(word_count) + ' Words'

        view.set_status('wordcount', display_string)

    def count_words(self, view):
        region = view.sel()[0]
        
        if region.begin() == region.end():
            return 0

        return len(view.substr(region).split())
