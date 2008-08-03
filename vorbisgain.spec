%define name    vorbisgain
%define version 0.37
%define release %mkrel 4
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


