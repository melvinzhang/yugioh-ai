from babel.dates import format_time

from ..channel import Channel, NO_SEND_CHECK

class Watchers(Channel):
	def __init__(self):
		Channel.__init__(self, flags = NO_SEND_CHECK)
	
	def is_enabled(self, recipient):
		return recipient.watch
	
	def format_message(self, recipient, sender, message, params):
		return recipient._(message).format(player = sender.nickname)
	
	def format_history_message(self, recipient, buffer_entry):
		return format_time(buffer_entry['time'], format='short', locale=self.get_locale_for_recipient(recipient))+" - "+recipient._(buffer_entry['message']).format(buffer_entry['sender'])
