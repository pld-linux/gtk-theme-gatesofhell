Summary:	Look & Feel of Win2k for GTK+
Summary(pl.UTF-8):	Motyw Win2k dla GTK+
Name:		gtk-theme-gatesofhell
Version:	0.1
Release:	2
License:	GPL
Group:		Themes/GTK+
Source0:	http://www.iceflow.net/themes/gatesofhell.tar.gz
# Source0-md5:	4729e318e956f9832d03c6ce4173a5b1
URL:		http://www.iceflow.net/themes/
BuildRequires:	gtk+-devel
Requires:	gtk-engines
# KLOCZEK: jak bedziesz zmienial to i to requires zmien
Requires:	gtk-theme-ThinIce
Requires:	gtk-theme-engine-Xenophilia
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This theme is a work in progress with the ultimate goal of cloning the
look and feel of the Win2k widgets. In order to get the look as close
as possible I made use of multiple theme engines that do not use
pixmaps(for speed reasons).

%description -l pl.UTF-8
Ten motyw ma za zadanie sklonować wygląd i sposób pracy widgetów
Win2k.

%prep
%setup  -q -n Gatesofhell

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/themes/GatesOfHell

install gtk/gtkrc $RPM_BUILD_ROOT%{_datadir}/themes/GatesOfHell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/themes/GatesOfHell
