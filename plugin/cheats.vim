if !has('python')
    finish
endif

function! OpenCheatSheet()
    pyfile /Users/varunrau/.vim/bundle/Cheats.vim/plugin/cheats.py
endfunction

function! OpenGeneralCheatSheet()
    pyfile /Users/varunrau/.vim/bundle/Cheats.vim/plugin/cheats_general.py
endfunction
