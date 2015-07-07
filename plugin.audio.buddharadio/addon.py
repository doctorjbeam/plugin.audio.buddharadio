import sys
import xbmcgui
import xbmcplugin
import os
import xbmcaddon


addon = xbmcaddon.Addon()

addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'audio')

addon_dir = addon.getAddonInfo('path')




url = os.path.join( addon_dir, 'resources', 'data', 'buddha.strm' )


li = xbmcgui.ListItem('Buddha Radio - Live Stream', iconImage='http://cdn.scahw.com.au/cdn-1cf89c9ffd45110/ImageVaultFiles/id_295202/cf_827/st_edited/aVx0G43hWLRdklwAC7Ll.png', thumbnailImage='http://whitenoisehq.co.uk/kisstory.png')
li.setProperty('fanart_image', 'http://2.bp.blogspot.com/-ue0Og71iPQs/UQ4o0Zi66AI/AAAAAAAACOo/sHE5cWYM2VE/s1600/Buddha+Bar+Compilation+Best+of+wallpaper+cover.jpg')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
xbmcplugin.endOfDirectory(addon_handle)