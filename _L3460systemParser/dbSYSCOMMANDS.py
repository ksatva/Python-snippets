

db = {
"list all installed libraries" : "qlist -IRv",
"sync ebuilds from web" : "emerge-webrsync",
"Updates portage tree with the latest ebuilds" : "emerge --sync",
"Upgrade all installed packages" : "emerge -uDU --keep-going --with-bdeps=y @world",
"Upgrade world" : "emerge -avuD world",
"Upgrade system" : "emerge -avuD system",
"Updates config files" : "dispatch-conf",
"Install outside world" : "emerge --oneshot ", #emerge --oneshot package-name
#"Install outside world" : "emerge -1", # emerge -1 package-name
"remove a package" : "emerge -cav ",
"force remove package" : "emerge -C ",
"Before removing unnessary packages" : "emerge --update --newuse --deep --quiet @world"
"Remove unnessary packages" : "emerge -av --depclean",
"Check and rebuild missing libraries" : "revdep-rebuild -v",
"After updating perl core" : "perl-cleaner --all",
"update haskell" : "haskell-updater",
"" : "",
"" : "",
"" : "",
"" : "",
"" : "",
"" : "",
"" : "",
"" : "",
"" : "",
"" : "",
"" : "",
"" : "",
"" : "",
"" : "",
"" : "",
"" : "",
"" : "",
"" : "",
"" : "",
"" : "",
"" : ""
}