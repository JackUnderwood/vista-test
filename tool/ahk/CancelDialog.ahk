#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
#Warn  ; Enable warnings to assist with detecting common errors.

; Cancel the dialog
#SingleInstance force
#IfWinActive indytest says:
^y::
	SendInput, {TAB}{ENTER}
Return
#IfWinActive
