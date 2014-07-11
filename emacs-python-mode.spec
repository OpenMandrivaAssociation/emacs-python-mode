%define rname	python-mode
%define tarname	%{rname}.el

Summary:	An Emacs mode for editing Python code
Name:		emacs-%{rname}
Version:	6.0.10
Release:	8
Source0:	https://launchpad.net/python-mode/trunk/%{version}/+download/%{tarname}-%{version}.tar.gz
License:	GPLv3+
Group:		Editors
Url:		https://launchpad.net/python-mode/
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
mkdir -p %{buildroot}%{_datadir}/emacs/site-lisp

emacs -batch --eval '(progn (byte-compile-file "python-mode.el" t))'
%__install -m 644 python-mode.el* %{buildroot}%{_datadir}/emacs/site-lisp

install -d %{buildroot}%{_sysconfdir}/emacs/site-start.d
cat <<EOF > %{buildroot}%{_sysconfdir}/emacs/site-start.d/python.el
(setq auto-mode-alist (cons '("\\\\.py$" . python-mode) auto-mode-alist))
(setq py-install-directory "/usr/share/emacs/site-lisp")
(autoload 'python-mode "python-mode" "Mode for python files." t)
EOF

%files
%doc LICENSE NEWS README
%_datadir/emacs/site-lisp/*.el*
%config(noreplace) %_sysconfdir/emacs/site-start.d/python.el
