#
Summary:	Drag and drop files mentioned in the shell
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

%prep
%setup -q

# undos the source
#find '(' -name '*.php' -o -name '*.inc' ')' -print0 | xargs -0 sed -i -e 's,\r$,,'

# remove CVS control files
#find -name CVS -print0 | xargs -0 rm -rf

# you'll need this if you cp -a complete dir in source
# cleanup backups after patching
find . '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f

%build
# if ac/am/* rebuilding is necessary, do it in this order and add
# appropriate BuildRequires
#%%{__intltoolize}
#%%{__gettextize}
#%%{__libtoolize}
#%%{__aclocal}
#%%{__autoconf}
#%%{__autoheader}
#%%{__automake}
#cp -f /usr/share/automake/config.sub .
%configure
%{__make}

#%{__make} \
#	CFLAGS="%{rpmcflags}" \
#	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post

%preun

%postun

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/dragbox
%{_mandir}/man1/dragbox.1*
%dir %{py_sitescriptdir}/Dragbox
%{py_sitescriptdir}/Dragbox/*.py[oc]
