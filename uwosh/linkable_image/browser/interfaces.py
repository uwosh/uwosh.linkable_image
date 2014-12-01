##need my own browserlayer in order to overwrite IUWOshThemeLayer
from uwosh.themebase.browser.interfaces import IUWOshThemeLayer

class ILinkableImagesLayer(IUWOshThemeLayer):
    """
    Marker interface that defines a browser layer...subclass of IUWOshThemeLayer
    """
