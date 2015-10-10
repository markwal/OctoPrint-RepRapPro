# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class RepRapProPlugin(octoprint.plugin.StartupPlugin):
	def _gcode_queuing(self, comm, phase, cmd, cmd_type, gcode, *args, **kwargs):
		if gcode is "M0" or gcode is "M1":
			eventManager().fire(Events.WAITING)
			comm._enqueue_for_sending(cmd, command_type=cmd_type)
			return None, # suppress further processing
		return None # proceed normally, no change


__plugin_name__ = "RepRapPro"

def __plugin_load__():
	global __plugin_implementation__
	plugin = RepRapProPlugin()
	__plugin_implementation__ = plugin

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.comm.protocol.gcode.queuing": plugin._gcode_queuing,
	}

