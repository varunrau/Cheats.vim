
vim.command("let my_filetype = &filetype")
filetype = vim.eval("my_filetype")
buffer_size = 30 #vim.command("exists(cheats_buffer_size)")
open_command = "%dvnew /Users/varunrau/.vim/bundle/Cheats.vim/plugin/cheatsheets/%s.cheats" % (buffer_size, filetype)
vim.command(open_command)
