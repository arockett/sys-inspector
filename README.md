Runtime System Inspector
=============

Module for recording current system information while running a program.


The primary system inspecting is done by a Detective object.
Each Detective is tailored to collect standardized information about 
a specific type of operating system as well as any OS specific info.

The SystemInspector object contains the dictionary of attributes to
report. It is the object the user can interact with to add customized 
information to the attributes dictionary. The SystemInspector works
by choosing which Detective to use based on the operating system and
recording the standardized system attributes collected by the Detective.


** NOTE **
This Detective-SystemInspector relationship has not been set-up yet.
