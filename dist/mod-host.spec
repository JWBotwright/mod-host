Name:		mod-host
Version:	0.10.6
Release:	1%{?dist}
Summary:	Mod-devices pedalboard daemon

License:	GNU General Public License
URL:		https://moddevices.com/
Source0:	v0.10.6-432-g81b2567-el7.tar.gz

%description
This is the backend for the MOD software web UI frontend.

%prep
%setup

%build
make

%install
make DESTDIR=%{buildroot} PREFIX=/usr install

%files
%attr(755, root, -) /usr/bin/mod-host
%doc /usr/share/man/man1/mod-host.1.gz
/usr/lib64/jack/fake-input.so
/usr/lib64/jack/mod-host.so
/usr/lib64/jack/mod-monitor.so

%changelog
* Sat Apr 3 2021 JWBotwright <john@johnandlara.plus.com> 0.10.6
- Initial version (0.10.6-432-g81b2567)
