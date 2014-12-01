from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
import interfaces
from uwosh.linkable_image.config import *
from Products.ATContentTypes.content.image import ATImage, ATImageSchema
from Products.ATContentTypes.content.link import ATLink, ATLinkSchema

copied_fields = {}

copied_fields['remoteUrl'] = ATLinkSchema['remoteUrl'].copy()
copied_fields['remoteUrl'].default = ''
copied_fields['remoteUrl'].primary = False
copied_fields['remoteUrl'].required = True
copied_fields['remoteUrl'].widget.description = "Where the image will link to"
copied_fields['remoteUrl'].widget.label = "URL"

schema = Schema((

    copied_fields['remoteUrl'],

    BooleanField(
        name='newWindow',
        widget=BooleanWidget(
           label='Open in new window?',
           description='Should the link attached to this image open in a new window?',
        ),
        default=False,
        schemata='default',
    ),

)
)

LinkableImageSchema = ATImageSchema.copy() + schema.copy()

class LinkableImage(ATImage):
    """
    
    """
    
#     assocMimetypes = ('application/*', 'audio/*', 'video/*', )
#     assocFileExt   = ('mp3', 'flv', 'mov', 'swf')
    
    security = ClassSecurityInfo()

    implements(interfaces.ILinkableImage)
    
    archetype_name = 'LinkableImage'
    meta_type = 'LinkableImage'
    portal_type = "LinkableImage"
    _at_rename_after_creation = True

    schema = LinkableImageSchema
    
    
registerType(LinkableImage, PRODUCT_NAME)
