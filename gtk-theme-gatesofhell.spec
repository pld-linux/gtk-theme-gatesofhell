Summary:	Look & Feel of Win2k for GTK
Summary(pl):	Temat Win2k dla GTK
Name:		gtk-theme-gatesofhell
Version:	0.1
Release:	1
License:	GPL
Group:		Themes/Gtk
Group(de):	Themen/Gtk
Group(pl):	Motywy/Gtk
Source0:	http://www.iceflow.net/themes/gatesofhell.tar.gz
URL:		http://www.iceflow.net/themes/
BuildRequires:	gtk+-devel
Requires:	gtk-engines
# KLOCZEK: jak bedziesz zmienial to i to requires zmien
Requires:	gtk-theme-ThinIce
Requires:	gtk-theme-engine-Xenophilia
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		/usr/X11R6/man

%description
This theme is a work in progress with the ultimate goal of cloning the
look and feel of the Win2k widgets. In order to get the look as close
as possible I made use of multiple theme engines that do not use
pixmaps(for speed reasons).

%description -l pl
Ten temat ma za zadanie sklonowaæ wygl±d i sposób pracy widgetów
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
