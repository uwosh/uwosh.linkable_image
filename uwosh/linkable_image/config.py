from Products.CMFCore.permissions import setDefaultRoles

PRODUCT_NAME = "uwosh.linkable_image"

DEFAULT_ADD_CONTENT_PERMISSION = "Add portal content"
setDefaultRoles(DEFAULT_ADD_CONTENT_PERMISSION, ('Manager', 'Owner'))
ADD_CONTENT_PERMISSIONS = { 
    'LinkableImage': 'uwosh.linkable_image: Add Linkable Image',
 
}

setDefaultRoles('uwosh.linkable_image: Add Linkable Image', ('Manager'))
