%define rname	python-mode
%define tarname	%{rname}.el
%define name	emacs-%{rname}
%define version	6.0.5
%define release %mkrel 1

Summary:	An Emacs mode for editing Python code
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{tarname}-%{version}.tar.gz
License:	GPLv3+
Group:		Editors
Url:		https://launchpad.net/python-mode/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Conflicts:	python < 2.7.1-5
BuildArch:	noarch
Requires:	emacs, emacs-pymacs >= 0.24, python >= 2.7.1-5
BuildRequires:	emacs, emacs-pymacs >= 0.24, python-devel >= 2.7.1-5

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

emacs -batch --eval '(progn (byte-compile-file "column-marker.el" t) (byte-compile-file "python-mode.el" t))'
%__install -m 644 python-mode.el* column-marker.el* %{buildroot}%{_datadir}/emacs/site-lisp

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
