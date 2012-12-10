%define rname	python-mode
%define tarname	%{rname}.el
%define name	emacs-%{rname}
%define version	6.0.10
%define release 1

Summary:	An Emacs mode for editing Python code
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	https://launchpad.net/python-mode/trunk/%{version}/+download/%{tarname}-%{version}.tar.gz
License:	GPLv3+
Group:		Editors
Url:		https://launchpad.net/python-mode/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Conflicts:	python < 2.7.1-5
BuildArch:	noarch
Requires:	emacs, python >= 2.7.1-5
Suggests:	emacs-pymacs
BuildRequires:	emacs, python-devel >= 2.7.1-5

%description
This package contains an Emacs and XEmacs mode for editing, debugging,
and developing Python programs. Note that this mode is different than
the one included by default in Emacs.

%prep
%setup -q -n %{tarname}-%{version}

%build

%install
%__rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/emacs/site-lisp

emacs -batch --eval '(progn (byte-compile-file "python-mode.el" t))'
%__install -m 644 python-mode.el* %{buildroot}%{_datadir}/emacs/site-lisp

install -d %{buildroot}%{_sysconfdir}/emacs/site-start.d
cat <<EOF > %{buildroot}%{_sysconfdir}/emacs/site-start.d/python.el
(setq auto-mode-alist (cons '("\\\\.py$" . python-mode) auto-mode-alist))
(setq py-install-directory "/usr/share/emacs/site-lisp")
(autoload 'python-mode "python-mode" "Mode for python files." t)
EOF

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE NEWS README
%_datadir/emacs/site-lisp/*.el*
%config(noreplace) %_sysconfdir/emacs/site-start.d/python.el


%changelog
* Thu Jun 28 2012 Lev Givon <lev@mandriva.org> 6.0.10-1
+ Revision: 807412
- Update to 6.0.10.

* Mon May 07 2012 Lev Givon <lev@mandriva.org> 6.0.7-1
+ Revision: 797319
- Update to 6.0.7.

* Sun Apr 22 2012 Lev Givon <lev@mandriva.org> 6.0.6-1
+ Revision: 792710
- Update to 6.0.6.

* Tue Mar 13 2012 Lev Givon <lev@mandriva.org> 6.0.5-1
+ Revision: 784708
- Update to 6.0.5.
  Add pymacs dependency.

* Mon Jan 16 2012 Lev Givon <lev@mandriva.org> 6.0.4-1
+ Revision: 761652
- Update to 6.0.4.

* Mon Dec 19 2011 Lev Givon <lev@mandriva.org> 6.0.3-1
+ Revision: 743819
- Update to 6.0.3

* Fri Aug 12 2011 Lev Givon <lev@mandriva.org> 6.0.1-1
+ Revision: 694250
- Update to 6.0.1.

* Thu Mar 03 2011 Lev Givon <lev@mandriva.org> 5.2.0-1
+ Revision: 641444
- import emacs-python-mode


