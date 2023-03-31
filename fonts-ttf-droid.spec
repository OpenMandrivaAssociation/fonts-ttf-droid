%define pkgname droid-fonts

Summary:	Droid Fonts
Name:		fonts-ttf-droid
Version:	1.0
Release:	22
License:	Apache License
Group:		System/Fonts/True type
Url:		http://www.droidfonts.com/
Source0:	%{pkgname}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	fontconfig
BuildRequires:	freetype-tools

%description
The Droid family of fonts consists of Droid Sans, Droid Sans Mono and 
Droid Serif. Each contains extensive character set coverage including 
Western Europe, Eastern/Central Europe, Baltic, Cyrillic, Greek and 
Turkish support. The Droid Sans regular font also includes support for 
Simplified and Traditional Chinese, Japanese and Korean support for 
the GB2312, Big 5, JIS 0208 and KSC 5601 character sets respectively. 
Droid was designed by Ascender's Steve Matteson to provide optimal quality 
and comfort on a mobile handset when rendered in application menus, web 
browsers and for other screen text. 

%prep
%setup -qn %{pkgname}-%{version}

%build

%install
mkdir -p %{buildroot}%{_datadir}/fonts/TTF/droid

install -m 644 *.ttf %{buildroot}%{_datadir}/fonts/TTF/droid
ttmkfdir %{buildroot}%{_datadir}/fonts/TTF/droid > %{buildroot}%{_datadir}/fonts/TTF/droid/fonts.dir
ln -s fonts.dir %{buildroot}%{_datadir}/fonts/TTF/droid/fonts.scale

mkdir -p %{buildroot}%{_sysconfdir}/X11/fontpath.d/
ln -s ../../..%{_datadir}/fonts/TTF/droid \
	%{buildroot}%{_sysconfdir}/X11/fontpath.d/ttf-droid:pri=50

%files
%doc README COPYING AUTHORS
%dir %{_datadir}/fonts/TTF/droid
%{_datadir}/fonts/TTF/droid/*.ttf
%verify(not mtime) %{_datadir}/fonts/TTF/droid/fonts.dir
%{_datadir}/fonts/TTF/droid/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-droid:pri=50

