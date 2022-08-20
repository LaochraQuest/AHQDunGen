#-*-coding:utf8;-*-
#################
#import libraries
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivy.properties import StringProperty
from kivymd.uix.list import OneLineAvatarListItem
from kivy.core.window import Window
from AHQ_func import passages
from AHQ_func import rooms
from AHQ_func import treasure
from AHQ_func import door_leads
##import webbrowser
#################


kv = """
Screen
    BoxLayout:
    
        orientation: 'vertical'
        MDTopAppBar:
            id: toolbar
            title: "Advanced HeroQuest Dungeon Generator"
            left_action_items: [["menu", lambda x: nav_draw.set_state()]]
            #set_headline_font_style: 'hq_gaze.ttf'  
            md_bg_color: 0.2, 0.2, 0.2, 1
            specific_text_color: 0.95, 0.95, 0.6, 1
        Widget:

    #################
    #Main Screen text
    
    MDLabel:
        text: ""
        id: txt
        markup: True
        theme_text_color: 'Custom'
        text_color: 0.9, 0.9, 0.6, 1
        font_size: 20
        pos_hint: {'center_x': 0.65, 'center_y': 0.58}
    MDRoundFlatButton:
        text: '    Passage     '
        pos_hint: {'center_x': 0.25, 'center_y': 0.08}
        font_name: 'hq_gaze.ttf'  
        font_size: "28sp"
        theme_text_color: "Custom"
        text_color: 0.9, 0.9, 0.6, 1
        line_color: 0.9, 0.9, 0.6, 1
        on_press:
            app.action('pas')
    MDRoundFlatButton:
        text: '     Room      '
        font_name: 'hq_gaze.ttf'  
        font_size: "28sp"
        theme_text_color: "Custom"
        text_color: 0.9, 0.9, 0.6, 1
        line_color: 0.9, 0.9, 0.6, 1
        pos_hint: {'center_x': 0.71, 'center_y': 0.08}
        on_press:
            app.action('room')
##            app.check_prev()#app.root.ids.check)

            
    MDIconButton:
        icon: "artflow_chest.png"
        #was 58sp
        icon_size: "54sp"
        #was 0.17, 0.21
        pos_hint: {'center_x': 0.18, 'center_y': 0.17}
        on_press:
            app.action('treasure')
    MDIconButton:
        icon: "artflow_door.png"
        #was 64sp
        icon_size: "60sp"
        #was 0.83, 0.2
        pos_hint: {'center_x': 0.78, 'center_y': 0.16}
        on_press:
            app.action('door')
##    MDFloatingActionButtonSpeedDial:
##        data: app.data
##        rotation_root_button: True


    ###############
    #Drawer

    MDNavigationDrawer:
        id: nav_draw
        orientation: "vertical"
        padding: "8dp"
        spacing: "8dp"
        
        AnchorLayout:
            anchor_x: "left"
            size_hint_y: None
            height: avatar.height
            
            Image:
                id: avatar
                size_hint: None, None
                size: "48dp", "48dp"
                source: "artflow_icon.png"


        MDLabel:
            markup: True
            text: "Dungeon Settings"
            #was 42
            font_size: 56    
            theme_text_color: 'Custom'
            text_color: 0.9, 0.9, 0.6, 1
            font_name: 'hq_gaze.ttf'  
            size_hint_y: None
            height: self.texture_size[1]                

##        ScrollView:
        MDList:

            #### Create new Quest
            OneLineAvatarListItem:
                markup: True
                #font was 32
                text: "[font=Caxton.ttf][size=44]New Quest[/font][/size]"     
                theme_text_color: 'Custom'
                text_color: 0.9, 0.9, 0.6, 1
                on_press:
                    app.action('reset_rms')
                    app.action('new')
                    nav_draw.set_state("close")
                IconLeftWidget:
                    icon: 'stairs.png'
                    #was 12
                    user_font_size: '10sp'
                    on_press:
                        app.action('reset_rms')
                        app.action('new')
                        nav_draw.set_state("close")


            #### HeroQuest Furniture
            TwoLineAvatarListItem:
                on_press: cb_furn._do_press()
                markup: True
                text: "[font=Caxton.ttf][size=44]Furniture[/font][/size]"
                secondary_text: "[font=Caxton.ttf][size=30]Use HeroQuest Furniture[/font][/size]"
                theme_text_color: 'Custom'
                text_color: 0.9, 0.9, 0.6, 1
                IconLeftWidget:
                    icon: 'bgr.png'
                    MDCheckbox:
                        active: True
                        id: cb_furn
                        size_hint: None, None
                        color_active: 0.9, 0.9, 0.6, 1
                        color_inactive: 0.9, 0.9, 0.6, 1
                        #size: "48dp", "48dp"
                        on_active:
                            app.action('furn')
            

            #### Terror in the Dark
            ThreeLineAvatarListItem:
                on_press: cb_ter._do_press()
                markup: True
                text: "[font=Caxton.ttf][size=44]Quest Rooms[/font][/size]"
                secondary_text: "[font=Caxton.ttf][size=30]Use Terror in the Dark quest[/font][/size]"
                tertiary_text: "[font=Caxton.ttf][size=30]rooms likelihood table[/font][/size]"
                theme_text_color: 'Custom'
                text_color: 0.9, 0.9, 0.6, 1
                IconLeftWidget:
                    icon: 'bgr.png'
                    MDCheckbox:
                        active: True
                        id: cb_ter
                        size_hint: None, None
                        color_active: 0.9, 0.9, 0.6, 1
                        color_inactive: 0.9, 0.9, 0.6, 1
                        #size: "48dp", "48dp"
                        on_active:
                            app.action('ter')


            ##### Previously Encountered
            OneLineAvatarListItem:
                markup: True
                text: "[font=Caxton.ttf][size=44]Characters encountered[/font][/size]"     
                on_press: app.show_chars_dialog()
                theme_text_color: 'Custom'
                text_color: 0.9, 0.9, 0.6, 1
##                divider: 'Inset'
                IconLeftWidget:
                    id: enc
                    icon: 'encounter.png'
                    user_font_size: '10sp' 
                    on_release:
                        app.show_chars_dialog()

                       

            #### Room counter
            TwoLineAvatarListItem:
##                on_press:
##                    nav_draw.set_state("close")
                markup: True
                text: "[font=Caxton.ttf][size=44]Number of rooms[/font][/size]"     
                secondary_text: "[font=Caxton.ttf][size=30]Tap number to reset[/font][/size]"
                theme_text_color: 'Custom'
                text_color: 0.9, 0.9, 0.6, 1
                IconLeftWidget:
                    icon: 'bgr.png'
                    on_press:
                        app.action('reset_rms')
##                        nav_draw.set_state("close")
                    MDLabel:
                        markup: True
                        text: "  0"
                        id: n_rms
                        font_size: 40    
                        theme_text_color: 'Custom'
                        text_color: 0.9, 0.9, 0.6, 1
                        font_name: 'hq_gaze.ttf'  
                        size_hint_y: None
                        #height: self.texture_size[1]



            ##### Website
            OneLineAvatarListItem:
                on_press:
                    import webbrowser
                    #webbrowser.open('https://ko-fi.com/ahqdungeon')
                    webbrowser.open('https://laochraquest.github.io/Taverne/')
                    nav_draw.set_state("close")
                markup: True
                text: "[font=Caxton.ttf][size=44]The Taverne[/font][/size]"     
                theme_text_color: 'Custom'
                text_color: 0.9, 0.9, 0.6, 1
                IconLeftWidget:
                    icon: "ale.png"
                    on_press:
                        import webbrowser
                        #webbrowser.open('https://ko-fi.com/ahqdungeon')
                        webbrowser.open('https://laochraquest.github.io/Taverne/')

                
                            
        Widget:
        
    #End drawer
    ##############


<ItemSelect>
    
    CheckboxLeftWidget:
        id: check
        char: root.text
        source: root.source
        color_active: 0.9, 0.9, 0.6, 1
        color_inactive: 0.9, 0.9, 0.6, 1
        theme_text_color: 'Custom'
        text_color: 0.9, 0.9, 0.6, 1        
        check: app.check_prev(check)
        on_active:
            app.on_checkbox_active(root.source,*args)

"""

chars = set()
room_count = 0
Terror = True
Furniture = True

class ItemSelect(OneLineAvatarListItem):
    divider = None
    source = StringProperty()


class MyApp(MDApp):
    dialog = None
    
    def on_start(self):
        #This changes the Toolbar font
        self.root.ids.toolbar.ids.label_title.font_name = "hq_gaze.ttf"
        self.root.ids.toolbar.ids.label_title.font_size = '28sp'

    def action(self,obj):
        #label = self.root.ids.txt
        #text = "This text is displayed after pressing button"

        #My phone
##        head = "50"
##        fs = "30"
        head = "60"
        fs = "40"
        
        global room_count
        global chars
        global Terror
        global Furniture
        
        if obj == 'pas':
            text = "[font=hq_gaze.ttf][size="+head+"][b]Passages[/b][/size][/font]\n\n\n[font=Caxton.ttf][size="+fs+"]"+passages()+"[/size][/font]"
            self.root.ids.txt.text=text
        if obj == 'room':
            rms = rooms(room_count,terror=Terror,chars=chars,furniture=Furniture)
            room_count += rms[0]
            text = "[font=hq_gaze.ttf][size="+head+"][b]Rooms[/b][/size][/font]\n\n\n[font=Caxton.ttf][size="+fs+"]"+rms[1]+"[/size][/font]\n"
            self.root.ids.txt.text=text
            #update room counter
            if room_count < 10:
                rcount = "  "+str(room_count)
            if 9 <  room_count < 100:
                rcount = " "+str(room_count)
            if room_count >= 100:
                rcount = str(room_count)
            self.root.ids.n_rms.text=rcount
        if obj == 'treasure':
            text="[font=hq_gaze.ttf][size="+head+"][b]Treasure[/b][/size][/font]\n\n\n[font=Caxton.ttf][size="+fs+"]"+treasure()+"[/size][/font]\n\n"
            self.root.ids.txt.text=text
        if obj == 'door':
            text="[font=hq_gaze.ttf][size="+head+"][b]Door[/b][/size][/font]\n\n\n[font=Caxton.ttf][size="+fs+"]"+door_leads()+"[/size][/font]\n\n"
            self.root.ids.txt.text=text

        if obj == 'ter':
            Terror = not Terror

        if obj == 'reset_rms':
            room_count = 0
            self.root.ids.n_rms.text= '  0'
            
        if obj == 'new':
            room_count = 0
            self.root.ids.n_rms.text= '  0'
            self.root.ids.txt.text= ''

        if obj == 'furn':
            Furniture = not Furniture



    def build(self):
##        Window.size = [540, 1080]
        self.theme_cls.theme_style = "Dark"  # "Light"
        return Builder.load_string(kv)


    def show_chars_dialog(self):
        
##        if not self.dialog:
        self.dialog = MDDialog(
            title="[font=hq_gaze.ttf]Have the Heroes encountered:[/font]",
            type="confirmation",
##                content_cls=ItemSelect(),
            items=[
                ItemSelect(text="[font=Caxton.ttf]Maiden[/font]",source='maiden'),
                ItemSelect(text="[font=Caxton.ttf]Witch[/font]",source='witch'),
                ItemSelect(text="[font=Caxton.ttf]Rogue[/font]",source='rogue'),
                ItemSelect(text="[font=Caxton.ttf]Man-at-Arms[/font]",source='henchman'),
            ],
##                buttons=[
##                    MDFlatButton(
##                        text="OK"
##                    ),
##                ],
        )
            
##        for i in self.dialog.items:
##            if i.source in chars:
##                i.state = 'down'
##            else:
##                i.state = 'normal'
##            print(chars, i.source, i.state)
        
        self.dialog.open()

    def check_prev(self, checkbox):
##        print(checkbox.active, checkbox.char, checkbox.source)
        if len(chars) > 0:
            for char in chars:
                #ch = "[font=Caxton.ttf]" + char[0].upper() + char[1:] + "[/font]"
                if checkbox.source == char and checkbox.state == 'normal':
                    checkbox.state = 'down'

    def on_checkbox_active(self, ch, checkbox, value):
##        ch = checkbox.char.split(']')[1].split('[')[0].lower()
        if checkbox.state == 'down':
            chars.add(ch)
        if checkbox.state == 'normal':
            chars.remove(ch)
##        print("click",chars)

    
if __name__ == '__main__':
    MyApp().run() 
