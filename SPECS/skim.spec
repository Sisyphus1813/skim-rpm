Name:           skim
Version:        3.4.0
Release:        1%{?dist}
Summary:        A powerful fuzzy finder designed to make your workflow faster and more efficient.
License:        MIT
URL:            https://github.com/skim-rs/skim

Source0:        https://github.com/skim-rs/skim/archive/refs/tags/v%{version}.tar.gz
Source1:        skim-%{version}-vendor.tar.gz

ExclusiveArch:  x86_64 aarch64

BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  pkgconfig

%description
skim is a fuzzy finder written in Rust.
This is an unofficial COPR packaging of skim and is maintained independently.
Upstream project: https://github.com/skim-rs/skim

%prep
%autosetup
%{__tar} -xzf %{SOURCE1}

%build
export CARGO_NET_OFFLINE=true
cargo build --release

%check
./target/release/sk --version

%install
install -Dpm0755 target/release/sk %{buildroot}%{_bindir}/sk
install -Dpm0644 man/man1/sk.1 %{buildroot}%{_mandir}/man1/sk.1
install -Dpm0644 shell/completion.bash %{buildroot}%{_datadir}/bash-completion/completions/sk
install -Dpm0644 shell/completion.zsh %{buildroot}%{_datadir}/zsh/site-functions/_sk
install -Dpm0644 shell/completion.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/sk.fish
install -Dpm0644 shell/completion.nu %{buildroot}%{_datadir}/nushell/completions/sk.nu
install -d -m 0755 %{buildroot}%{_datadir}/skim
install -Dpm0644 shell/key-bindings.* %{buildroot}%{_datadir}/skim/

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/sk
%{_mandir}/man1/sk.*
%{_datadir}/bash-completion/completions/sk
%{_datadir}/zsh/site-functions/_sk
%{_datadir}/fish/vendor_completions.d/sk.fish
%{_datadir}/nushell/completions/sk.nu
%{_datadir}/skim/key-bindings.bash
%{_datadir}/skim/key-bindings.fish
%{_datadir}/skim/key-bindings.zsh

%changelog
* Thu Feb 19 2026 Fedora COPR <sisyphus1813@protonmail.com> - 3.4.0
- Initial COPR build of skim
