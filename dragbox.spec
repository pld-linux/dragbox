Summary:	Drag and drop files mentioned in the shell
Summary(pl):	Przeci�ganie i upuszczanie plik�w podanych z pow�oki
Name:		dragbox
Version:	0.2.3
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.student.lu.se/~cif04usv/publicfiles/%{name}_%{version}.tar.gz
# Source0-md5:	8727bb39c011ed952874365d275ab5fe
URL:		http://www.student.lu.se/~cif04usv/wiki/dragbox.html
BuildRequires:	python-dbus
BuildRequires:	python-gnome-devel
BuildRequires:	python-gnome-ui
BuildRequires:	python-gnome-vfs
BuildRequires:	python-pygtk-devel
BuildRequires:	python-pygtk-glade
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dragbox is a tool for connecting the commandline with the desktop
environment. It summons a drag handle from nowhere when you are
managing files or information in a shell, further empowering you in
your workflow.

Dragbox accepts both drags and drops once started, and can be made to
output dragged-to items to the standard output. You can also pipe text
to dragbox, or a list of files using xargs.

Clicking an item copies it to the clipboard. Right-clicking opens a
context menu with access to the preferences dialog.

%description -l pl
Dragbox to narz�dzie do ��czenia linii polece� ze �rodowiskiem
graficznym. Wywo�uje znik�d uchwyt przy zarz�dzaniu plik�w lub innych
informacji z pow�oki, wspomagaj�c prac�.

Dragbox przyjmuje zar�wno przeci�gni�cia jak i upuszczenia od chwili
uruchomienia i mo�e wypisa� przeci�gni�te elementy na standardowym
wyj�ciu. Mo�na tak�e przekaza� do dragboksa tekst potokiem lub list�
plik�w przy u�yciu xargs.

Klikni�cie na elemencie kopiuje go do schowka. Klikni�cie prawym
przyciskiem otwiera menu kontekstowe z dost�pem do okna dialogowego
ustawie�.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/dragbox
%{_mandir}/man1/dragbox.1*
%dir %{py_sitescriptdir}/Dragbox
%{py_sitescriptdir}/Dragbox/*.py[co]
