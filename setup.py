# -*- coding: UTF-8 -*-
from . import _, config_root, PLUGIN_BASE, PLUGIN_VERSION

from Screens.Screen import Screen
from Components.ActionMap import ActionMap
from Components.ConfigList import ConfigListScreen
from Components.config import config, getConfigListEntry
from Components.Button import Button
from Components.Label import Label

class SetupWindow(Screen, ConfigListScreen):

    skin="""
        <screen css="full_screen" title="openHAB client setup">
		<eLabel position="675,140" size="430,35" text="openHAB setup" font="Regular;28" transparent="1" zPosition="2" runningLine="2" />
		<eLabel position="665,180" size="450,2" backgroundColor="white" zPosition="2" />
		<widget position="650,195" size="510,410" name="config" css="menu_w485h50i50w" zPosition="2" />
		<ePixmap css="button_pix_red" />
		<ePixmap css="button_pix_green" />
		<ePixmap css="button_pix_yellow" />
		<ePixmap css="button_pix_blue" />
		<widget name="key_red" css="button_red" />
		<widget name="key_green" css="button_green" />
        </screen>"""

    def __init__(self, session):
        Screen.__init__(self, session)
        self.list = [
            getConfigListEntry(_("Host"), config_root.host),
            getConfigListEntry(_("Port"), config_root.port),
            getConfigListEntry(_("User"), config_root.user),
            getConfigListEntry(_("Password"), config_root.password),
            getConfigListEntry(_("Sitemap"), config_root.sitemap),
            getConfigListEntry(_("Refresh interval"), config_root.refresh),
            getConfigListEntry(_("Dimmer step"), config_root.dimmer_step),
            getConfigListEntry(_("Slider style"), config_root.graphic_sliders),
            getConfigListEntry(_("Enable debug"), config_root.debug),
        ]
        ConfigListScreen.__init__(self, self.list)
        
        self["config"].list = self.list
        self["info"] = Label(_("Plugin: %(name)s, Version: %(version)s") % dict(name=PLUGIN_BASE, version=PLUGIN_VERSION))

        self["key_red"] = Button(_("Cancel"))
        self["key_green"] = Button(_("Save"))
        self["key_yellow"] = Button(" ")
        self["key_blue"] = Button(" ")

        self["setupActions"] = ActionMap(["SetupActions", "ColorActions"],
        {
            "save": self.save,
            "green": self.save,
            "cancel": self.cancel,
            "red": self.cancel,
        }, -2)

    def save(self):
        self.saveAll()
        self.close(True)

    def cancel(self):
        for x in self["config"].list:
            x[1].cancel()
        self.close(False)
