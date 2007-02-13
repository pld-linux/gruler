Summary:	GNOME Screen Ruler
Summary(pl.UTF-8):	Linijka ekranowa dla GNOME
Name:		gruler
Version:	0.6
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://linuxadvocate.org/projects/gruler/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	62f5c8e1814b615456be76f9677e6d49
Patch0:		%{name}-desktop.patch
URL:		http://linuxadvocate.org/projects/gruler/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel >= 0.10.40
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A customizable screen ruler for GNOME.

%description -l pl.UTF-8
Konfigurowalna linijka ekranowa dla GNOME.

%prep
%setup -q
%patch0 -p1

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake} 
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}/%{name}-icon.png \
	$RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png
mv -f $RPM_BUILD_ROOT%{_datadir}/gnome/apps/Utilities/* \
	$RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/gruler
%{_datadir}/%{name}
%{_pixmapsdir}/%{name}.png
%{_desktopdir}/%{name}.desktop
