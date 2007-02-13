Summary:	Drag and drop files mentioned in the shell
Summary(pl.UTF-8):	Przeciąganie i upuszczanie plików podanych z powłoki
Name:		dragbox
Version:	0.2.3
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.student.lu.se/~cif04usv/publicfiles/%{name}_%{version}.tar.gz
# Source0-md5:	8727bb39c011ed952874365d275ab5fe
URL:		http://www.student.lu.se/~cif04usv/wiki/dragbox.html
BuildRequires:	pkgconfig
BuildRequires:	python-dbus
BuildRequires:	python-gnome-devel
BuildRequires:	python-gnome-ui
BuildRequires:	python-gnome-vfs
BuildRequires:	python-pygtk-devel >= 2:2.6
BuildRequires:	python-pygtk-glade >= 2:2.6
BuildRequires:	rpm-pythonprov
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

%description -l pl.UTF-8
Dragbox to narzędzie do łączenia linii poleceń ze środowiskiem
graficznym. Wywołuje znikąd uchwyt przy zarządzaniu plików lub innych
informacji z powłoki, wspomagając pracę.

Dragbox przyjmuje zarówno przeciągnięcia jak i upuszczenia od chwili
uruchomienia i może wypisać przeciągnięte elementy na standardowym
wyjściu. Można także przekazać do dragboksa tekst potokiem lub listę
plików przy użyciu xargs.

Kliknięcie na elemencie kopiuje go do schowka. Kliknięcie prawym
przyciskiem otwiera menu kontekstowe z dostępem do okna dialogowego
ustawień.

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
