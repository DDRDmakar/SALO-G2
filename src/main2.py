
import urwid

salo_g2_logo = (
'''                                                       
    ######        ######      ##              ######   
  ##      ##    ##      ##    ##            ##      ## 
  ##            ##      ##    ##            ##      ## 
    ######      ##      ##    ##            ##      ## 
          ##    ##########    ##            ##      ## 
  ##      ##    ##      ##    ##            ##      ## 
    ######      ##      ##    ##########      ######   
                                                        
                           
    ######        ######   
  ##      ##    ##      ## 
  ##                    ## 
  ##  ######          ##   
  ##      ##        ##     
  ##      ##      ##       
    ######      ########## 
                           ''')

class EditCom(urwid.Edit):
	_metaclass_ = urwid.signals.MetaSignals  
	signals = ['done']
	def keypress(self, size, key):
		if key == 'enter':
			urwid.emit_signal(self, 'done', self, self.get_edit_text()) #if you dont need a reference to the CustomEdit instance you can drop the 3rd argument
			super(EditCom, self).set_edit_text('')
			return
		elif key == 'esc':
			super(EditCom, self).set_edit_text('')
			return
		urwid.Edit.keypress(self, size, key)

#class MyListBox(urwid.ListBox):
	#all_children_visible = True
	
	#def keypress(self, size, *args, **kwargs):
		#self.all_children_visible = self._compute_all_children_visible(size)
		#return super(MyListBox, self).keypress(size, *args, **kwargs)
	
	#def mouse_event(self, size, *args, **kwargs):
		#self.all_children_visible = self._compute_all_children_visible(size)
		#return super(MyListBox, self).mouse_event(size, *args, **kwargs)
	
	#def render(self, size, *args, **kwargs):
		#self.all_children_visible = self._compute_all_children_visible(size)
		#return super(MyListBox, self).render(size, *args, **kwargs)
	
	#def _compute_all_children_visible(self, size):
		#n_total_widgets = len(self.body)
		#middle, top, bottom = self.calculate_visible(size)
		#n_visible = len(top[1]) + len(bottom[1])
		#if middle:
			#n_visible += 1
		#return n_total_widgets == n_visible

class LogListBox(urwid.ListBox):
	all_children_visible = True
	
	def keypress(self, size, *args, **kwargs):
		self.all_children_visible = self._compute_all_children_visible(size)
		return super(LogListBox, self).keypress(size, *args, **kwargs)
	
	def mouse_event(self, size, *args, **kwargs):
		self.all_children_visible = self._compute_all_children_visible(size)
		return super(LogListBox, self).mouse_event(size, *args, **kwargs)
	
	def render(self, size, *args, **kwargs):
		self.all_children_visible = self._compute_all_children_visible(size)
		return super(LogListBox, self).render(size, *args, **kwargs)
	
	def _compute_all_children_visible(self, size):
		n_total_widgets = len(self.body)
		middle, top, bottom = self.calculate_visible(size)
		n_visible = len(top[1]) + len(bottom[1]) + (1 if middle else 0)
		if n_total_widgets > n_visible:
			for i in range(n_total_widgets - n_visible):
				self.body.pop(0)
		return n_total_widgets == n_visible

class User_interface(object):
	
	def __init__(self):
		self.log = urwid.SimpleListWalker([urwid.Text(salo_g2_logo)])
		self.log_box = LogListBox(self.log)
		self.log_linebox = urwid.LineBox(self.log_box)
		
		self.com_text = EditCom('> ')
		urwid.connect_signal(self.com_text, 'done', self.on_command)
		
		self.top = urwid.Frame(
			self.log_linebox, footer=self.com_text, focus_part='footer'
		)
	
	def on_command(self, edit, new_edit_text):
		self.log.append(urwid.Text(new_edit_text))
		#if not self.log_box.all_children_visible:
		#	self.log.pop(0)

user_interface = User_interface()
urwid.MainLoop(user_interface.top).run()
