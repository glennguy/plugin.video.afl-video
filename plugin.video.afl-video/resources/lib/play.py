#
#    AFL Video XBMC Plugin
#    Copyright (C) 2012 Andy Botting
#
#    AFL Video is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    AFL Video is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with AFL Video.  If not, see <http://www.gnu.org/licenses/>.
#

import sys, re
import classes, config, utils, comm
import xbmc, xbmcgui, xbmcplugin, xbmcaddon


def play(url):

	params = utils.get_url(url)
	print params
	video_id = params['id']

	# Show a dialog
	d = xbmcgui.DialogProgress()
	d.create(config.NAME, '')
	d.update(20, 'Fetching video parameters...')

	try:
		d.update(50, 'Fetching video URL...')
		v = comm.get_video(video_id)

		listitem = xbmcgui.ListItem(label=v.get_title(), iconImage=v.get_thumbnail(), thumbnailImage=v.get_thumbnail())
		listitem.addStreamInfo('video', v.get_xbmc_stream_info())
		listitem.setInfo('video', v.get_xbmc_list_item())
	
		d.update(99, 'Starting video...')
		xbmc.Player().play(v.get_url(), listitem)
	except:
		# user cancelled dialog or an error occurred
		d = xbmcgui.Dialog()
		message = utils.dialog_error("Unable to play video")
		d.ok(*message)
		utils.log_error();
