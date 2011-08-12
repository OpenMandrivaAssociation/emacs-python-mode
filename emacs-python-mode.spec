%define rname	python-mode
%define tarname	%{rname}.el
%define name	emacs-%{rname}
%define version	6.0.1
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
Requires:	emacs
BuildRequires:	emacs

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
%__install -m 644 *.el %{buildroot}%{_datadir}/emacs/site-lisp

pushd %{buildroot}%{_datadir}/emacs/site-lisp/
emacs -batch --eval '(progn (byte-compile-file "highlight-indentation.el" t) (byte-compile-file "python-mode.el" t))'
popd

install -d %{buildroot}%{_sysconfdir}/emacs/site-start.d
cat <<EOF > %{buildroot}%{_sysconfdir}/emacs/site-start.d/python.el
(setq auto-mode-alist (cons '("\\\\.py$" . python-mode) auto-mode-alist))
(autoload 'python-mode "python-mode" "Mode for python files." t)
EOF

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE NEWS README
%_datadir/emacs/site-lisp/*.el*
%config(noreplace) %_sysconfdir/emacs/site-start.d/python.el
