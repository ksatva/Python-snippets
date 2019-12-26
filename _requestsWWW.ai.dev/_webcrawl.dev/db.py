#place this file in _L3460parser too

db = {
   "Man_page" : "https://wiki.gentoo.org/wiki/Man_page" #Gentoo man page
   "unmask_package" :"", #"echo "sys-kernel/gentoo-sources-4.14.83::gentoo" >> /etc/portage/package.unmask"
   }


 dbsearchKeys = "package.accept_keywords" #in Man_page







#day notes
# change config /etc/portage/package.accept_keywords
"""TROUBLESHOOTING GENTOO UPDATE
emerge -cav skypeforlinux-8.30.0.50    #success
emerge --ask binutils-libs               #success
emerge --ask sys-kernel/linux-firmware   #success after dispatch-conf
emerge --ask sys-firmware/intel-microcode  #success after dispatch-conf
emerge --ask sys-kernel/gentoo-sources

emerge --ask app-text/poppler #success
emerge --ask dev-libs/icu #unsuccess
emerge --ask sys-libs/glibc #success
emerge --ask sys-devel/binutils #success NOTE:SECURITY THREAT
dev-qt/qtcore #unsuccess
dev-qt/linguist-tools

kde-plasma/kwin  #unsuccess
emerrge kde-frameworks/kxmlgui #unsuccess

libreoffice #unsuccess
emerge @preserved-rebuild #unsuccess # emerged the package individually 
emerge --info '=app-office/libreoffice-6.2.5.2::gentoo'

emerge -avuD system #=dev-qt/qtsvg-5.12.5 ~amd64
emerge -avuD world

emerge --update --changed-use --deep --quiet @world
emerge -av --depclean

#emerge -cav mupdf
emerge -cav app-accessibility/festival
#dev-libs/liborcus
TODO:
	emerge -cav linux-firmware
	or 
	emerge --ask sys-kernel/gentoo-sources
	
	emerge 


-------------------------------------
- sys-kernel/gentoo-sources-4.14.83::gentoo (masked by: linux-firmware license(s))
A copy of the 'linux-firmware' license is located at '/usr/portage/licenses/linux-firmware'.

- sys-kernel/linux-firmware-20181218::gentoo (masked by: linux-firmware no-source-code freedist license(s))
A copy of the 'no-source-code' license is located at '/usr/portage/licenses/no-source-code'.

A copy of the 'freedist' license is located at '/usr/portage/licenses/freedist'.

- media-libs/faac-1.29.9.2::gentoo (masked by: MPEG-4 license(s))
A copy of the 'MPEG-4' license is located at '/usr/portage/licenses/MPEG-4'.

- app-accessibility/speech-tools-2.1-r4::gentoo (masked by: FESTIVAL license(s))
- sys-devel/binutils-2.30-r4::gentoo (masked by: package.mask)
- app-editors/sublime-text-3_p3176::gentoo (masked by: Sublime license(s))
A copy of the 'Sublime' license is located at '/usr/portage/licenses/Sublime'.

- app-arch/unrar-5.6.6::gentoo (masked by: unRAR license(s))
A copy of the 'unRAR' license is located at '/usr/portage/licenses/unRAR'.

- sci-visualization/xgraph-12.1-r4::gentoo (masked by: xgraph license(s))
A copy of the 'xgraph' license is located at '/usr/portage/licenses/xgraph'.

For more information, see the MASKED PACKAGES section in the emerge
man page or refer to the Gentoo Handbook.


Would you like to merge these packages? [Yes/No] y
--------------------------

emerge --oneshot app-editors/sublime-text
emerge --oneshot app-accessibility/speech-tools
emerge --oneshot app-accessibility/festival
emerge --oneshot sci-visualization/xgraph
emerge --oneshot media-libs/faac


Project IDEA:
subject: trouble shoot system update issues
steps:
try to update
if success
   ok program executin complete
if fail
   input the log message
   parse text
   copy library names
   show to operator for analysis
   execute operator instructions
   Loop again
"""


"""ONESHOT PACKAGES 
##dependency:   dev-qt/qtcore
dev-qt/qtbluetooth-5.12.3::gentoo" [ebuild])
(dependency required by "dev-python/PyQt5-5.12.2::gentoo[bluetooth]" [ebuild])
(dependency required by "media-video/openshot-2.4.0-r1::gentoo"
"""