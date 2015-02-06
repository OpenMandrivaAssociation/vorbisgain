%define name    vorbisgain
%define version 0.37
%define release 7
%define summary Adds tags to Ogg Vorbis files to adjust the volume

Summary:        %summary
Name:           %name
Version:        %version
Release:        %release
# GPLv2.1
License:        GPL
Group:          Sound
URL:            http://sjeng.sourceforge.net/vorbisgain.html

# http://sjeng.org/ftp/vorbis/vorbisgain-0.32.zip
Source0:        http://sjeng.org/ftp/vorbis/%name-%version.tar.bz2
Patch1:		%name-patch-configure.bz2
Patch2:		%name-fix-str-fmt.patch
BuildRoot:      %_tmppath/%name-buildroot
Buildrequires:  oggvorbis-devel libogg-devel


%description
VorbisGain is a utility that uses a psychoacoustic method to correct the
volume of an Ogg Vorbis file to a predefined standardized loudness.

It is meant as a replacement for the normalization that is commonly used
before encoding. Although normalization will ensure that each song has
the same peak volume, this unfortunately does not say anything about the
apparent loudness of the music, with the end result being that many
normalized files still don't sound equally loud. VorbisGain uses
psychoacoustics to address this deficiency. Moreover, unlike
normalization, it's a lossless procedure which works by adding tags to
the file. Additionally, it will add hints that can be used to prevent
clipping on playback. It is based upon the ReplayGain technology.

The end result is that the file ends up with superior playback quality
compared to a non-VorbisGain'ed file.

It needs player support to work. Non-supporting players will play back
the files without problems, but you'll miss out on the benefits.
Nowadays most good players such as ogg123 and mplayer are already
compatible. xmms will support this feature from release 1.2.8.


%prep
%setup -q
%patch1
%patch2 -p0

%build
%__chmod 755 configure
%configure --enable-recursive
%make


%install
rm -rf %buildroot
%makeinstall


%clean
rm -rf %buildroot


%files
%defattr(0755,root,root)
%_bindir/*
%defattr(0644,root,root,0755)
%doc NEWS  README
%_mandir/man1/*1*




%changelog
* Wed Oct 28 2009 RÃ©my Clouard <shikamaru@mandriva.org> 0.37-6mdv2010.0
+ Revision: 459826
- fix build (string format error)

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild
    - rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.37-3mdv2009.0
+ Revision: 255593
- rebuild

* Sat Mar 01 2008 Michael Scherer <misc@mandriva.org> 0.37-1mdv2008.1
+ Revision: 177313
- update to new version 0.37

  + Thierry Vignaud <tvignaud@mandriva.com>
    - fix spacing at top of description

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.36-1mdv2008.1
+ Revision: 129215
- kill re-definition of %%buildroot on Pixel's request
- do not hardcode man pages extension
- import vorbisgain


* Thu Jun 02 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.36-1mdk
- New release 0.36
- %%mkrel

* Thu Jun 02 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.34-3mdk
- Fix Source

* Mon Nov 08 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.34-2mdk
- rebuild

* Sun Oct 12 2003 Han Boetes <han@linux-mandrake.com> 0.34-1mdk
- Bump!

* Mon Apr 21 2003 Han Boetes <han@linux-mandrake.com> 0.32-3mdk
- Remove the patch again. OpenBSD-guru's say it's nonsense and
  vorbisgain segfaults.
- Added a patch to clean up configure

* Tue Mar 18 2003 Han Boetes <han@linux-mandrake.com> 0.32-2mdk
- added patches and updates that can also be found in the OpenBSD-port
- mplayer and ogg123 support this extension BTW :)

* Tue Mar  4 2003 Han Boetes <han@linux-mandrake.com> 0.32-1mdk
- This rpm works, the program works, just nothing supports it yet.
  We have to wait for xmms-1.2.8. Ow well. :)
