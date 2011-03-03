%define rname	python-mode
%define name	emacs-%{rname}
%define version	5.2.0
%define release %mkrel 1

Summary:	An Emacs mode for editing Python code
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{rname}-%{version}.tgz
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
%setup -q -n %{rname}

%build

%install
%__rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/emacs/site-lisp
%__install -m 644 python-mode.el %{buildroot}%{_datadir}/emacs/site-lisp
emacs -batch -f batch-byte-compile %{buildroot}%{_datadir}/emacs/site-lisp/*.el

install -d %{buildroot}%{_sysconfdir}/emacs/site-start.d
cat <<EOF > %{buildroot}%{_sysconfdir}/emacs/site-start.d/python.el
(setq auto-mode-alist (cons '("\\\\.py$" . python-mode) auto-mode-alist))
(autoload 'python-mode "python-mode" "Mode for python files." t)
EOF

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc NEWS
%_datadir/emacs/site-lisp/%rname.el*
%config(noreplace) %_sysconfdir/emacs/site-start.d/python.el
