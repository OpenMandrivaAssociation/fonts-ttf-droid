%define pkgname droid-font
%define _fontdir %{_datadir}/fonts/TTF/droid

Name: fonts-ttf-droid
Summary: The Droid family of fonts
Version: 1.0
Release: %mkrel 1
License: Apache2
Group: System/Fonts/True type
URL: http://www.droidfonts.com/
Source: %{pkgname}.tar.gz
BuildRequires: freetype-tools
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The Droid family of fonts consists of Droid Sans, Droid Sans Mono and
Droid Serif. Each contains extensive character set coverage including
Western Europe, Eastern/Central Europe, Baltic, Cyrillic, Greek and
Turkish support. The Droid Sans regular font also includes support for
Simplified and Traditional Chinese, Japanese and Korean support for
the GB2312, Big 5, JIS 0208 and KSC 5601 character sets respectively.

%prep
%setup -q -n droid

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_fontdir}
install -m 644 *.ttf %{buildroot}%{_fontdir}
ttmkfdir %{buildroot}%{_fontdir} > %{buildroot}%{_fontdir}/fonts.dir
ln -s fonts.dir %{buildroot}%{_fontdir}/fonts.scale
mkdir -p %{buildroot}%{_sysconfdir}/X11/fontpath.d/
ln -s ../../..%{_fontdir} \
	%{buildroot}%{_sysconfdir}/X11/fontpath.d/ttf-droid:pri=50

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE
%dir %{_fontdir}
%{_fontdir}/*.ttf
%verify(not mtime) %{_fontdir}/fonts.dir
%{_fontdir}/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-droid:pri=50
