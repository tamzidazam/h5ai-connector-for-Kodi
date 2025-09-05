# -*- coding: utf-8 -*-
import xbmcaddon

__addon__ = xbmcaddon.Addon()

def get_setting(setting_id):
    """
    Gets a setting value from settings.xml

    :param setting_id: The id of the setting to get.
    :type setting_id: str
    :return: The value of the setting.
    :rtype: str
    """
    return __addon__.getSetting(setting_id)

def set_setting(setting_id, value):
    """
    Sets a setting value in settings.xml

    :param setting_id: The id of the setting to set.
    :type setting_id: str
    :param value: The value to set.
    :type value: str
    """
    __addon__.setSetting(setting_id, value)
