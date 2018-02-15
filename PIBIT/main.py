import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

import sys
print(sys.getdefaultencoding())


from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.treeview import TreeViewNode
from kivy.uix.treeview import TreeView
from kivy.core.window import Window
from kivy.uix.treeview import TreeViewLabel
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton


class includeListButton(ListItemButton):
    selected_color =  [.8, .5, .7, 1]
    deselected_color = [.4, .5, .7, 1]
    pass

class customBox(BoxLayout):
    layout = BoxLayout(orientation='vertical')
    btn1 = Label(text='Hello')
    btn2 = Label(text='World')
    layout.add_widget(btn1)
    layout.add_widget(btn2)
    pass

class TreeViewCheck(customBox,TreeViewNode):
    orientation = "horizontal"
    height = 25
    pass

class TreeWidget(FloatLayout):
    def __init__(self, **kwargs):
        super(TreeWidget, self).__init__(**kwargs)
        tv = TreeView(root_options={'text':'CID-10'})
        tv.add_node(TreeViewLabel(text='My second item'))
        tv.add_node(TreeViewLabel(text='My first item'))
        tv.add_node(TreeViewLabel(text='My second item'))
        tv.add_node(TreeViewLabel(text='My first item'))
        tv.add_node(TreeViewLabel(text='My second item'))
        tv.add_node(TreeViewLabel(text='My first item'))
        tv.add_node(TreeViewLabel(text='My second item'))
        tv.add_node(TreeViewLabel(text='My first item'))
        tv.add_node(TreeViewLabel(text='My second item'))
        tv.add_node(TreeViewLabel(text='My first item'))
        tv.add_node(TreeViewLabel(text='My second item'))
        self.add_widget(tv)
    pass

class CidTree(Widget):
    tv = TreeView()
    pass


class Interface(BoxLayout):
    include_list = ObjectProperty()
    rule = ObjectProperty()

    def add_include(self):
        # Get the student name from the TextInputs
        rule_name = self.rule.text

        # Add the student to the ListView
        self.include_list.adapter.data.extend([rule_name])

        # Reset the ListView
        self.include_list._trigger_reset_populate()
        pass
    def delete_include(self):
        pass
    pass





class SelectTrialsApp(App):
    def build(self):
        #Window.clearcolor = (1,1,1,1)
        return Interface()

if __name__ == '__main__':
    SelectTrialsApp().run()