Summary:	Adds tags to Ogg Vorbis files to adjust the volume
Name:		vorbisgain
Version:	0.37
Release:	9
License:	GPLv2+
Group:		Sound
Url:		http://sjeng.sourceforge.net/vorbisgain.html
# http://sjeng.org/ftp/vorbis/vorbisgain-0.32.zip
Source0:	http://sjeng.org/ftp/vorbis/%{name}-%{version}.tar.gz
Patch1:		vorbisgain-patch-configure.patch
Patch2:		vorbisgain-fix-str-fmt.patch
BuildRequires:	pkgconfig(ogg)
BuildRequires:	pkgconfig(vorbis)

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

%files
%doc NEWS README
%{_bindir}/*
%{_mandir}/man1/*1*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch1 -p0
%patch2 -p0

%build
chmod 755 configure
%configure --enable-recursive
%make_build

%install
%make_install

