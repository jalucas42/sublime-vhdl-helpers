import sublime
import sublime_plugin
import re

class VhdlPortDeclToSignalDeclCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		selection = self.view.sel()
		for region in selection:
			region_text = self.view.substr(region)
			lines_new = [];
			lines_orig = region_text.split("\n");
			for line in lines_orig:
				# Align comment lines
				line = re.sub(r'^\s*(--.*)$', r'  \1', line, flags=re.IGNORECASE);
				# Convert the ports to signals.
				# FIXME: Insert semicolon always, even if port doesn't have one.
				line = re.sub(r'^\s*([a-z0-9_]+\s*):\s*(?:IN|OUT|INOUT|BUFFER)\s+(.+)$', r'  \1: \2', line, flags=re.IGNORECASE);

				lines_new.append(line);
			
			self.view.replace(edit, region, "\n".join(lines_new));
			#print("\n".join(lines_new)); 
