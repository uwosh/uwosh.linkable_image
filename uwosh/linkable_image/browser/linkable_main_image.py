from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from zope.component import getMultiAdapter
from Products.CMFCore.utils import getToolByName
from AccessControl import getSecurityManager
import random
from plone.memoize.instance import memoize
from uwosh.themebase.browser.viewlets.mainimage import MainImage

class LinkableMainImage(MainImage):
    render = ViewPageTemplateFile('linkable_image_viewlet.pt')


    def update(self):
        super(MainImage, self).update()

    @memoize
    def get_image_data(self):
        data = []
        for image in self.images:
            img_data = {'image_url' : image.absolute_url()}
            if image.portal_type == "LinkableImage":
                img_data['target'] = image.getNewWindow() and '_blank' or ''
                img_data['url'] = image.getRemoteUrl()
            data.append(img_data)
                
        return data

    @property
    @memoize
    def hasImages(self):
        return len(self.images) > 0

    @property
    @memoize
    def images(self):
        try:
            image_folder = self.context.unrestrictedTraverse('main-images')
        except:
            return []

        return [image_folder[id] for id in image_folder.objectIds() if image_folder[id].portal_type in ["Image", "LinkableImage"]]

    def javascript(self):

        return """
        <script type="text/javascript">
        var image_data = [%s];
        var selected = image_data[Math.round(Math.random()*(image_data.length-1))];
        var img = jq('<img src="' + selected.image_url + '" />');
        jq("#mainImage").append(img);
        if(selected.url != undefined){
            img.wrap('<a href="' + selected.url + '" target="' + selected.target + '" />');
        }
        </script>""" % ','.join([str(d) for d in self.get_image_data()])

